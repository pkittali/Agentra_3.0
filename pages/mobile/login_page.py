# pages/mobile/login_page.py
from pages.base_page import BasePage

class MobileLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        # for app-based flow maybe ensure app is in foreground
        pass

    def enter_username(self, locator, username):
        self.enter_text(locator, username)

    def enter_password(self, locator, pwd):
        self.enter_text(locator, pwd)

    def click_login(self, locator):
        self.click(locator)
