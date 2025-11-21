import time
import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import ShippingBillingPageLocators
from core.logger import get_logger

class ShippingBillingPage(BasePage):
    def __init__(self, driver, config):
        super().__init__(driver, config)
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
        
    



    def is_login_successful(self):
        self.logger.info("Checking if login was successful")
        with allure.step("Check if login was successful"):
            return self.driver.find_element(*LoginPageLocators.SUCCESS_MESSAGE).is_displayed()
