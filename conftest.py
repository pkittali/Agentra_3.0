# conftest.py
import pytest
from core.configManager import ConfigManager

ConfigManager.load()  # loads config.yaml by default

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="web", help="web|mobile|desktop|hybrid")

@pytest.fixture(scope="function")
def driver(request):
    platform = request.config.getoption("--platform")

    if platform == "web":
        from core.web_driver import WebDriverManager
        mgr = WebDriverManager()
        drv = mgr.get_driver()
        try:
            yield drv
        finally:
            mgr.quit()

    elif platform == "mobile":
        from core.mobile_driver import MobileDriverManager
        mgr = MobileDriverManager()
        drv = mgr.get_driver()
        try:
            yield drv
        finally:
            mgr.quit()

    elif platform == "desktop":
        from core.desktop_driver import DesktopDriverManager
        mgr = DesktopDriverManager()
        mgr.get_driver()  # sets mgr.main_window
        try:
            yield mgr
        finally:
            mgr.quit()

    elif platform == "hybrid":
        # hybrid simply yields a dict/obj holding both web and desktop (mobile optional)
        from core.web_driver import WebDriverManager
        from core.desktop_driver import DesktopDriverManager

        web_mgr = WebDriverManager(); web = web_mgr.get_driver()
        desk_mgr = DesktopDriverManager(); desk_mgr.get_driver()

        class Hybrid:
            def __init__(self, web, desk_mgr, web_mgr, desk_mgr_obj):
                self.web = web
                self.desktop = desk_mgr
                self._web_mgr = web_mgr
                self._desktop_mgr = desk_mgr_obj
            def close(self):
                try: self._web_mgr.quit()
                except: pass
                try: self._desktop_mgr.quit()
                except: pass

        handle = Hybrid(web, desk_mgr, web_mgr, desk_mgr)
        try:
            yield handle
        finally:
            handle.close()

    else:
        raise ValueError("Unknown platform option")
