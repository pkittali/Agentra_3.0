import random
import string
import time
import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import HPCheckoutPageLocators
from core.logger import get_logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains

class HPCheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def click_hp_checkout(self):
        self.logger.info("Clicking HP Checkout button")
        with allure.step("Clicked HP Checkout button"):
            element=self.wait.wait_until_visible(*HPCheckoutPageLocators.HP_CHECKOUT_BUTTON)
            if element:
                self.click(*HPCheckoutPageLocators.HP_CHECKOUT_BUTTON)
            else:
                pass

    def click_edit_plan(self):
        self.logger.info("Clicking Edit Plan button")
        with allure.step("Clicked Edit Plan button"):
            self.click(*HPCheckoutPageLocators.EDIT_PLAN_BUTTON)

    # def click_paypal_express(self):
    #     self.logger.info("Clicking PayPal Express button")
    #     with allure.step("Clicked PayPal Express button"):
    #         self.click(*HPCheckoutPageLocators.PAYPAL_EXPRESS_BUTTON)