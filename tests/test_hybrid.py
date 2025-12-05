# tests/test_hybrid.py
import pytest
from apps.hp_web_app import HPAppWeb
from apps.hp_desktop_app import HPAppDesktop
from core.configManager import ConfigManager

@pytest.mark.hybrid
@pytest.mark.flaky(reruns=1, reruns_delay=2)
def test_hybrid_web_desktop_flow(driver):
    """
    Hybrid test:
        Step 1 → Perform login on Web
        Step 2 → Switch to Desktop App and click Manage Account

    Run using:
        pytest tests/test_hybrid.py --platform hybrid
    """

    # HYBRID FIXTURE RETURNS AN OBJECT LIKE:
    #   driver.web     → raw Selenium webdriver
    #   driver.desktop → DesktopDriverManager instance

    # -----------------------------------------
    # STEP 1 → WEB LOGIN
    # -----------------------------------------
    username = ConfigManager.get_credential("username")
    password = ConfigManager.get_credential("password")

    web_app = HPAppWeb(driver.web)
    web_app.login(username, password)

    # You may assert something on web:
    assert driver.web.title is not None

    # -----------------------------------------
    # STEP 2 → DESKTOP INTERACTION
    # -----------------------------------------
    desktop_app = HPAppDesktop(driver.desktop, driver.desktop.main_window)

    desktop_app.login_page.open()
    desktop_app.login_page.click_manage_account()

    assert driver.desktop.main_window.exists()
