import time
import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import LoginPageLocators
from core.logger import get_logger

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def click_login(self):
        self.logger.info("Clicking Login button")
        with allure.step("Clicked Login button"):
            self.click(*LoginPageLocators.LOGIN_BUTTON)

    def is_login_successful(self):
        self.logger.info("Checking if login was successful")
        with allure.step("Check if login was successful"):
            return self.driver.find_element(*LoginPageLocators.SUCCESS_MESSAGE).is_displayed()

