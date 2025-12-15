# pages/web/login_page.py
import allure
from pages.base_page import BasePage
from resources.locators.web_locators import LoginPageLocators
from core.configManager import ConfigManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver  # web manager returns raw webdriver or manager

    def open(self):
        url = ConfigManager.get_url("login")
        self.driver.get(url)

    def enter_username(self, username):
        self.enter_text(("id", LoginPageLocators.USERNAME_INPUT[1]), username)

    def enter_password(self, pwd):
        self.enter_text(("id", LoginPageLocators.PASSWORD_INPUT[1]), pwd)

    def click_login(self):
        self.click(("xpath", LoginPageLocators.LOGIN_BUTTON[1]))


    def is_login_successful(self):
        with allure.step("Verify Login Success"):
            try:
                text = self.get_text(LoginPageLocators.SUCCESS_MESSAGE)

                if not text or text.strip() == "":
                    raise AssertionError("Success message element found but empty")

                allure.attach(
                    f"Success message detected: {text}",
                    name="Login Success",
                    attachment_type=allure.attachment_type.TEXT
                )
                return True

            except Exception as e:
                # screenshot
                try:
                    if hasattr(self.driver, "driver") and hasattr(self.driver.driver, "get_screenshot_as_png"):
                        screenshot = self.driver.driver.get_screenshot_as_png()
                        allure.attach(
                            screenshot,
                            name="Login Failure Screenshot",
                            attachment_type=allure.attachment_type.PNG
                        )
                except:
                    pass

                allure.attach(
                    f"Login verification failed: {str(e)}",
                    name="Login Failure Details",
                    attachment_type=allure.attachment_type.TEXT
                )

                raise AssertionError(f"Login failed: {str(e)}")
            


# import time
# import allure
# import pytest
# from pages.base_page import BasePage
# from utils.waits import WaitUtils
# from core.configManager import ConfigManager
# from selenium.webdriver.common.by import By
# from resources.locators.web_locators import LoginPageLocators
# from core.logger import get_logger

# class LoginPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#         self.logger = get_logger(self.__class__.__name__)
#         self.wait = WaitUtils(driver)

#     def open(self):
#         self.logger.info("Navigating to HP Portal Login URL")
#         with allure.step("Launch HP Portal"):
#             url = ConfigManager.get_url("login")
#             self.driver.get(url)
            
#     def enter_username(self, username):
#         self.logger.info("Entering username into input field")        
#         with allure.step("Enter username"):
#             self.enter_text(*LoginPageLocators.USERNAME_INPUT, username)

#     def enter_password(self, password):
#         self.logger.info("Entering password into input field")
#         with allure.step("Enter password"):
#             self.enter_text(*LoginPageLocators.PASSWORD_INPUT, password)

#     def click_login(self):
#         self.logger.info("Clicking Login button")
#         with allure.step("Click Login button"):
#             self.click(*LoginPageLocators.LOGIN_BUTTON)

#     def is_login_successful(self):
#         self.logger.info("Checking if login was successful")
#         with allure.step("Check if login was successful"):
#             return self.driver.find_element(*LoginPageLocators.SUCCESS_MESSAGE).is_displayed()