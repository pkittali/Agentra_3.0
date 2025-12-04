import random
import string
import time
import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import AddShippingPageLocators, HPCheckoutPageLocators
from core.logger import get_logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains

class ShippingPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def enter_first_name(self,first_name):
        self.logger.info("Entering First Name")
        with allure.step("Entered FIrst Name"):
            self.enter_text(*AddShippingPageLocators.FIRST_NAME_INPUT,first_name) 

    def enter_last_name(self,last_name):
        self.logger.info("Entering last Name")
        with allure.step("Entered last Name"):
            self.enter_text(*AddShippingPageLocators.LAST_NAME_INPUT,last_name)

    def enter_company_name(self,company_name):
        self.logger.info("Entering Company Name")
        with allure.step("Entered Company Name"):
            self.enter_text(*AddShippingPageLocators.COMPANY_INPUT,company_name)

    def enter_mobile_number(self,mobile_number):
        self.logger.info("Entering Mobile Number")
        with allure.step("Entered Mobile Number"):
            self.enter_text(*AddShippingPageLocators.MOBILE_NUMBER_INPUT,mobile_number)

    def enter_street1(self,street1):
        self.logger.info("Entering Street1")
        with allure.step("Entered Street1"):
            self.enter_text(*AddShippingPageLocators.STREET1_INPUT,street1)

    def enter_street2(self,street2):
        self.logger.info("Entering Street2")
        with allure.step("Entered Street2"):
            self.enter_text(*AddShippingPageLocators.STREET2_INPUT,street2)

    def enter_city(self,city):
        self.logger.info("Entering City")
        with allure.step("Entered City"):
            self.enter_text(*AddShippingPageLocators.CITY_INPUT,city)

    def select_state(self,state):
        self.logger.info("Selecting State")
        with allure.step("Selected State"):
            self.click(*AddShippingPageLocators.STATE_COMBOBOX_OPEN)
            self.select_custom_dropdown_by_text(state)

    def enter_zipcode(self,zipcode):
        self.logger.info("Entering Zipcode")
        with allure.step("Entered Zipcode"):
            self.enter_text(*AddShippingPageLocators.ZIP_CODE_INPUT,zipcode)

    def click_save_shipping(self):
        self.logger.info("Clicking Save Shipping button")
        with allure.step("Clicked Save Shipping button"):
            self.click(*AddShippingPageLocators.SAVE_BUTTON)

    def check_text_message_option(self):
        self.logger.info("Checking Text Message Option")
        with allure.step("Checked Text Message Option"):
            self.click(*AddShippingPageLocators.TEXT_MESSAGE_OPTION_CHECKBOX)


    def fill_shipping(self,mobile_number,street1,city,state_name,zip_code,text_message_optin=False):
        self.enter_street1(street1)
        self.enter_city(city)
        self.select_state(state_name)
        self.enter_zipcode(zip_code)
        self.enter_mobile_number(mobile_number)
        if text_message_optin:
            self.check_text_message_option()
        self.click_save_shipping()
    
    def click_ship_to_this_address_if_visible(self):
        self.logger.info("Clicking Ship to this address button")
        with allure.step("Clicked Ship to this address button"):
            try:
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='dialog']")))
                self.wait.wait_until_visible(*AddShippingPageLocators.SHIP_TO_THIS_ADDRESS_BUTTON,timeout=20)
                self.wait.wait_until_clickable(*AddShippingPageLocators.SHIP_TO_THIS_ADDRESS_BUTTON,timeout=20)
                if element:
                    self.click(*AddShippingPageLocators.SHIP_TO_THIS_ADDRESS_BUTTON)
            except TimeoutException:
                self.logger.info("Ship to this address button not visible, proceeding without clicking it.")
                pass

    