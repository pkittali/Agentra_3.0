import random
import string
import time
import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import SpecialOffersPageLocators
from core.logger import get_logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains

class SpecialOffersPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def get_require_billing_message_text(self):
        self.logger.info("Getting 'Require Billing Information' message text")
        with allure.step("Fetched 'Require Billing Information' message text"):
            return self.get_text(*SpecialOffersPageLocators.REQUIRE_BILLING_TEXT)
        
    def get_enrollment_key_label(self):
        self.logger.info("Getting 'Enrollment Key' label text")
        with allure.step("Fetched 'Enrollment Key' label text"):
            return self.get_text(*SpecialOffersPageLocators.ENROLLMENT_KEY_LABEL)
        
    def get_enrollment_key_verifymonths_text(self):
        self.logger.info("Getting 'Verify Months' text for Enrollment Key")
        with allure.step("Fetched 'Verify Months' text for Enrollment Key"):
            return self.get_text(*SpecialOffersPageLocators.ENROLLMENT_KEY_MONTHS_TEXT)
        
    

    

    

   