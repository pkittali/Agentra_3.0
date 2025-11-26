# apps/hp_app_desktop.py
from pages.desktop import *
from pages.desktop.login_page import LoginPage
from core.configManager import ConfigManager
from pywinauto.application import Application
from pages.desktop.launchapp_page import LaunchAppPage

class HPAppDesktop:
    def __init__(self, main_window):
        app = Application(backend="uia").connect(title="HP Smart")
        self.main_window =app.window(title_re="HP Smart")
        self.login_page = LoginPage(main_window)
        self.launchapp_page = LaunchAppPage(main_window)

        # self.enroll_page = WebEnrollPage(driver)

    def login(self, email, password):
        self.login_page.open_user_profile()
        self.login_page.sign_in(email,password)
    
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
