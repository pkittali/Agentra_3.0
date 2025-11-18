# core/desktop_driver.py
import os
import time
import subprocess
from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError


class DesktopDriverManager:
    """Desktop platform driver implementation using pywinauto.

    Manages launching desktop applications and exposing automation
    APIs through BaseDriver compatibility.

    Args:
        app_path (str): Path to application executable.
        backend (str): pywinauto backend ("uia" recommended).

    Methods:
        get_driver(): Launch the desktop app.
        find_element(...): Locate window control elements.
        click(...): Invoke click patterns on UI elements.
        send_keys(...): Type into desktop input fields.
        wait_for_element(...): Wait for window/control states.
        quit(): Close the application window and release handles.
    """
    def __init__(self):
        self.app = None
        self.main_window = None

    def _get_hp_smart_appid(self):
        """Retrieve HP Smart AppID dynamically using PowerShell"""
        try:
            cmd = [
                "powershell",
                "-Command",
                "Get-StartApps | Where-Object { $_.Name -like '*HP Smart*' } | Select-Object -ExpandProperty AppID"
            ]
            appid = subprocess.check_output(cmd, text=True).strip()
            if not appid:
                raise FileNotFoundError("HP Smart AppID not found. Ensure HP Smart is installed.")
            return appid
        except Exception as e:
            raise FileNotFoundError(f"Failed to get HP Smart AppID: {e}")

    def get_driver(self):
        """Launch HP Smart app via its AppID and return the main window."""
        appid = self._get_hp_smart_appid()
        print(f"Launching HP Smart via AppID: {appid}")

        # Launch the app (UWP)
        os.system(f'start shell:appsFolder\\{appid}')
        time.sleep(5)

        try:
            # Attach to running window
            self.app = Application(backend="uia").connect(title_re=".*HP Smart.*")
            self.main_window = self.app.window(title_re=".*HP Smart.*")
            self.main_window.wait("visible", timeout=20)
            print("✅ Connected to HP Smart window successfully.")
            return self.main_window
        except ElementNotFoundError:
            raise Exception("⚠️ HP Smart window not found after launch.")

    def quit(self):
        """Close HP Smart app gracefully."""
        if self.main_window:
            try:
                self.main_window.close()
                print("✅ HP Smart closed.")
            except Exception:
                pass
