from core.web_driver import WebDriverManager
from core.mobile_driver import MobileDriverManager
from core.desktop_driver import DesktopDriverManager

class DriverFactory:
    @staticmethod
    def get_driver(platform='web'):
        if platform == 'web':
            return WebDriverManager().get_driver()
        elif platform == 'mobile':
            return MobileDriverManager().get_driver()
        elif platform == 'desktop':
            return DesktopDriverManager().get_driver()
        else:
            raise ValueError(f'Unsupported platform: {platform}')
