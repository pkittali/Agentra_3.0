import time
import allure
from pages.base_page import BasePage
from resources.locators.web_locators import CreateAccountPageLocators
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.logger import get_logger
import re

class CreateAccountPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

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

    def enter_verification_code(self,otp):
        self.logger.info("Entering verification code")
        with allure.step("Entered Verification code"):
            self.enter_text(*CreateAccountPageLocators.VERIFICATION_CODE_INPUT,otp)
    
    def click_verify(self):
        self.logger.info("Clicking Verify button")
        with allure.step("Clicked Verify button"):
            self.click(*CreateAccountPageLocators.VERIFY_BUTTON)

    def fetch_and_enter_otp(self, test_email):
        self.logger.info("Opening email to fetch verification code")
        with allure.step("Opened Email"):
            inbox_url = f"https://mailsac.com/inbox/{test_email}"
            # Open a new tab for Mailsac
            self.driver.driver.execute_script("window.open('');")
            self.driver.driver.switch_to.window(self.driver.driver.window_handles[-1])
            self.driver.driver.get(inbox_url)
            wait = WebDriverWait(self.driver.driver, 15)

            # Poll for email for up to 120 seconds
            email_found = False
            start_time = time.time()

            while time.time() - start_time < 120:
                try:
                    messages = self.driver.driver.find_elements(By.CSS_SELECTOR, "tr.ng-scope")
                    if messages:
                        email_found = True
                        break
                except:
                    pass

                print("[DEBUG] No email yet, refreshing inbox...")
                self.driver.driver.refresh()
                time.sleep(5)

            if not email_found:
                raise TimeoutError(f"No OTP email received at {test_email} within 120 seconds.")

            # Open latest email
            messages[0].click()

            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            email_body = self.driver.driver.find_element(By.TAG_NAME, "body").text

            # Extract OTP (6 digits)
            otp_match = re.search(r'\b(\d{6})\b', email_body)
            assert otp_match, f"No OTP found in email body: {email_body}"

            otp = otp_match.group(1)
            print(f"[DEBUG] OTP Found: {otp}")
            # Switch back to main tab
            self.driver.driver.switch_to.window(self.driver.driver.window_handles[0])
            self.enter_verification_code(otp)
            self.click_verify()