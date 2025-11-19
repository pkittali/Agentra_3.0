"""
BasePage Module
===============

This module defines the BasePage class, which acts as the foundation for all
Page Object classes in the Agentra automation framework. It provides an
abstraction layer over platform- or tool-specific drivers (Web, Mobile, Desktop),
ensuring consistent, reusable, and tool-agnostic interactions.

Key Responsibilities
--------------------
1. Driver Abstraction
2. Common Interactions (click, enter_text, get_text)
3. Unified Wait Handling
4. Logging Integration
5. Allure Reporting
6. Centralized Error Handling via safe_action()

Design Principles
-----------------
- Tool-Agnostic API
- Single Source of Truth for interaction logic
- Extensible for platform-specific enhancements
- Consistent logging + reporting behavior
"""

import time
import traceback
import allure

# Selenium exceptions
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)

#test
# Appium exceptions
try:
    from appium.webdriver.common.exceptions import WebDriverException as AppiumDriverException
except Exception:
    AppiumDriverException = WebDriverException

# Desktop exceptions (pywinauto)
try:
    from pywinauto.findwindows import ElementNotFoundError
except Exception:
    ElementNotFoundError = Exception  # fallback for non-desktop envs

from core.logger import get_logger, log_allure


class BasePage:
    """Base class for all Page Objects providing safe UI interactions."""

    RETRY_EXCEPTIONS = (
        StaleElementReferenceException,
        NoSuchElementException,
        TimeoutException,
        ElementNotInteractableException
    )    
    RETRIES = 2

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def _safe_action(self, action_name, func, *args, **kwargs):
        """
        Retries ANY exception up to RETRIES times.
        Only fails after all retries have been exhausted.
        """

        for attempt in range(1, self.RETRIES + 2):  # RETRIES + initial attempt

            try:
                with allure.step(f"{action_name} (Attempt {attempt})"):
                    self.logger.info(f"{action_name} - Attempt {attempt}")
                    log_allure(f"{action_name} - Attempt {attempt}")
                    return func(*args, **kwargs)   # SUCCESS → exit immediately

            except Exception as e:

                # RETRY if attempts still available
                if attempt <= self.RETRIES:
                    self.logger.warning(
                        f"{action_name} failed with {type(e).__name__}. "
                        f"Retrying {attempt}/{self.RETRIES}..."
                    )
                    time.sleep(0.3)
                    continue  # <-- RETRY HERE

                # ALL RETRIES EXHAUSTED → FAIL
                return self._fail(
                    action_name,
                    f"Failed after {self.RETRIES} retries ({type(e).__name__})",
                    e
                )


    # ----------------------------------------------------------------------
    # FAILURE HANDLER
    # ----------------------------------------------------------------------
    def _fail(self, action_name, title, exception_obj):
        """Capture logs, screenshot, and raise failures cleanly."""

        error_msg = f"❌ {title} during: {action_name}\n{str(exception_obj)}"
        self.logger.error(error_msg)
        self.logger.debug(traceback.format_exc())

        # Screenshot attachment
        try:
            if hasattr(self.driver, "driver") and hasattr(self.driver.driver, "get_screenshot_as_png"):
                screenshot = self.driver.driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception:
            pass  # Don't mask the original error

        # Text stack trace
        allure.attach(
            traceback.format_exc(),
            name="Error Trace",
            attachment_type=allure.attachment_type.TEXT
        )

        raise exception_obj  # important: propagate failure to test

    # ----------------------------------------------------------------------
    # PUBLIC INTERACTION WRAPPERS
    # ----------------------------------------------------------------------
    def click(self, locator_type, locator_value):
        """Safely click an element."""
        action_name = f"Clicking element ({locator_type}, {locator_value})"
        return self._safe_action(
            action_name,
            self._click,
            locator_type,
            locator_value
        )

    def _click(self, locator_type, locator_value):
        self.driver.wait_for_element(locator_type, locator_value)
        self.driver.click(locator_type, locator_value)

    def enter_text(self, locator_type, locator_value, text):
        """Safely enter text into an input field."""
        action_name = f"Entering '{text}' into ({locator_type}, {locator_value})"
        return self._safe_action(
            action_name,
            self._enter_text,
            locator_type,
            locator_value,
            text
        )

    def _enter_text(self, locator_type, locator_value, text):
        self.driver.wait_for_element(locator_type, locator_value)
        self.driver.send_keys(locator_type, locator_value, text)

    def get_text(self, locator_type, locator_value):
        """Safely fetch visible text from an element."""
        action_name = f"Fetching text from ({locator_type}, {locator_value})"
        return self._safe_action(
            action_name,
            self._get_text,
            locator_type,
            locator_value
        )

    def _get_text(self, locator_type, locator_value):
        el = self.driver.find_element(locator_type, locator_value)
        return el.text if el else None
