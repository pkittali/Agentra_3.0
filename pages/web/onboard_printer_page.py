import time
import allure
from core.configManager import ConfigManager
from pages.base_page import BasePage
from resources.locators.web_locators import OnboardPrinterPageLocators
from utils.waits import WaitUtils
from core.logger import get_logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class OnboardPrinterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitUtils(driver)
        self.logger = get_logger(self.__class__.__name__)

    def open_printer_url(self, printer_url):
        driver = self.driver.driver
        logger = self.logger
        logger.info(f"Opening printer onboarding URL: {printer_url}")
        try:
            with allure.step("Verify user is logged in"):
                current_url = driver.current_url
                logger.info(f"Current URL: {current_url}")

                # If user is on login page → wait until logged in
                if "login" in current_url or "sign" in current_url:
                    logger.info("User appears to be on login page — waiting for login to complete")

                    WebDriverWait(driver, 60).until(
                        lambda d: "login" not in d.current_url and "sign" not in d.current_url
                    )

                    logger.info("Login completed successfully")

            # ---------- OPEN NEW TAB ----------
            with allure.step("Open new tab for printer onboarding"):
                driver.execute_script("window.open('');")
                all_tabs = driver.window_handles
                printer_tab = all_tabs[-1]

                driver.switch_to.window(printer_tab)
                logger.info(f"Switched to new printer tab: {printer_tab}")

                driver.get(printer_url)
                logger.info(f"Navigated to printer URL: {printer_url}")

                time.sleep(2)

            # ---------- CHECK LOGIN STATUS ----------
            with allure.step("Validate login status on printer page"):
                if "user_not_logged" in driver.current_url:
                    logger.warning("Page indicates user is NOT logged in — retrying once")
                    driver.get(printer_url)
                    time.sleep(2)

            # ---------- ACCEPT COOKIES ----------
            with allure.step("Handle cookie acceptance popup"):
                try:
                    WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located(OnboardPrinterPageLocators.ACCEPT_BUTTON)
                    )
                    self.click(*OnboardPrinterPageLocators.ACCEPT_BUTTON)
                    logger.info("Clicked Accept Cookies button")
                except TimeoutException:
                    logger.info("No cookie popup found")

            # ---------- CLOSE PREVIOUS TAB ----------
            with allure.step("Close previous tab after URL stabilizes"):
                all_tabs = driver.window_handles

                if len(all_tabs) > 1:
                    old_tab = all_tabs[0]
                    logger.info(f"Closing old tab: {old_tab}")

                    driver.switch_to.window(old_tab)
                    driver.close()

                    driver.switch_to.window(printer_tab)
                    logger.info("Switched back to printer tab")

            logger.info("Printer onboarding URL opened successfully")

        except Exception as e:
            logger.error(f"open_printer_url failed: {e}")

            # Attach screenshot in Allure
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="open_printer_url_failure",
                    attachment_type=allure.attachment_type.PNG
                )
            except:
                pass

            allure.attach(str(e), "Exception Details", allure.attachment_type.TEXT)
            raise e


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
        url = ConfigManager.get_url("instantink_landing_url")
        self.driver.get(url)
        self.driver.driver.maximize_window()
        # driver.get("https://instantink-stage1.hpconnectedstage.com/us/en/l/v2")
