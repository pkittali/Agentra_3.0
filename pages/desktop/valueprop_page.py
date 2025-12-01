
import allure
import time
from pywinauto import Desktop
from pywinauto.timings import wait_until

from core.logger import get_logger

from resources.locators.desktop_locators import  ValuePropLocators



class ValuePropPage:

    def __init__(self, main_window):
        self.main_window = main_window
        self.logger = get_logger(self.__class__.__name__)

    def click_next_button(self):
        
        self.logger.info("Attempting to click 'Next' button")
    
        try:

            with allure.step("Click 'Next'"):
    
                # Locate the button

                next_btn = self.main_window.child_window(**ValuePropLocators.NEXT_BTN)
                next_btn.wait('enabled', timeout=180)
                next_btn.click_input()

        except Exception as e:

            self.logger.error(f"Failed to click 'Next' button. Error: {e}")
    
          

    