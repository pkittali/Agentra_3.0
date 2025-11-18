import pytest
import apps

def pytest_addoption(parser):
    """Registers custom CLI arguments.

    Supported args:
        --platform: web | mobile | desktop
        --env: dev | qa | staging | prod
        --browser: chrome | firefox
    """    
    parser.addoption("--platform", action="store", default="web", help="Platform: web | mobile | desktop")

@pytest.fixture
def driver(request):
    """Create and yield a platform driver based on CLI arguments.

    Behavior:
        - Instantiates WebDriverManager / MobileDriverManager /
          DesktopDriverManager.
        - Applies SingletonDriver internally to ensure one instance per worker.
        - Yields driver to tests.
        - Ensures cleanup on teardown.
    """    
    platform = request.config.getoption("--platform")

    if platform == "web":
        from core.web_driver import WebDriverManager
        return WebDriverManager().get_driver()
    elif platform == "mobile":
        from core.mobile_driver import MobileDriverManager
        return MobileDriverManager().get_driver()
    elif platform == "desktop":
        from core.desktop_driver import DesktopDriverManager
        return DesktopDriverManager().get_driver()
    else:
        raise ValueError(f"Unknown platform: {platform}")

@pytest.fixture
def hpApp(request, driver):
    platform = request.config.getoption("--platform")

    if platform == "web":
        from apps.hp_web_app import HPAppWeb
        return HPAppWeb(driver)
    elif platform == "mobile":
        from apps.hp_mobile_app import HPAppMobile
        return HPAppMobile(driver)
    elif platform == "desktop":
        from apps.hp_desktop_app import HPAppDesktop
        return HPAppDesktop(driver)
