# core/web_driver.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebDriverManager:
    def __init__(self, browser="chrome"):
        self.browser = browser
        self.driver = None

    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        # options.add_argument("--headless")  # enable if needed
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(3)
        return self.driver

    def wait_for_element(self, locator_type, locator_value, timeout=10):
        by = getattr(By, locator_type.upper())
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator_value))
        )

    def find_element(self, locator_type, locator_value):
        by = getattr(By, locator_type.upper())
        return self.driver.find_element(by, locator_value)

    def click(self, locator_type, locator_value):
        el = self.find_element(locator_type, locator_value)
        el.click()

    def send_keys(self, locator_type, locator_value, text):
        el = self.find_element(locator_type, locator_value)
        el.clear()
        el.send_keys(text)

    def quit(self):
        try:
            if self.driver:
                self.driver.quit()
        except Exception:
            pass
