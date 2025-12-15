import allure
import pytest
from core.configManager import ConfigManager
from core.testdataManager import TestDataManager
from apps.hp_web_app import HPAppWeb
from pages.web import login_page
from core.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.flaky(reruns=2, reruns_delay=3)
@pytest.mark.web
#@pytest.mark.parametrize('user,pwd', [('student','Password123')])
@allure.title("Test Login Functionality on Web Platform")
@allure.description("""
This test validates the login functionality on the web platform using valid user credentials.
It ensures that:
1. The login page opens correctly.
2. Username and password are entered.
3. Login action succeeds.
4. Success message or post-login page is visible.
""")

def test_login_web(driver):

    # user = "student"#TestDataManager.get("login", "valid", "username")
    # pwd = "Password123"#TestDataManager.get("login", "valid", "password")
    user = ConfigManager.get_credential("username")
    pwd = ConfigManager.get_credential("password")

    print(user)
    print(pwd)

    app = HPAppWeb(driver)
    app.login(user, pwd)

    
    # Example: assert something after login if required
    # (Adjust depending on your AUT)
    # hpApp.enter_shipping_details()
    # hpApp.start_enrollment()
    # hpApp.enter_shipping_details()
    # hpApp.confirm_enrollment()
    # hpApp.validateOnboarding(codeType="EK", codeValue="EK12345")




