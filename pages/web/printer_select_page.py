import time
import allure
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from resources.locators.web_locators import PrinterSelectionPageLocators
from core.logger import get_logger


class PrinterSelectionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitUtils(driver)
        self.logger = get_logger(self.__class__.__name__)

    def select_printer(self):
        driver = self.driver.driver  
        self.logger.info("Selecting printer from card list")

        with allure.step("Select Printer"):
            wait = WebDriverWait(driver, 20)
            element = wait.until(
                EC.visibility_of_element_located(PrinterSelectionPageLocators.ADD_PRINTER_CARD_RADIO)
            )

            # Scroll into view
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(1)

            # Click if not selected
            if not element.is_selected():
                wait.until(
                    EC.element_to_be_clickable(PrinterSelectionPageLocators.ADD_PRINTER_CARD_RADIO)
                )
                ActionChains(driver).move_to_element(element).click().perform()
                self.logger.info("Printer radio button selected")
            else:
                self.logger.info("Printer already selected")

    def scroll_to_continue(self):
        driver = self.driver.driver
        self.logger.info("Scrolling to Continue button")
        with allure.step("Scroll to Continue Button"):
            btn = self.wait.wait_for_element_to_be_clickable(
                *PrinterSelectionPageLocators.CONTINUE_BUTTON, timeout=10
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            time.sleep(1)


    def click_continue(self):
        self.logger.info("Clicking Continue button")
        with allure.step("Click Continue"):
            self.click(*PrinterSelectionPageLocators.CONTINUE_BUTTON)

    def printer_selection(self):
        self.logger.info("Starting printer selection process")
        with allure.step("Start Printer Selection Flow"):
            self.select_printer()
            self.scroll_to_continue()
            self.click_continue()
        self.logger.info("Printer selection process complete")
