# apps/hp_mobile_app.py
from pages.mobile.login_page import MobileLoginPage

class HPAppMobile:
    def __init__(self, mobile_driver):
        # mobile_driver is appium webdriver
        self.driver = mobile_driver
        self.login_page = MobileLoginPage(self.driver)

    def login(self, user_locator, pw_locator, username, password):
        self.login_page.enter_username(user_locator, username)
        self.login_page.enter_password(pw_locator, password)
        self.login_page.click_login(("id", "login_button"))  # example
