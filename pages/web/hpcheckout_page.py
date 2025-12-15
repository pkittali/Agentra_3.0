import allure
from pages.base_page import BasePage
from resources.locators.web_locators import HPCheckoutPageLocators
from utils.waits import WaitUtils
from core.logger import get_logger
from selenium.common.exceptions import TimeoutException

class HPCheckoutPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def click_hp_checkout(self):
        self.logger.info("Clicking HP Checkout button")
        with allure.step("Clicked HP Checkout button"):
            try:
                element = self.wait.wait_until_clickable(*HPCheckoutPageLocators.HP_CHECKOUT_BUTTON, timeout=40)
                if element:
                    self.click(*HPCheckoutPageLocators.HP_CHECKOUT_BUTTON)
            except TimeoutException:
                self.logger.warning("HP Checkout button not visible — continuing flow")
                pass