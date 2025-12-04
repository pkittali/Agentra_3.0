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

    def validate_require_billing_message_text(self):
        self.logger.info("Getting 'Require Billing Information' message text")
        with allure.step("Fetched 'Require Billing Information' message text"):
            assert "A payment method is needed on file to enroll" in self.get_text(*SpecialOffersPageLocators.REQUIRE_BILLING_TEXT)
        
    def validate_enrollment_key_label(self):
        self.logger.info("Getting 'Enrollment Key' label text")
        with allure.step("Fetched 'Enrollment Key' label text"):
            assert "Enrollment Key" in self.get_text(*SpecialOffersPageLocators.ENROLLMENT_KEY_LABEL)
        
    def validate_enrollment_key_verifymonths_text(self):
        self.logger.info("Getting 'Verify Months' text for Enrollment Key")
        with allure.step("Fetched 'Verify Months' text for Enrollment Key"):
            assert "1 month" in self.get_text(*SpecialOffersPageLocators.ENROLLMENT_KEY_MONTHS_TEXT)
        
    def enter_promo_code(self, promo_code):
        self.logger.info("Entering promo code")
        with allure.step("Entered promo code"):
            self.enter_text(*SpecialOffersPageLocators.SPECIAL_OFFERS_ENTRY_BOX, promo_code)

    def click_apply_promo(self):
        self.logger.info("Clicking Apply Promo button")
        with allure.step("Clicked Apply Promo button"):
            self.click(*SpecialOffersPageLocators.SPECIAL_OFFERS_APPLY_BUTTON)

    def is_apply_enabled(self):
        self.logger.info("Checking if Apply button is enabled")
        with allure.step("Checked Apply button state"):
            assert self.wait.wait_until_clickable(*SpecialOffersPageLocators.SPECIAL_OFFERS_APPLY_BUTTON),"Apply button is not enabled after entering code"
    
    def is_promotion_text_visible(self):
        self.logger.info("Checking if promotion message is visible")
        with allure.step("Checked promotion message visibility"):
            return self.wait.wait_until_visible(*SpecialOffersPageLocators.PROMOTION_TEXT)
        
    def click_close_modal(self):
        self.logger.info("Clicking Close Modal button")
        with allure.step("Clicked Close Modal button"):
            self.click(*SpecialOffersPageLocators.CLOSE_SOB_MODAL)
        
    def apply_and_validate_promo(self,code):
        self.logger.info(f"Applying and validating promo code: {code}")
        with allure.step(f"Applied and validated promo code: {code}"):
            self.enter_promo_code(code)
            self.is_apply_enabled()
            self.click_apply_promo()
            time.sleep(2)  
            assert self.is_promotion_text_visible(), "Promotion message is not visible"
    
    def is_promotion_message_visible(self):
        self.logger.info("Checking if promotion message is visible")
        with allure.step("Checked promotion message visibility"):
            return self.wait.wait_until_visible(*SpecialOffersPageLocators.PROMOTION_ICON_MESSAGE)
        
    def get_promotion_message_text(self):
        self.logger.info("Getting promotion message text")
        with allure.step("Fetched promotion message text"):
            return self.get_text(*SpecialOffersPageLocators.PROMOTION_TEXT)
        
    def get_promo_code_text(self):
        self.logger.info("Getting promo code text from breakdown")
        with allure.step("Fetched promo code text from breakdown"):
            return self.get_text(*SpecialOffersPageLocators.PROMO_CODE_LABEL)
        
    def get_promo_code_months_text(self):
        self.logger.info("Getting promo code months text from breakdown")
        with allure.step("Fetched promo code months text from breakdown"):
            return self.get_text(*SpecialOffersPageLocators.PROMO_CODE_MONTHS_TEXT)
        
    def validate_multiple_codes(self,multiple_codes):
        # 4. Apply multiple promo codes one by one
        for idx, code in enumerate(multiple_codes, start=1):
            self.apply_and_validate_promo(code)

            if idx < len(multiple_codes):
                # Close SOB modal after every promo code except last
                self.click_close_modal()
            else:
                # For last promo code, validate combined messages before closing modal
                assert self.is_promotion_message_visible(), "Promotion message should be visible after applying codes"
                promo_message = self.get_promotion_message_text()
                assert "Promotion codes cannot be combined. If multiple codes are entered, the promotion with the best value is applied." in promo_message, \
                    f"Expected 'Promotion codes cannot be combined. If multiple codes are entered, the promotion with the best value is applied.' in promo message but got: {promo_message}"

                code_name = self.get_promo_code_text().lower()
                code_months = self.get_promo_code_months_text().lower()
                assert "promo code" in code_name, "Breakdown should show promotion details having promo code"
                assert "month" in code_months, "Breakdown should show promotion details having promo months"

                self.click_close_modal()

    


    