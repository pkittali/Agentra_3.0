import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import BillingInformationPageLocators
from core.logger import get_logger

class BillingInformationPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def click_continue(self):
        self.logger.info("Clicking Continue button")
        with allure.step("Clicked Continue button"):
            self.click(*BillingInformationPageLocators.CONTINUE_BUTTON) 