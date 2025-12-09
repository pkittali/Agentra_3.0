import time
import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import ShippingBillingPageLocators
from core.logger import get_logger

class ShippingBillingPage(BasePage):
    # def __init__(self, driver, config):
    #     super().__init__(driver, config)
    #     self.driver = driver
    #     self.logger = get_logger(self.__class__.__name__)
    #     self.wait = WaitUtils(driver)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def click_continue_button(self):
        self.logger.info("Clicking Continue button on Shipping and Billing page")
        with allure.step("Click Continue button"):
            self.click(*ShippingBillingPageLocators.CONTINUE_TO_ENROLL)
    
    def is_continue_button_visible(self):
        self.logger.info("Checking if Add Billing button is visible")
        with allure.step("Check if Add Billing button is visible"):
            return self.is_element_visible(*ShippingBillingPageLocators.ADD_BILLING_BUTTON)
        
    def click_add_shipping(self):
        self.logger.info("Clicking Add Shipping button")
        with allure.step("Click Add Shipping button"):
            self.click(*ShippingBillingPageLocators.ADD_SHIPPING_BUTTON)

    def click_add_billing(self):
        self.logger.info("Clicking Add Billing button")
        with allure.step("Click Add Billing button"):
            self.click(*ShippingBillingPageLocators.ADD_BILLING_BUTTON)

    def click_apply_promotion(self):
        self.logger.info("Clicking Apply Promotion link")
        with allure.step("Click Apply Promotion link"):
            self.click(*ShippingBillingPageLocators.APPLY_PROMOTION_BUTTON)
        
    



    
