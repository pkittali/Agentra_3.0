# apps/hp_desktop_app.py
from pages.desktop.login_page import LoginPage

class HPAppDesktop:
    def __init__(self, desktop_mgr, main_window=None):
        # desktop_mgr is DesktopDriverManager (returned from conftest driver fixture)
        self.driver = desktop_mgr
        self.main_window = main_window or getattr(desktop_mgr, "main_window", None)
        self.login_page = LoginPage(self.driver, self.main_window)

    def login(self):
        self.login_page.open()
        # whatever sequence clicks login etc.
