import allure
import time
from pywinauto import Desktop
from pywinauto.timings import wait_until

from core.logger import get_logger

from resources.locators.desktop_locators import BillingLocators, SobLocators

def wait_for_element(element, timeout=30):
    wait_until(timeout=timeout, retry_interval=1,

               func=lambda: element.exists() and element.is_enabled())

    return element



class SobPage:

    def __init__(self, main_window):
        self.main_window = main_window
        self.logger = get_logger(self.__class__.__name__)

    def apply_code(self, apply_code):
        """
        Apply promo code on the promo modal screen.
        """
        self.logger.info(f"Attempting to apply promo code: {apply_code}")

        try:
            with allure.step("Click 'Enter promo or PIN code'"):
                promo_btn = self.window.child_window(**SobLocators.PROMO_BTN)
                wait_for_element(promo_btn, timeout=30)
                promo_btn.click_input()
                self.logger.info("Clicked 'Enter promo or PIN code' button")

            with allure.step("Enter Promo Code"):
                promo_input = self.window.child_window(**SobLocators.PROMO_INPUT)
                wait_for_element(promo_input, timeout=20)
                promo_input.set_edit_text("")
                promo_input.type_keys(apply_code, with_spaces=True)
                self.logger.info(f"Entered promo code: {apply_code}")

            with allure.step("Click Apply Button"):
                apply_btn = self.window.child_window(**SobLocators.APPLY_BTN)
                wait_for_element(apply_btn, timeout=20)
                apply_btn.click_input()
                self.logger.info("Clicked 'Apply' button")

        except Exception as e:
            self.logger.error(f"Failed to apply promo code. Error: {e}")
