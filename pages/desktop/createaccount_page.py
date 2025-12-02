# import time
# import allure
# import pytest
# import random
# import string
# import re
# from datetime import datetime

# import pyautogui
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from pywinauto import Desktop, timings

# from core.logger import get_logger
# from resources.locators.desktop_locators import CreateAccountLocators


# class CreateAccountPage:

#     def __init__(self, main_window):
#         self.main_window = main_window
#         self.logger = get_logger(self.__class__.__name__)

#     def open_manage_account(self):
#         self.logger.info("Opening Manage HP Account section")

#         with allure.step("Open Manage HP Account"):
#             self.main_window.set_focus()
#             self.main_window.maximize()

#             btn = self.main_window.child_window(**CreateAccountLocators.MANAGE_HP_ACCOUNT_BTN)
#             btn.wait("ready", timeout=20)
#             btn.click_input()

    
#     def click_create_account(self):
#         self.logger.info("Clicking Create Account button")

#         with allure.step("Click Create Account"):
#             btn = self.main_window.child_window(**CreateAccountLocators.CREATE_ACCOUNT_BTN)
#             btn.wait("ready", timeout=20)
#             btn.click_input()

    
#     def wait_for_chrome_window(self):
#         self.logger.info("Waiting for HP Account Chrome window")

#         with allure.step("Wait for Chrome Create Account Page"):
#             deadline = time.time() + 160

#             while time.time() < deadline:
#                 for win in Desktop(backend="uia").windows(title_re=".*Chrome.*"):
#                     title = win.window_text().lower()

#                     if "hp account" in title or "create account" in title:
#                         win.set_focus()
#                         win.maximize()
#                         self.logger.info("HP Account Chrome window detected")
#                         return win

#                 time.sleep(2)

#             raise TimeoutError("HP Account Chrome window not found!")

    
#     def create_account(self):
#         self.logger.info("Filling Create Account form")

#         with allure.step("Fill Create Account Form"):

#             # Generate dynamic email + password
#             suffix = ''.join(random.choices(string.digits, k=4))
#             email = f"stagestack{suffix}@mailsac.com"
#             password = f"Password@{suffix}"
#             first_name = "Stage"
#             last_name = "Stack"

#             time.sleep(10)  # allow full form load

#             # FIRST NAME
#             pyautogui.typewrite(first_name, interval=0.05)
#             pyautogui.press("tab")

#             # LAST NAME
#             pyautogui.typewrite(last_name, interval=0.05)
#             pyautogui.press("tab")

#             # EMAIL
#             pyautogui.typewrite(email, interval=0.05)
#             pyautogui.press("tab")

#             # PASSWORD
#             pyautogui.typewrite(password, interval=0.05)
#             pyautogui.press("tab", presses=4)

#             # SUBMIT
#             pyautogui.press("enter")
#             self.logger.info(f"Submitted account form for {email}")

#             time.sleep(10)

        
#         self.logger.info("Fetching OTP from Mailsac inbox")

#         with allure.step("Fetch OTP"):
#             driver = webdriver.Chrome()
#             driver.get(f"https://mailsac.com/inbox/{email}")

#             wait = WebDriverWait(driver, 15)
#             start_time=time.time()


#             otp = None

#             while time.time()-start_time < 120:

                
#                 rows = driver.find_elements(**CreateAccountLocators.EMAIL)
#                 if rows:
#                     self.logger.info("Email list found → Clicking first email")
#                     rows[0].click()
#                     break

#                 driver.refresh()
#                 time.sleep(4)

#             # Extract OTP
#             body = wait.until(
#                 EC.visibility_of_element_located(**CreateAccountLocators.BODY)
#             ).text

#             match = re.search(r"\b(\d{6})\b", body)

#             driver.quit()

#             if not match:
#                 raise Exception("OTP not found in email content!")

#             otp = match.group(1)
#             self.logger.info(f"OTP Received: {otp}")

        
#         with allure.step("Enter OTP"):

#             time.sleep(2)
#             pyautogui.hotkey("ctrl", "shift", "tab")  # switch back to HP Account tab
#             time.sleep(3)

#             pyautogui.typewrite(otp, interval=0.07)
#             pyautogui.press('tab',presses=1,interval=0.3)
#             pyautogui.press('enter')

#             self.logger.info("OTP entered successfully")

    
#     def return_to_hp_smart(self):
#         self.logger.info("Switching back to HP Smart Desktop App")

#         with allure.step("Return to HP Smart App"):
#             time.sleep(30)

#             pyautogui.press("tab", presses=2)
#             time.sleep(1)
#             pyautogui.press("enter")

#             time.sleep(15)
#             self.main_window.set_focus()

#             self.logger.info("Successfully returned to HP Smart App")


import allure
import pytest
import random
import string
import re
import time
from datetime import datetime

import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pywinauto import Desktop, timings

from core.logger import get_logger
from resources.locators.desktop_locators import CreateAccountLocators


class CreateAccountPage:

    def __init__(self, main_window):
        self.main_window = main_window
        self.logger = get_logger(self.__class__.__name__)

    
    def open_manage_account(self):
        with allure.step("Open Manage HP Account"):
            self.logger.info("Opening Manage HP Account")

            self.main_window.set_focus()
            self.main_window.maximize()

            btn = self.main_window.child_window(**CreateAccountLocators.MANAGE_HP_ACCOUNT_BTN)
            btn.wait("ready", timeout=20)
            print("open_manage_account - clicking button")
            self.desktop_click(**CreateAccountLocators.MANAGE_HP_ACCOUNT_BTN)

    
    def click_create_account(self):
        with allure.step("Click Create Account"):
            self.logger.info("Clicking Create Account")

            btn = self.main_window.child_window(**CreateAccountLocators.CREATE_ACCOUNT_BTN)
            btn.wait("ready", timeout=20)
            btn.desktop_click(**CreateAccountLocators.CREATE_ACCOUNT_BTN)

    
    def wait_for_chrome_window(self):
        self.logger.info("Waiting for Chrome Account Window")

        with allure.step("Wait for Chrome Window"):
            deadline = time.time() + 160

            while time.time() < deadline:
                for win in Desktop(backend="uia").windows(title_re=".*Chrome.*"):
                    if any(x in win.window_text().lower() for x in ["hp account", "create account", "sign up"]):
                        win.set_focus()
                        win.maximize()
                        return win
                timings.wait_until_passes(2, 1, lambda: None)

            raise TimeoutError("Chrome Account window not detected!")

    
    def create_account(self):
        with allure.step("Fill Create Account Form"):
            self.logger.info("Filling Create Account Form")

            # Dynamically generate email/password
            suffix = ''.join(random.choices(string.digits, k=4))
            email = f"stagestack{suffix}@mailsac.com"
            password = f"Password@{suffix}"

            chrome_win = Desktop(backend="uia").window(title_re=".*Chrome.*")
            chrome_win.wait("exists ready", timeout=20)
            chrome_win.set_focus()

            # Correct renderer window
           

            # --- FIRST NAME ---
            first = chrome_win.window(**CreateAccountLocators.FIRST_NAME)
            first.wait("ready", timeout=20)
            first.type_keys("Stage", with_spaces=True)

            # --- LAST NAME ---
            last = chrome_win.window(**CreateAccountLocators.LAST_NAME)
            last.wait("ready", timeout=20)
            last.type_keys("Stack", with_spaces=True)

            # --- EMAIL ---
            email_box = chrome_win.window(**CreateAccountLocators.EMAIL)
            email_box.wait("ready", timeout=20)
            email_box.type_keys(email, with_spaces=True)

            # --- PASSWORD ---
            pwd_box = chrome_win.window(**CreateAccountLocators.PASSWORD)
            pwd_box.wait("ready", timeout=20)
            pwd_box.type_keys(password, with_spaces=True)

            # --- CREATE BUTTON ---
            create_btn = chrome_win.window(**CreateAccountLocators.CREATE_BTN)
            create_btn.wait("ready", timeout=20)
            create_btn.click_input()

            self.logger.info(f"Submitted Create Account for {email}")

        
        with allure.step("Fetch OTP from Mailsac"):
            self.logger.info("Fetching OTP")

            driver = webdriver.Chrome()
            driver.get(f"https://mailsac.com/inbox/{email}")
            wait = WebDriverWait(driver, 30)

            start = time.time()
            otp = None
            refresh_interval = 10      
            max_wait = 180             

            self.logger.info("Waiting for OTP email to arrive...")

            while time.time() - start < max_wait:

                rows = driver.find_elements(*CreateAccountLocators.MAILSAC_EMAIL_ROWS)

                if rows:
                    self.logger.info("Email detected! Opening email...")
                    rows[0].click()

                    # Wait for email body to load
                    try:
                        body_text = wait.until(
                            EC.visibility_of_element_located(CreateAccountLocators.MAILSAC_BODY)
                        ).text
                    except:
                        self.logger.warning("Email body not loaded yet… retrying.")
                        time.sleep(3)
                        continue

                    # Extract 6-digit code
                    match = re.search(r"\b(\d{6})\b", body_text)

                    if match:
                        otp = match.group(1)
                        self.logger.info(f"OTP Found: {otp}")
                        break

                    else:
                        self.logger.warning("Body loaded but OTP not found.")

                # Refresh inbox every 10 seconds
                self.logger.info("OTP not received yet. Refreshing inbox…")
                driver.refresh()
                time.sleep(refresh_interval)

            driver.quit()

            if not otp:
                raise Exception("OTP not found after waiting 3 minutes!")

            

        
        
        with allure.step("Enter OTP in Chrome"):
            chrome_win.set_focus()

            otp_box = chrome_win.child_window(**CreateAccountLocators.OTP_INPUT)
            otp_box.wait("ready", timeout=25)
            otp_box.set_edit_text(otp)

            submit_btn = chrome_win.child_window(**CreateAccountLocators.OTP_SUBMIT)
            submit_btn.wait("ready", timeout=20)
            submit_btn.click_input()

            self.logger.info("OTP submitted successfully")
            time.sleep(10)


    
    def return_to_hp_smart(self):
        with allure.step("Return to HP Smart App"):
            self.logger.info("Switching back to HP Smart app")

            time.sleep(30)

            pyautogui.press("tab", presses=2)
            time.sleep(1)
            pyautogui.press("enter")

            time.sleep(15)
            self.main_window.set_focus()

            self.logger.info("Successfully returned to HP Smart App")
