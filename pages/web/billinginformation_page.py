import random
import string
import time
import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import BillingInformationPageLocators
from core.logger import get_logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains

class BillingInformationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def click_continue(self):
        self.logger.info("Clicking Continue button")
        with allure.step("Clicked Continue button"):
            self.click(*BillingInformationPageLocators.CONTINUE_BUTTON) 

   