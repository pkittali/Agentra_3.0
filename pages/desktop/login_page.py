import time
import allure
import pytest
from core.logger import get_logger
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.desktop_locators import LoginPageLocators
from pywinauto.timings import wait_until
import pyautogui
from pywinauto import Desktop, Application, mouse
class LoginPage(BasePage):
    def __init__(self, main_window):
        self.main_window = main_window
        self.logger = get_logger(self.__class__.__name__)

    def wait_for_element(self,element, timeout=30):
        """Generic wait for Pywinauto element to exist and enabled."""

        wait_until(
            timeout=timeout,
            retry_interval=1,
            func=lambda: element.exists() and element.is_enabled(),
        )

        return element

    def open_user_profile(self):
        self.logger.info("Navigating to HP Portal Login URL")
        with allure.step("Launch HP Smart Desktop App"):
            # self.driver.get("https://practicetestautomation.com/practice-test-login/")
            # self.main_window.click(**LoginPageLocators.USER_PROFILE)
            self.main_window.child_window(**LoginPageLocators.USER_PROFILE).click_input()

    
    def sign_in(self,email,password):
        self.logger.info("Navigating to HP Portal Login URL")
        with allure.step("Launch HP Smart Desktop App"):
            # self.driver.get("https://practicetestautomation.com/practice-test-login/")
            self.main_window.child_window(**LoginPageLocators.SIGN_IN_BUTTON).click_input()
            # Step: Detect Chrome window and fill HP Account
            print("Waiting for Chrome window with HP Account page...")
            chrome_win = Desktop(backend="uia").window(title_re=".*Chrome.*")
            chrome_win.wait("exists ready", timeout=20)
            chrome_win.set_focus()
 
            try:
                print("Typing user details in HP Account form...")

                username =  chrome_win.window(**LoginPageLocators.WEB_USERNAME_INPUT)
                username.wait("ready", timeout=20)
                username.type_keys(email, with_spaces=True)
                self.wait_for_element( chrome_win.window(**LoginPageLocators.USE_PASSWORD_BUTTON), timeout=30).click_input()
                self.wait_for_element( chrome_win.window(**LoginPageLocators.WEB_PASSWORD_INPUT), timeout=30). type_keys(password, with_spaces=True)
                self.wait_for_element( chrome_win.window(**LoginPageLocators.WEB_SUBMIT_BUTTON), timeout=30).click_input()
                self.wait_for_element( chrome_win.window(**LoginPageLocators.OPEN_HP_SMART_BUTTON), timeout=30).click_input()
                print("Completed login + Open + switch to HP Smart successfully!")
            except Exception as e:
                pytest.fail(f"Failed to complete HP Smart login & open flow: {e}")

    def enter_username(self, username):
        self.logger.info("Entering username into input field")        
        with allure.step("Enter username"):
            self.driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.logger.info("Entering password into input field")
        with allure.step("Enter username"):
            self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.logger.info("Clicking Login button")
        with allure.step("Click Login button"):
            self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def is_login_successful(self):
        self.logger.info("Checking if login was successful")
        with allure.step("Check if login was successful"):
            return self.driver.find_element(*LoginPageLocators.SUCCESS_MESSAGE).is_displayed()

