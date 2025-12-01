import allure
import time
from pywinauto import Desktop
from pywinauto.timings import wait_until

from core.logger import get_logger

from resources.locators.desktop_locators import PrinterPrivacyLocators, PrinterSetupLocators



class PrinterPrivacyPage:

    def __init__(self, main_window):
        self.main_window = main_window
        self.logger = get_logger(self.__class__.__name__)

    def accept_printer_privacy(self):
        """
        Accept printer privacy on the HP Smart app.
        """
        self.logger.info("Attempting to accept printer privacy")

        try:
            # Bring privacy dialog to focus
            privacy_dialog = self.app.window(**PrinterPrivacyLocators.APP_TITLE)
            privacy_dialog.set_focus()

            with allure.step("Click 'Accept All' on Printer Privacy page"):
                privacy_accept_btn = privacy_dialog.child_window(**PrinterPrivacyLocators.PRIVACY_ACCEPT_BTN)
                privacy_accept_btn.wait('enabled', timeout=20)
                privacy_accept_btn.click_input()

            

            self.logger.info("Printer privacy accepted successfully")

        except Exception as e:
            self.logger.error(f"Failed to accept printer privacy. Error: {e}")
            raise e
