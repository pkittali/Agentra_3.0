# apps/hp_app_web.py
import random
import string
from pages.web import *
from pages.web.billing_page import BillingPage
from pages.web.billinginformation_page import BillingInformationPage
from pages.web.hpcheckout_page import HPCheckoutPage
from pages.web.launchlanding_page import LaunchLandingPage
from pages.web.login_page import LoginPage
from pages.web.createaccount_page import CreateAccountPage
from pages.web.onboard_printer_page import OnboardPrinterPage
from pages.web.plan_selection_page import PlanSelectionPage
from pages.web.printer_select_page import PrinterSelectionPage
from pages.web.shipping_billing_page import ShippingBillingPage
from pages.web.shippingpage import ShippingPage
from pages.web.special_offers_page import SpecialOffersPage

class HPAppWeb:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.login_page = LoginPage(driver, config)
        self.create_account_page = CreateAccountPage(driver)
        self.landing_page=LaunchLandingPage(driver)
        self.onboard_printer_page=OnboardPrinterPage(driver)
        self.printer_select_page=PrinterSelectionPage(driver)
        self.plan_select_page=PlanSelectionPage(driver)
        self.hp_checkout_page=HPCheckoutPage(driver)
        self.shipping_billing_page=ShippingBillingPage(driver,config)
        self.shippingpage=ShippingPage(driver)
        self.billinginformation_page=BillingInformationPage(driver)
        self.billing_page=BillingPage(driver)
        self.special_offers_page=SpecialOffersPage(driver)
        

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

    def onboard_printer(self):
        # "link_printer_url": "https://www.hpsmartstage.com/us/en/newprinter"
        url="https://www.hpsmartstage.com/us/en/newprinter"
        claim_code="ABCDEFGH"
        self.onboard_printer_page.open_printer_url(url)
        self.onboard_printer_page.enter_claim_code(claim_code)
        self.onboard_printer_page.click_add_printer()

    def checkout_upto_shipping_billing(self):
        # self.landing_page.click_signup_now()
        # self.printer_select_page.printer_selection()
        self.plan_select_page.plan_selection()
        # self.hp_checkout_page.click_hp_checkout()
        
    def start_enrollment(self):
        self.login_page.open()
        self.login_page.login()
    
    def enter_shipping_details(self):
        self.shipping_billing_page.click_add_shipping()
        self.shippingpage.fill_shipping("9898989898","1234 Sunset Blvd","Los Angeles","California","90026","False")
        self.shippingpage.click_save_shipping()
        self.shippingpage.click_ship_to_this_address()

    def enter_billing_details(self):
        self.shipping_billing_page.click_add_billing()
        self.billinginformation_page.click_continue()
        self.billing_page.fill_billing_details("5555555555554444","12","2028","123")
        self.billing_page.click_save_billing()

    def apply_promo_code(self):
        self.shipping_billing_page.click_apply_promotion()
        self.special_offers_page.enter_promo_code("PROMO123")
        self.special_offers_page.click_apply_promo()

    
    