# pages/base_page.py (fixed)
import time
import traceback
import allure
from core.configManager import ConfigManager
from core.logger import get_logger
from utils.self_healing import SelfHealingEngine
from selenium.webdriver.support.ui import Select
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.RETRIES = ConfigManager.get_retry_count("step_retry") or 1

        try:
            self.healer = SelfHealingEngine(driver)
        except Exception:
            self.healer = None

    # ----------------------------------------------------------------------
    # SAFE ACTION
    # ----------------------------------------------------------------------
    def _safe_action(self, action_name, func, locator, *args):
        """
        locator is passed as ONE item always.
        """
        healed_locator = None

        for attempt in range(1, self.RETRIES + 2):
            try:
                with allure.step(f"{action_name} (Attempt {attempt})"):
                    active_locator = healed_locator or locator
                    self.logger.info(f"{action_name} - Attempt {attempt}")
                    return func(active_locator, *args)

            except Exception as e:
                self.logger.warning(f"{action_name} failed: {type(e).__name__}: {e}")
                self._attach_screenshot(f"{action_name}_attempt_{attempt}")

                # Self-healing only on first failure
                if attempt == 1 and self.healer is not None:
                    healed_locator = self.healer.self_heal_locator(locator)
                    if healed_locator:
                        self.logger.info(f"Applied healed locator: {healed_locator}")
                        continue  # retry using healed locator

                if attempt <= self.RETRIES:
                    time.sleep(0.3)
                    continue

                return self._fail(
                    action_name,
                    f"Failed after {self.RETRIES} retries ({type(e).__name__})",
                    e
                )

    # ----------------------------------------------------------------------
    # CLICK
    # ----------------------------------------------------------------------
    def click(self, locator):
        return self._safe_action(f"Click {locator}", self._click, locator)

    def _click(self, locator):
        # Web/Appium tuple
        if isinstance(locator, tuple):
            by, value = locator

            # If DriverManager exists
            if hasattr(self.driver, "wait_for_element"):
                self.driver.wait_for_element(by, value)
                return self.driver.click(by, value)

            # RAW Selenium fallback
            el = self.driver.find_element(by, value)
            return el.click()

        # Desktop dictionary
        elif isinstance(locator, dict):
            if hasattr(self.driver, "wait_for_element"):
                el = self.driver.wait_for_element(locator)
                return el.click_input()

            # fallback for raw win32 wrappers
            el = self.driver.child_window(**locator)
            return el.click_input()

        raise ValueError(f"Unsupported locator: {locator}")
    # ----------------------------------------------------------------------
    # ENTER TEXT
    # ----------------------------------------------------------------------
    def enter_text(self, locator, text):
        return self._safe_action(f"Enter '{text}'", self._enter_text, locator, text)

    def _enter_text(self, locator, text):
        if isinstance(locator, tuple):
            by, value = locator

            # Use manager if available
            if hasattr(self.driver, "wait_for_element"):
                self.driver.wait_for_element(by, value)
                return self.driver.send_keys(by, value, text)

            # Raw Selenium fallback
            el = self.driver.find_element(by, value)
            el.clear()
            return el.send_keys(text)

        elif isinstance(locator, dict):
            if hasattr(self.driver, "wait_for_element"):
                el = self.driver.wait_for_element(locator)
                return el.set_edit_text(text)

            # Fallback
            el = self.driver.child_window(**locator)
            return el.set_edit_text(text)

    # ----------------------------------------------------------------------
    # GET TEXT
    # ----------------------------------------------------------------------
    def get_text(self, locator):
        action = f"Get text from {locator}"
        return self._safe_action(action, self._get_text, locator)

    def _get_text(self, locator):
        if isinstance(locator, tuple) and len(locator) == 2:
            by, value = locator
            el = self.driver.find_element(by, value)
            return el.text

        elif isinstance(locator, dict):
            el = self.driver.find_element(locator)
            return getattr(el, "window_text", lambda: el.text)()

        return None

    # ----------------------------------------------------------------------
    # FAILURE HANDLER
    # ----------------------------------------------------------------------
    def _fail(self, action_name, title, exception_obj):
        msg = f"{title} during: {action_name}\n{exception_obj}"
        self.logger.error(msg)

        raise AssertionError(msg)

    # ----------------------------------------------------------------------
    # SCREENSHOT
    # ----------------------------------------------------------------------
    def _attach_screenshot(self, name):
        try:
            raw = getattr(self.driver, "driver", None)
            if raw and hasattr(raw, "get_screenshot_as_png"):
                allure.attach(
                    raw.get_screenshot_as_png(),
                    name=name,
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception:
            pass
    
    def select_dropdown_by_value(self, locator, value, timeout=15):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            Select(element).select_by_value(str(value))
        except TimeoutException:
            raise Exception(f"Dropdown with locator {locator} not found within {timeout} seconds.")
        except Exception as e:
            raise Exception(f"Could not select value '{value}' in dropdown {locator}: {e}")