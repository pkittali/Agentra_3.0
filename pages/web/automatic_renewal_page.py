import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import ARNPageLocators
from core.logger import get_logger

class ARNPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def click_arn_checkbox_1(self):
        self.logger.info("Clicking HP Checkout button")
        with allure.step("Clicked HP Checkout button"):
            self.click(*ARNPageLocators.ARN_CHECK_BOX_1) 

    def is_enroll_button_enabled(self):
        self.logger.info("Checking if Enroll button is enabled")
        with allure.step("Check if Enroll button is enabled"):
            enroll_button = self.wait.wait_until_visible(*ARNPageLocators.ARN_ENROLL_BUTTON)
            if enroll_button:
                return enroll_button.is_enabled()
            return False
        
    def click_enroll_button(self):
        self.logger.info("Clicking Enroll button")
        with allure.step("Click Enroll button"):
            assert self.is_enroll_button_enabled(), "Enroll button is not enabled"
            self.click(*ARNPageLocators.ARN_ENROLL_BUTTON)

    #to check is visible and scroll to checkbox1 and then click
    def validate_and_click_arn_checkbox_1(self):
        self.logger.info("Validating and clicking ARN checkbox 1")
        with allure.step("Validating and clicking ARN checkbox 1"):
            assert self.wait.wait_until_visible(*ARNPageLocators.ARN_CHECK_BOX_1), "Checkbox not visible"  
            self.scroll(*ARNPageLocators.ARN_CHECK_BOX_1)
            self.click_arn_checkbox_1()
            
            

        
