import random
import string
import time
import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import CreateAccountPageLocators, LoginPageLocators
from core.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class CreateAccountPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)
    
    # def generate_random_string(length=8):
    #     chars = string.ascii_lowercase
    #     return ''.join(random.choices(chars, k=length))

    def click_create_account(self):
        self.logger.info("Navigating to create account page")
        with allure.step("Clicked Create Account"):
            self.click(*CreateAccountPageLocators.CREATE_ACCOUNT_BUTTON)

    def enter_first_name(self, first_name="John"):
        self.logger.info("Entering first name into input field")
        with allure.step("Entered First Name"):
            self.enter_text(*CreateAccountPageLocators.FIRST_NAME_INPUT, first_name)
    
    def enter_last_name(self, last_name="Doe"):
        self.logger.info("Entering last name into input field")
        with allure.step("Entered Last Name"):
            self.enter_text(*CreateAccountPageLocators.LAST_NAME_INPUT, last_name)

    # test_email = f"GS{generate_random_string(8)}7@mailsac.com"
    # test_password = f"GS{test_email}@123"

    def enter_create_email(self, test_email):
        self.logger.info("Entering email into input field")
        with allure.step("Entered Email"):
            self.enter_text(*CreateAccountPageLocators.EMAIL_INPUT, test_email)

    def enter_create_password(self, test_password):
        self.logger.info("Entering password into input field")
        with allure.step("Entered Password"):
            self.enter_text(*CreateAccountPageLocators.PASSWORD_INPUT, test_password)

    def click_submit_create_account(self):
        self.logger.info("Clicking Submit Create Account button")
        with allure.step("Clicked Submit Create Account button"):
            self.click(*CreateAccountPageLocators.SUBMIT_CREATE_ACCOUNT)

    def fetch_and_enter_otp(self,test_email):
        self.logger.info("Opening email to fetch verification code")
        with allure.step("Opened Email"):
            inbox_url = f"https://mailsac.com/inbox/{test_email}"
            # Open a new tab for Mailsac
            self.driver.execute_script("window.open('');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.get(inbox_url)
            wait = WebDriverWait(self.driver, 15)
            # Poll for email for up to 90 seconds
            email_found = False
            start_time = time.time()
            while time.time() - start_time < 120:
                try:
                    messages = self.driver.find_elements(By.CSS_SELECTOR, "tr.ng-scope")
                    if messages:
                        email_found = True
                        break
                except:
                    pass
                print("[DEBUG] No email yet, refreshing inbox...")
                self.driver.refresh()
                time.sleep(5)
            if not email_found:
                raise TimeoutError(f"No OTP email received at {test_email} within 90 seconds.")
            messages[0].click()
            try:
                wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                email_body = self.driver.find_element(By.TAG_NAME, "body").text
            except:
                raise TimeoutError("Email body did not load in time.")
            # Extract OTP from email body
            otp_match = re.search(r'\b(\d{6})\b', email_body)
            assert otp_match, f"No OTP found in email body: {email_body}"
            otp = otp_match.group(1)
            print(f"[DEBUG] OTP Found: {otp}")
            # Switch back to the original application tab
            self.driver.switch_to.window(self.driver.window_handles[0])





    

   

