import random
import string
import time
import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import ThankYouPageLocators
from core.logger import get_logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains

class ThankYouPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    # def click_arn_checkbox_1(self):
    #     self.logger.info("Clicking HP Checkout button")
    #     with allure.step("Clicked HP Checkout button"):
    #         self.click(*ARNPageLocators.ARN_CHECK_BOX_1) 

    # def is_enroll_button_enabled(self):
    #     self.logger.info("Checking if Enroll button is enabled")
    #     with allure.step("Check if Enroll button is enabled"):
    #         enroll_button = self.wait.wait_until_visible(*ARNPageLocators.ARN_ENROLL_BUTTON)
    #         if enroll_button:
    #             return enroll_button.is_enabled()
    #         return False
        
    # def click_enroll_button(self):
    #     self.logger.info("Clicking Enroll button")
    #     with allure.step("Click Enroll button"):
    #         assert self.is_enroll_button_enabled(), "Enroll button is not enabled"
    #         self.click(*ARNPageLocators.ARN_ENROLL_BUTTON)

    #to check is visible and scroll to checkbox1 and then click
    def validate_confirmation_text(self):
        self.logger.info("Validating Thank You Page confirmation text")
        with allure.step("Validating Thank You Page confirmation text"):
            confirmation_text = self.wait.wait_until_visible(*ThankYouPageLocators.SUCCESS_CONTAINER)
            assert "success!" in confirmation_text and "you’re signed up." in confirmation_text, \
                "'Success!' and 'You’re signed up.' messages should both be present after signup"
            

    def click_continue(self):
        self.logger.info("Clicking Continue button on Thank You Page")
        with allure.step("Click Continue button on Thank You Page"):
            self.click(*ThankYouPageLocators.CONTINUE_BUTTON)

    def click_full_screen_continue_button(self):
        self.logger.info("Clicking Full Screen Continue button on Thank You Page")
        with allure.step("Click Full Screen Continue button on Thank You Page"):
            self.click(*ThankYouPageLocators.FULL_SCREEN_CONTINUE_BUTTON)
