import time
import allure
from pages.base_page import BasePage
from utils.waits import WaitUtils
from core.logger import get_logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.locators.web_locators import OnboardPrinterPageLocators


class OnboardPrinterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitUtils(driver)
        self.logger = get_logger(self.__class__.__name__)

    # --------------------------------------------------------------
    # OPEN PRINTER URL (Correct driver usage)
    # --------------------------------------------------------------
    def open_printer_url(self, printer_url):

        driver = self.driver.driver  

        self.logger.info(f"Opening printer onboarding URL: {printer_url}")

        try:
            # New tab
            with allure.step("Open URL in new tab"):
                driver.execute_script("window.open('');")
                printer_tab = driver.window_handles[-1]
                driver.switch_to.window(printer_tab)
                driver.get(printer_url)
                time.sleep(2)

            # Login check
            with allure.step("Check login status"):
                if "user_not_logged" in driver.current_url:
                    self.logger.warning("Detected 'user_not_logged' — retrying")
                    driver.get(printer_url)
                    time.sleep(2)

            # Accept cookies
            with allure.step("Accept cookies popup if present"):
                try:
                    WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located(OnboardPrinterPageLocators.ACCEPT_BUTTON)
                    )
                    self.click(*OnboardPrinterPageLocators.ACCEPT_BUTTON)
                    self.logger.info("Clicked 'Accept Cookies'")
                except TimeoutException:
                    self.logger.info("No cookie popup found")

            # Close old tabs
            with allure.step("Close old tabs"):
                while len(driver.window_handles) > 1:
                    driver.switch_to.window(driver.window_handles[0])
                    driver.close()
                driver.switch_to.window(printer_tab)

            self.logger.info("Printer onboarding URL opened successfully")

        except Exception as e:
            self.logger.error(f"open_printer_url failed: {e}")

    # --------------------------------------------------------------
    # ENTER CLAIM CODE
    # --------------------------------------------------------------
    def enter_claim_code(self, claim_code):
        self.logger.info(f"Entering claim code: {claim_code}")
        with allure.step("Enter Claim Code"):
            self.enter_text(*OnboardPrinterPageLocators.CLAIM_CODE_INPUT, claim_code)

    # --------------------------------------------------------------
    # CLICK ADD PRINTER
    # --------------------------------------------------------------
    def click_add_printer(self):
        self.logger.info("Clicking Add Printer button")
        with allure.step("Click Add Printer"):
            self.click(*OnboardPrinterPageLocators.ADD_BUTTON)

        # Example of opening new tab after click
        driver = self.driver.driver
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get("https://instantink-stage1.hpconnectedstage.com/us/en/l/v2")
