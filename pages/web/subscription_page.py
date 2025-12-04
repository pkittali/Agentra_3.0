import random
import string
import time
import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import SubscriptionPageLocators, ThankYouPageLocators
from core.logger import get_logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains

class SubscriptionPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def click_accept_all_button(self):
        self.logger.info("Clicking Accept All button on consent pop-up")
        with allure.step("Click Accept All button on consent pop-up"):
            self.click(*SubscriptionPageLocators.ACCEPT_ALL)
       
    def click_pop_up_continue_button(self):
        self.logger.info("Clicking Continue button on pop-up")
        with allure.step("Click Continue button on pop-up"):
            self.click(*SubscriptionPageLocators.POP_UP_CONTINUE_BUTTON)

    def click_skip_button(self):
        self.logger.info("Clicking Skip button on pop-up")
        with allure.step("Click Skip button on pop-up"):
            self.click(*SubscriptionPageLocators.SKIP_BUTTON)

    def click_close_modal_if_present(self):
        self.logger.info("Closing modal if present")
        with allure.step("Close modal if present"):
            try:
                close_button = self.wait.wait_until_visible(*SubscriptionPageLocators.CLOSE_BUTTON)
                close_button.click()
                self.logger.info("Modal closed successfully")
            except TimeoutException:
                self.logger.info("No modal present to close")

    def get_free_months_message(self):
        self.logger.info("Retrieving free months message from Subscription Page")
        with allure.step("Get free months message from Subscription Page"):
            message_element = self.wait.wait_until_visible(*SubscriptionPageLocators.FREE_MONTHS_MESSAGE)
            message = message_element.text
            self.logger.info(f"Free Months Message: {message}")
            return message

    def validate_subscription_plan_details(self):
        self.logger.info("Validating subscription plan details on Subscription Page")
        with allure.step("Validate subscription plan details on Subscription Page"):
            months_validation = self.get_free_months_message()
            normalized_text = re.sub(r'\s+', ' ', months_validation).lower()
            pattern = r'get \d+ free months, starting when you install instant ink cartridges'
            assert re.search(pattern, normalized_text), \
            f"Expected message pattern not found.\nActual message: {months_validation}"