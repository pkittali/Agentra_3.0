# apps/hp_app_web.py
from pages.desktop import *
from pages.desktop.billing_page import BillingPage
from pages.desktop.login_page import LoginPage
from pages.desktop.createaccount_page import CreateAccountPage
from pages.desktop.launchapp_page import LaunchAppPage
from pywinauto.application import Application

from pages.desktop.printerprivacy_page import PrinterPrivacyPage
from pages.desktop.printersetup_page import PrinterSetupPage
from pages.desktop.shipping_page import ShippingPage
from pages.desktop.valueprop_page import ValuePropPage


class HPAppDesktop:
    def __init__(self, main_window):
        app = Application(backend="uia").connect(title="HP Smart")
        self.main_window =app.window(title="HP Smart")
        
        self.login_page = LoginPage(main_window)
        self.launchapp_page = LaunchAppPage(main_window)
        self.createaccount_page= CreateAccountPage(main_window)
        self.printer_setup_page = PrinterSetupPage(main_window)
        self.printer_privacy_page = PrinterPrivacyPage(main_window)
        self.value_prop_page = ValuePropPage(main_window)
        self.shipping_page = ShippingPage(main_window)
        self.billing_page = BillingPage(main_window)
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

    def launch_app(self):
        self.launchapp_page.launchapp()

    def create_account(self):
        print("calling create account")
        self.createaccount_page.open_manage_account()
        self.createaccount_page.click_create_account()
        self.createaccount_page.wait_for_chrome_window()
        self.createaccount_page.create_account()
        self.createaccount_page.return_to_hp_smart()

    def printer_setup(self, printer_name):
        self.printer_setup_page.click_add_printer()
        self.printer_setup_page.select_printer_from_list(printer_name)
        self.printer_setup_page.connect_printer_to_wifi()

    def printer_privacy(self):
        self.printer_privacy_page.accept_printer_privacy()

    def value_prop(self):
        self.value_prop_page.click_next_button()

    def shipping(self, address, city, state, zip_code, phone):
        self.shipping_page.click_add_shipping()
        self.shipping_page.fill_shipping_details(address, city, state, zip_code, phone)

    def billing(self, card_number, exp_month, exp_year, cvv):
        self.billing_page.click_add_billing()
        self.billing_page.fill_billing_details(card_number, exp_month, exp_year, cvv)

    

