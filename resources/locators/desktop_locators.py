"""
Locator definitions for the <PAGE NAME> of the Desktop application.

This module provides all locators used by pywinauto to identify Windows UI
controls. Locators represent attributes exposed by the application’s
automation backend (UIA recommended).

Purpose:
    - Centralize desktop UI selectors for stable automation.
    - Avoid scattering control names or automation IDs across Page Objects.
    - Make locator updates simple when application versions change.

Locator Format:
    LOCATOR_NAME = ("attribute", "value")

Common pywinauto Attributes:
    - "name"        → Visible text of the control
    - "automation_id" → UIA Automation ID (preferred)
    - "class_name"  → Win32/Control class
    - "control_type" → UIA type (Button, Edit, Window)
    - "title"       → Window title
    
Example:
    LOGIN_WINDOW    = ("title", "HP Smart - Sign in")
    USERNAME_INPUT  = ("automation_id", "txtUser")
    SIGNIN_BUTTON   = ("name", "Sign In")

Usage:
    Page objects send these locators to pywinauto methods such as:
        window.child_window(**locator).click()
        window.child_window(**locator).type_keys()

Naming Convention:
    - CONSTANTS in UPPER_SNAKE_CASE
    - Use meaningful names describing the UI control
"""
from selenium.webdriver.common.by import By
class LoginPageLocators:
    """
    Desktop (pywinauto) locators for HP Smart / test login app window.
    Each locator is a dictionary that can be passed as **kwargs to driver.find_element(**locator)
    """
    USERNAME_INPUT = {"title": "Username", "control_type": "Edit"}
    PASSWORD_INPUT = {"title": "Password", "control_type": "Edit"}
    LOGIN_BUTTON = {"title": "Sign in", "control_type": "Button"}
    SUCCESS_MESSAGE = {"title": "Login Successful", "control_type": "Text"}
    ERROR_MESSAGE = {"title": "Invalid credentials", "control_type": "Text"}


# class CreateAccountLocators:
#     """
#     Desktop (pywinauto) locators for HP Smart → Manage HP Account → Create Account flow.
#     """
#     MANAGE_HP_ACCOUNT_BTN = { "title": "Manage HP Account","control_type": "Button","found_index": 0}
#     CREATE_ACCOUNT_BTN = {"title": "Create account","control_type": "Button"}
#     CHROME_WINDOW = {"title_re": ".*Chrome.*","control_type": "Window"}
#     HP_ACCOUNT_CHROME_WINDOW = {"title_re": ".*(HP Account|Create Account).*","control_type": "Window"}
#     OTP_INPUT = {"title_re": ".*Enter verification code.*","control_type": "Edit"}
#     SUBMIT_OTP_BTN = {"title": "Verify","control_type": "Button"}
#     POPUP_OPEN_BTN = {"title_re": "Open","control_type": "Button"}
#     POPUP_CONTINUE_BTN = {"title_re": "Continue","control_type": "Button"}
#     EMAIL=(By.CSS_SELECTOR, "tr.ng-scope")
#     BODY=(By.TAG_NAME, "body")


class CreateAccountLocators:
    """
    Desktop (pywinauto) locators for HP Smart Account Creation.
    """

    # --- HP Smart app buttons ---
    MANAGE_HP_ACCOUNT_BTN = {"title": "Manage HP Account", "control_type": "Button", "found_index": 0}
    CREATE_ACCOUNT_BTN = {"title": "Create account", "control_type": "Button"}

    # --- Chrome Window ---
    HP_ACCOUNT_CHROME_WINDOW = {"title_re": ".*(HP Account|Create Account|Sign Up).*", "control_type": "Window"}

    # --- Create Account Form Fields (Chrome) ---
    FIRST_NAME = {"title": "firstName", "control_type": "Edit"}
    LAST_NAME = {"title": "lastName", "control_type": "Edit"}
    EMAIL = {"title": "email", "control_type": "Edit"}
    PASSWORD = {"title": "password", "control_type": "Edit"}
    CREATE_BTN = {"title": "Create", "control_type": "Button"}

    # --- OTP ---
    OTP_INPUT = {"title": "code", "control_type": "Edit"}
    OTP_SUBMIT = {"title": "submit-code", "control_type": "Button"}

    # --- Mailsac (Selenium) ---
    MAILSAC_EMAIL_ROWS = (By.CSS_SELECTOR, "tr.ng-scope")
    MAILSAC_BODY = (By.TAG_NAME, "body")


class PrinterSetupLocators:
    """
    Desktop (pywinauto) locators for HP Smart Printersetup.
    """
    ADD_PRINTER_BTN = {'title': "Add Printer", 'control_type': "Button"}
    BEACONING_LIST = {'title': "BeaconingPrinters", 'auto_id': "BeaconingGridView", 'control_type': "List"}
    CONTINUE_BTN={'title="Continue", control_type="Text"'}
    WIFI_CONTINUE_BTN = {"title_re": ".*Access Wi-Fi password for.*", "control_type": "Button", "found_index": 1}

class PrinterPrivacyLocators:
    """
    Desktop (pywinauto) locators for HP Smart Printer Privacy.
    """
    PRIVACY_ACCEPT_BTN = {"title": "Accept all", "control_type": "Button"}
    APP_TITLE = {"title": "HP Smart"}

class ValuePropLocators:
    """
    Desktop (pywinauto) locators for HP Smart Printer Privacy.
    """
    NEXT_BTN = {"title": "Next", "control_type": "Button"}

class ShippingLocators:
    """
    Desktop (pywinauto) locators for HP Smart Shipping Page.
    """
    ADD_SHIPPING_BTN = {"title": "Add Shipping", "control_type": "Button"}

    STREET_BOX = {"auto_id": "street1", "control_type": "Edit"}
    CITY_BOX = {"auto_id": "city", "control_type": "Edit"}
    STATE_DROPDOWN = {"auto_id": "state", "control_type": "ComboBox"}
    STATE_LIST = {"auto_id": "state-listbox", "control_type": "List"}
    STATE_ITEM = {"title": "state", "control_type": "ListItem"}

    ZIP_BOX = {"auto_id": "zip-code", "control_type": "Edit"}
    PHONE_BOX = {"auto_id": "phoneNumberSmall", "control_type": "Edit"}

    SAVE_BTN = {"title": "Save", "control_type": "Button"}
    



