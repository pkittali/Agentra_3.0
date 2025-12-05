# tests/test_desktop.py
import pytest
from apps.hp_desktop_app import HPAppDesktop

@pytest.mark.desktop
@pytest.mark.flaky(reruns=1, reruns_delay=2)
def test_launch_desktop_app(driver):
    """
    Desktop app launch + click Manage HP Account
    Run using:
        pytest tests/test_desktop.py --platform desktop
    """

    # driver is DesktopDriverManager
    app = HPAppDesktop(driver, driver.main_window)

    # navigate to login page
    app.login_page.open()

    # click the "Manage HP Account" button
    app.login_page.click_manage_account()

    # Add validations as needed
    assert driver.main_window is not None
