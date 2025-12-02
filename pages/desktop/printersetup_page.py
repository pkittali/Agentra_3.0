import allure
import time
from pywinauto import Desktop
from pywinauto.timings import wait_until

from core.logger import get_logger

from resources.locators.desktop_locators import PrinterSetupLocators



class PrinterSetupPage:

    def __init__(self, main_window):
        self.main_window = main_window
        self.logger = get_logger(self.__class__.__name__)

   
    def click_add_printer(self):
        """
        Clicks the 'Add Printer' button on Home screen.
        """
        self.logger.info("Attempting to click 'Add Printer' button")

        try:
            with allure.step("Click 'Add Printer'"):
                add_printer_btn = self.main_window.child_window(**PrinterSetupLocators.ADD_PRINTER_BTN)
                add_printer_btn.wait('enabled', timeout=20)
                add_printer_btn.click_input()
                

            self.logger.info("'Add Printer' button clicked successfully")

            
        except Exception as e:
            self.logger.error(f"Failed to click 'Add Printer'. Error: {e}")
            raise e

    
    def select_printer_from_list(self,printer_name):
        """
        Selects target printer from the beaconing printers list.
        """
        self.logger.info(f"Selecting printer: {printer_name}")

        try:
            with allure.step(f"Select printer '{printer_name}'"):

                beaconing_list = self.main_window.child_window(**PrinterSetupLocators.BEACONING_LIST)

                printer_item = beaconing_list.child_window(
                    title_re=f"DEVICEVIEWMODEL:{printer_name}",
                    control_type="ListItem"
                )

                printer_item.wait('enabled', timeout=30)
                printer_item.click_input()

            self.logger.info(f"Printer '{printer_name}' selected successfully")

            

        except Exception as e:
            self.logger.error(f"Failed to select printer '{printer_name}'. Error: {e}")
            raise e

    def connect_printer_to_wifi(self):
        """
        Completes the Wi-Fi setup for the selected printer.
        """
        self.logger.info("Starting printer Wi-Fi connection process")

        try:
            # Step 1: Click Continue (Time to connect)
            with allure.step("Click 'Continue' to start Wi-Fi setup"):
                continue_btn = self.main_window.child_window(**PrinterSetupLocators.CONTINUE_BTN)
                continue_btn.wait('enabled', timeout=30)
                continue_btn.click_input()


            # Step 2: Wi-Fi access dialog
            wifi_dialog = self.app.window(title="HP Smart")
            wifi_dialog.set_focus()

            with allure.step("Click 'Continue' in Wi-Fi Access Permission dialog"):
                wifi_continue_btn = wifi_dialog.child_window(**PrinterSetupLocators.WIFI_CONTINUE_BTN)
                wifi_continue_btn.wait('enabled', timeout=30)
                wifi_continue_btn.click_input()

            

            # Step 3: Wait for connection progress
            self.logger.info("Waiting for printer to finish connecting to Wi-Fi...")

            def is_wifi_setup_done():
                try:
                    btn = wifi_dialog.child_window(**PrinterSetupLocators.CONTINUE_BTN)
                    return btn.exists() and btn.is_enabled()
                except:
                    return False

            wait_until(timeout=360, retry_interval=2, func=is_wifi_setup_done)

            # Step 4: Final Continue
            with allure.step("Click final 'Continue' after Wi-Fi connection"):
                final_continue_btn = wifi_dialog.child_window(**PrinterSetupLocators.CONTINUE_BTN)
                final_continue_btn.click_input()

            

            self.logger.info("Printer Wi-Fi setup completed!")

        except Exception as e:
            self.logger.error(f"Wi-Fi setup failed. Error: {e}")
            raise e
