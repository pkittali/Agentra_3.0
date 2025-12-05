import random
import string
import time
import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import BillingInformationPageLocators, BillingPageLocators
from core.logger import get_logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains

class BillingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def enter_card_number(self, card_number):
        self.logger.info(f"Entering card number: {card_number}")
        with allure.step(f"Entered card number: {card_number}"):
            self.enter_text(*BillingPageLocators.CARD_NUMBER_INPUT, card_number)

    def select_expiry_date(self, month, year):
        self.logger.info(f"Selecting expiry date: {month}/{year}")
        with allure.step(f"Selected expiry date: {month}/{year}"):
            self.select_custom_dropdown_by_text(month)
            self.select_custom_dropdown_by_text(year)

    def enter_cvv(self, cvv):
        self.logger.info(f"Entering CVV: {cvv}")
        with allure.step(f"Entered CVV: {cvv}"):
            self.enter_text(*BillingPageLocators.CVV_INPUT, cvv)

    def click_save_billing(self):
        self.logger.info("Clicking Save Billing button")
        with allure.step("Clicked Save Billing button"):
            self.click(*BillingPageLocators.NEXT_BUTTON)

    #update for usage of allure and logger
    # def fill_billing_details(self):
    #     test_card_number = "4111111111111111"
    #     test_expiry_month = "12"
    #     test_expiry_year = "2025"
    #     test_cvv = "123"

    #     self.enter_card_number(test_card_number)
    #     self.select_expiry_date(test_expiry_month, test_expiry_year)
    #     self.enter_cvv(test_cvv)

    def fill_billing_details(self,test_card_number,test_expiry_month,test_expiry_year,test_cvv):
        self.logger.info("Filling billing details")
        with allure.step("Filling billing details"):
            self.enter_card_number(test_card_number)
            self.select_expiry_date(test_expiry_month, test_expiry_year)
            self.enter_cvv(test_cvv)
            self.click_save_billing()