import allure
import pytest
from core.testdataManager import TestDataManager
from core.logger import get_logger
from apps import HPAppWeb


logger = get_logger(__name__)

# @pytest.mark.flaky(reruns=2, reruns_delay=3)
# @pytest.mark.parametrize('user,pwd', [('student','Password123')])
@allure.title("Test Login Functionality on Web Platform")
@allure.description("""
This test validates the login functionality on the web platform using valid user credentials.
It ensures that:
1. The login page opens correctly.
2. Username and password are entered.
3. Login action succeeds.
4. Success message or post-login page is visible.
""")

def test_claimed(hpApp, user, pwd):

    # user = TestDataManager.get("login", "valid", "username")
    # pwd = TestDataManager.get("login", "valid", "password")
    logger.info(f"Starting test_login_web with user={user}")
    hpApp.launch_web()
    hpApp.create_account()
    hpApp.checkout_upto_shipping_billing()
    hpApp.enter_shipping_details()
    hpApp.enter_billing_details()
    hpApp.apply_promo_code()
    hpApp.click_continue_button()
    hpApp.deep_link_pages()
    
    
