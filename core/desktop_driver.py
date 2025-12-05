# core/desktop_driver.py
import os
import time
import subprocess
from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError

class DesktopDriverManager:
    def __init__(self, backend="uia", appid=None):
        self.app = None
        self.main_window = None
        self.backend = backend
        self._appid = appid

    def _get_appid(self):
        if self._appid:
            return self._appid
        try:
            cmd = [
                "powershell",
                "-Command",
                "Get-StartApps | Where-Object { $_.Name -like '*HP Smart*' } | Select-Object -ExpandProperty AppID"
            ]
            appid = subprocess.check_output(cmd, text=True).strip()
            return appid
        except Exception:
            return None

    def get_driver(self):
        appid = self._get_appid()
        if appid:
            os.system(f"start shell:appsFolder\\{appid}")
            time.sleep(2)
        # attach to a matching window
        try:
            self.app = Application(backend=self.backend).connect(title_re=".*HP Smart.*")
            self.main_window = self.app.window(title_re=".*HP Smart.*")
            self.main_window.wait("visible ready", timeout=20)
            return self
        except ElementNotFoundError:
            raise Exception("HP Smart window not found")

    def wait_for_element(self, locator_or_dict, timeout=15):
        # locator_or_dict is a dict of pywinauto properties
        el = self.main_window.child_window(**locator_or_dict)
        el.wait("exists ready", timeout=timeout)
        return el

    def find_element(self, locator_or_dict):
        return self.main_window.child_window(**locator_or_dict)

    def click(self, locator_or_dict):
        el = self.find_element(locator_or_dict)
        el.wait("ready", timeout=8)
        el.click_input()

    def send_keys(self, locator_or_dict, text):
        el = self.find_element(locator_or_dict)
        el.set_edit_text(text)

    def quit(self):
        try:
            if self.main_window:
                self.main_window.close()
        except Exception:
            pass
