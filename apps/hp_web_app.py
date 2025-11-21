# apps/hp_app_web.py
import random
import string
from pages.web import *
from pages.web.launchlanding_page import LaunchLandingPage
from pages.web.login_page import LoginPage
from pages.web.createaccount_page import CreateAccountPage

class HPAppWeb:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.create_account_page = CreateAccountPage(driver)
        self.landing_page=LaunchLandingPage(driver)
        #self.enroll_page = WebEnrollPage(driver)

    def login(self, username, password):
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login()
        assert self.login_page.is_login_successful(), "Login unsuccessful"

    def launch_web(self):
        self.landing_page.open()
        self.landing_page.click_accept()
        self.landing_page.click_signup_now()

    def generate_random_string(self,length=8):
        chars = string.ascii_lowercase
        return ''.join(random.choices(chars, k=length))

    def create_account(self):
        test_email = f"GS{self.generate_random_string(8)}7@mailsac.com"
        test_password = f"GS{test_email}@123"
        self.create_account_page.click_create_account()
        self.create_account_page.enter_first_name()
        self.create_account_page.enter_last_name()
        self.create_account_page.enter_create_email(test_email)
        self.create_account_page.enter_create_password(test_password)
        self.create_account_page.click_submit_create_account()
        self.create_account_page.fetch_and_enter_otp(test_email)

    def start_enrollment(self):
        self.login_page.open()
        self.login_page.login()
    
    def enter_shipping_details(self):
        self.enroll_page.fill_shipping()
    
    def confirm_enrollment(self):
        self.enroll_page.confirm()
    
    def verify_confirmation_screen(self):
        self.enroll_page.verify_succes