import logging
import re
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.waits import WaitUtils
from resources.locators.web_locators import SpecialOffersLocators


logger = logging.getLogger(__name__)


class SpecialOffersPage(BasePage):
    """
    Cleaned Page Object for Special Offers / Promo code area.
    - No assertions here (tests should assert)
    - All interactions wrapped in allure.step
    - High-level flows provided (apply_promo_code)
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WaitUtils(driver)

    # -------------------------
    # Visibility / basic getters
    # -------------------------


    # -------------------------
    # Promo entry actions
    # -------------------------
    def open_enter_promo_prompt(self):
        with allure.step("Open 'Enter promo or PIN code' prompt"):
            self.click(SpecialOffersLocators.SPECIAL_OFFERS_ENTER_PROMOCODE)

    def enter_promo_code(self, code):
        """Use `enter_text_2` if input inside shadow/iframe needs special handling, else use enter_text."""
        with allure.step(f"Enter promo code: {code}"):
            try:
                # prefer helper that handles tricky inputs; fallback to base enter_text if not available
                self.enter_text(self.driver, SpecialOffersLocators.INPUT_FIELD, code)
            except Exception:
                self.enter_text(*SpecialOffersLocators.INPUT_FIELD, code)

    def click_apply(self):
        with allure.step("Click Apply promo button"):
            self.click(SpecialOffersLocators.APPLY_BUTTON)
    
    def click_close_modal(self):
        with allure.step("Close special offers modal"):
            self.click(SpecialOffersLocators.CLOSE_SOB_MODAL)

    # -------------------------
    # High-level flows
    # -------------------------
    # -------------------------
    # Message / state checks (no asserts)
    # -------------------------
    def get_apply_success_msg(self):
        with allure.step("Get success/promo message text"):
            return self.get_text(SpecialOffersLocators.SPECIAL_OFFERS_MESSAGE)
        
    # @allure.step("Apply promo code")
    # def apply_promo_code(self, code, wait_for_toast=True, timeout=20):
    #     """
    #     High-level action to apply a promo code and optionally wait for result toast/message.
    #     Returns the toast/message text when wait_for_toast=True.
    #     """
    #     self.open_enter_promo_prompt()
    #     self.enter_promo_code(code)
    #     self.click_apply()
    #     self.get_apply_success_msg()
    #     self.click_close_modal()

    #     if wait_for_toast:
    #         msg = WebDriverWait(self.driver, timeout).until(
    #             EC.visibility_of_element_located(SpecialOffersLocators.SPECIAL_OFFERS_MESSAGE)
    #         )
    #         return msg.text
    #     return None

