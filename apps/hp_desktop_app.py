# apps/hp_app_web.py
from pages.desktop import *
from pages.desktop.login_page import LoginPage

class HPAppDesktop:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.login_page = LoginPage(driver, config)
        
        # self.enroll_page = WebEnrollPage(driver)

    def login(self, username, password):
        self.login_page.open()
        self.login_page.login()
    
    def start_enrollment(self):
        self.login_page.open()
        self.login_page.login()
    
    def enter_shipping_details(self):
        self.enroll_page.fill_shipping()
    
    def confirm_enrollment(self):
        self.enroll_page.confirm()
    
    def verify_confirmation_screen(self):
        self.enroll_page.verify_success_message()
