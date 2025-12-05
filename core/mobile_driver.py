# core/mobile_driver.py
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.configManager import ConfigManager

class MobileDriverManager:
    def __init__(self):
        self.driver = None

    def get_driver(self):
        cfg = ConfigManager.get("mobile") or {}
        server = cfg.get("server", "http://127.0.0.1:4723/wd/hub")
        caps = cfg.get("caps", {})
        self.driver = webdriver.Remote(server, caps)
        self.driver.implicitly_wait(3)
        return self.driver

    def wait_for_element(self, locator_type, locator_value, timeout=15):
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
