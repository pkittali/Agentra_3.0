import allure
import time
from pywinauto import Desktop
from pywinauto.timings import wait_until

from core.logger import get_logger

from resources.locators.desktop_locators import PrinterPrivacyLocators, PrinterSetupLocators, ShippingLocators

def wait_for_element(element, timeout=30):
    wait_until(timeout=timeout, retry_interval=1,

               func=lambda: element.exists() and element.is_enabled())

    return element



class ShippingPage:

    def __init__(self, main_window):
        self.main_window = main_window
        self.logger = get_logger(self.__class__.__name__)

    def click_add_shipping(self):
        self.logger.info("Attempting to click 'Add Shipping' button")

        try:
            with allure.step("Click 'Add Shipping'"):
                add_shipping_btn = self.main_window.child_window(**ShippingLocators.ADD_SHIPPING_BTN)
                add_shipping_btn.wait('enabled', timeout=30)
                add_shipping_btn.click_input()
        except Exception as e:
            self.logger.error(f"Failed to click 'Add Shipping'. Error: {e}")
            
    

    def fill_shipping_details(self, address, city, state, zip_code, phone):
        self.logger.info("Attempting to fill shipping details")

        try:
            with allure.step("Fill Shipping Details"):

                # ---- Street ----
                street = self.window.child_window(**ShippingLocators.STREET_BOX)
                wait_for_element(street).set_edit_text("")
                street.type_keys(address, with_spaces=True)
                self.logger.info(f"Entered Street: {address}")

                # ---- City ----
                city_box = self.window.child_window(**ShippingLocators.CITY_BOX)
                wait_for_element(city_box).set_edit_text("")
                city_box.type_keys(city, with_spaces=True)
                self.logger.info(f"Entered City: {city}")

                # ---- State Dropdown ----
                state_dd = self.window.child_window(**ShippingLocators.STATE_DROPDOWN)
                wait_for_element(state_dd).click_input()

               

                state_list = self.window.child_window(**ShippingLocators.STATE_LIST)
                wait_for_element(state_list)

                state_item = state_list.child_window(**ShippingLocators.STATE_ITEM)
                wait_for_element(state_item).click_input()
                self.logger.info(f"Selected State: {state}")

                # ---- ZIP Code ----
                zip_box = self.window.child_window(**ShippingLocators.ZIP_BOX)
                wait_for_element(zip_box).set_edit_text("")
                zip_box.type_keys(zip_code, with_spaces=True)
                self.logger.info(f"Entered ZIP: {zip_code}")

                # ---- Phone ----
                phone_box = self.window.child_window(**ShippingLocators.PHONE_BOX)
                wait_for_element(phone_box).set_edit_text("")
                phone_box.type_keys(phone, with_spaces=True)
                self.logger.info(f"Entered Phone: {phone}")

                # ---- Save Button ----
                save_btn = self.window.child_window(**ShippingLocators.SAVE_BTN)
                save_btn.wait('enabled', timeout=30)
                save_btn.click_input()
                self.logger.info("Shipping details saved successfully.")


        except Exception as e:
            self.logger.error(f"Failed to fill shipping details. Error: {e}")
           