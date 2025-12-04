class DriverOrchestrator:

    def __init__(self):
        self.web_driver = None
        self.desktop_driver = None

    def start_web(self):
        from core.web_driver import WebDriverManager
        self.web_driver = WebDriverManager().get_driver()
        return self.web_driver

    def start_desktop(self):
        from core.desktop_driver import DesktopDriverManager
        self.desktop_driver = DesktopDriverManager().get_driver()
        return self.desktop_driver

    def get_web(self):
        return self.web_driver

    def get_desktop(self):
        return self.desktop_driver

    def cleanup(self):
        if self.web_driver:
            self.web_driver.quit()
        if self.desktop_driver:
            self.desktop_driver.quit()
