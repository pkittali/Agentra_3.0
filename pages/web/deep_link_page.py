import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.logger import get_logger
from pages.base_page import BasePage
from resources.locators.web_locators import DeepLinkLocators
from utils.waits import WaitUtils


class DeepLinkPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.logger=get_logger(self.__class__.__name__)
        self.wait=WaitUtils(driver)
    # -------------------------
    # URL VALIDATION
    # -------------------------
    def verify_deeplink_page_loaded(self, timeout=20):
        with allure.step("Verify DeepLink page URL is loaded"):
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(DeepLinkLocators.EXPECTED_URL_SUBSTRING)
            )

            actual_url = self.driver.current_url
            self.logger.info(f"DeepLink URL: {actual_url}")

            if DeepLinkLocators.EXPECTED_URL_SUBSTRING not in actual_url:
                raise AssertionError(
                    f"URL does not contain expected substring. Actual URL: {actual_url}"
                )

            return actual_url

    # -------------------------
    # BUTTON VISIBILITY CHECK
    # -------------------------
    def is_connect_printer_later_visible(self, timeout=20):
        with allure.step("Check 'Connect Printer Later' button visibility"):
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(DeepLinkLocators.CONNECT_PRINTER_LATER)
            )
            return element.is_displayed()

    # -------------------------
    # BUTTON CLICK
    # -------------------------
    def click_connect_printer_later(self, timeout=20):
        with allure.step("Click 'Connect Printer Later' button"):
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(DeepLinkLocators.CONNECT_PRINTER_LATER)
            )
            self.click(DeepLinkLocators.CONNECT_PRINTER_LATER)
