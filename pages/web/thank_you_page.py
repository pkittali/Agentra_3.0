import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import ThankYouPageLocators
from core.logger import get_logger

class ThankYouPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

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
