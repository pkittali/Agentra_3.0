import allure
import time
from pywinauto import Desktop
from pywinauto.timings import wait_until

from core.logger import get_logger

from resources.locators.desktop_locators import BillingLocators

def wait_for_element(element, timeout=30):
    wait_until(timeout=timeout, retry_interval=1,

               func=lambda: element.exists() and element.is_enabled())

    return element



class BillingPage:

    def __init__(self, main_window):
        self.main_window = main_window
        self.logger = get_logger(self.__class__.__name__)

    def click_add_billing(self):
        self.logger.info("Attempting to click 'Add Billing' button")

        try:
            with allure.step("Click 'Add Billing'"):
                add_billing_btn = self.main_window.child_window(**BillingLocators.ADD_BILLING_BTN)
                add_billing_btn.wait('enabled', timeout=30)
                add_billing_btn.click_input()

        except Exception as e:
            self.logger.error(f"Failed to click 'Add Billing'. Error: {e}")
            
    

    def fill_billing_details(self, card_number, exp_month, exp_year, cvv):
        self.logger.info("Attempting to fill billing details")

        try:
            with allure.step("Fill Billing Details"):

                # ---- Card Number ----
                card_field = self.window.child_window(**BillingLocators.CARD_NUMBER_FIELD)
                wait_for_element(card_field).set_edit_text("")
                card_field.type_keys(card_number, with_spaces=True)
                self.logger.info(f"Entered Card Number: {card_number}")

                # ---- Expiration Month Dropdown ----
                month_dd = self.window.child_window(**BillingLocators.EXP_MONTH_DROPDOWN)
                wait_for_element(month_dd).click_input()

                month_list = self.window.child_window(**BillingLocators.EXP_MONTH_LIST)
                wait_for_element(month_list)

                month_item = month_list.child_window(**BillingLocators.EXP_MONTH_ITEM(exp_month))
                wait_for_element(month_item).click_input()
                self.logger.info(f"Selected Expiration Month: {exp_month}")

                ## ---- Expiration Month ----
                exp_month = self.main_window.child_window(**BillingLocators.EXP_MONTH_DROPDOWN)
                wait_for_element(exp_month, timeout=15)
                exp_month.select(exp_month)
                self.logger.info("Selected expiration month")

                # ---- Expiration Year ----
                exp_year = self.main_window.child_window(**BillingLocators.EXP_YEAR_DROPDOWN)
                wait_for_element(exp_year, timeout=15)
                exp_year.select(exp_year)
                self.logger.info("Selected expiration year")

                # ---- CVV ----
                cvv_field = self.window.child_window(**BillingLocators.CVV_FIELD)
                wait_for_element(cvv_field).set_edit_text("")
                cvv_field.type_keys(cvv, with_spaces=True)
                self.logger.info(f"Entered CVV: {cvv}")

                # ---- Save / Next Button ----
                save_btn = self.main_window.child_window(**BillingLocators.SAVE_BTN)
                save_btn.wait('enabled', timeout=30)
                save_btn.click_input()
                self.logger.info("Billing details saved successfully.")

        except Exception as e:
            self.logger.error(f"Failed to fill billing details. Error: {e}")
