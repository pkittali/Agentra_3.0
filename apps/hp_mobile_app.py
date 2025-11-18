# apps/hp_app_mobile.py
from pages.mobile import *

class HPAppMobile:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = MobileLoginPage(driver)
        self.permissions_page = PermissionsPage(driver)
        self.enroll_page = MobileEnrollPage(driver)
    
    def start_enrollment(self):
        self.login_page.open()
        self.login_page.login()
        if self.permissions_page.is_displayed():
            self.permissions_page.allow_permissions()
    
    def enter_shipping_details(self):
        self.enroll_page.fill_shipping()
    
    def confirm_enrollment(self):
        self.enroll_page.confirm()
    
    def verify_confirmation_screen(self):
        self.enroll_page.verify_success_message()
