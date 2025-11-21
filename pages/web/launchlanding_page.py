import time
import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import LandingPageLocators, LoginPageLocators
from core.logger import get_logger

class LaunchLandingPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def open(self):
        self.logger.info("Navigating to HP Portal Login URL")
        with allure.step("Launch HP Portal"):
            self.driver.get("https://instantink-stage1.hpconnectedstage.com/us/en/l/v2")
            # self.driver.maximize_window()

    def click_accept(self):
        self.logger.info("Navigating to HP Portal Login URL")
        with allure.step("Clicked I Accept "):
            self.click(*LandingPageLocators.ACCEPT_BUTTON)

    def click_signup_now(self):
        self.logger.info("Navigating to HP Portal Login URL")
        with allure.step("Clicked Sign up now"):
            self.click(*LandingPageLocators.SIGN_UP_NOW_BUTTON)


    

