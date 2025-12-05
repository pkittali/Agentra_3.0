# pages/desktop/login_page.py
import time
from pages.base_page import BasePage
from core.logger import get_logger
from resources.locators.desktop_locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver, main_window):
        # driver is DesktopDriverManager, main_window is driver.main_window
        super().__init__(driver)
        self.driver = driver
        self.main_window = main_window
        self.logger = get_logger(self.__class__.__name__)

    def open(self):
        self.main_window.wait("visible ready", timeout=20)
        self.main_window.set_focus()
        time.sleep(0.5)

    def click_manage_account(self):
        self.click(LoginPageLocators.MANAGE_HP_ACCOUNT_BTN)
