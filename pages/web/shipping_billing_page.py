import allure
from pages.base_page import BasePage
from resources.locators.web_locators import ShippingBillingPageLocators
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from core.logger import get_logger

class ShippingBillingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def click_add_shipping(self):
        self.logger.info("Clicking Add Shipping button")
        with allure.step("Click Add Shipping button"):
            self.click(*ShippingBillingPageLocators.ADD_SHIPPING_BUTTON)

    def click_add_billing(self):
        self.logger.info("Clicking Add Billing button")
        with allure.step("Click Add Billing button"):
            self.click(*ShippingBillingPageLocators.ADD_BILLING_BUTTON)

    def click_continue_button(self):
        self.logger.info("Clicking Continue button on Shipping and Billing page")
        with allure.step("Click Continue button"):
            self.click(*ShippingBillingPageLocators.CONTINUE_TO_ENROLL)