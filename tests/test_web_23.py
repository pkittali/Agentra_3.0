import allure
from apps.hp_web_app import HPAppWeb
from core.configManager import ConfigManager
import pytest
from pages.web import login_page
from core.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.flaky(reruns=2, reruns_delay=3)
@pytest.mark.web
@allure.title("Test Login Functionality on Web Platform")
@allure.description("""
This test validates the login functionality on the web platform using valid user credentials.
It ensures that:
1. The login page opens correctly.
2. Username and password are entered.
3. Login action succeeds.
4. Success message or post-login page is visible.
""")

def test_23_multiple_codes_ui_special_offer_enroll_oobe(driver): 

    ca_address = ConfigManager.get_shipping("ca_address")
    card = ConfigManager.get_billing("card_number")
    exp_month = ConfigManager.get_billing("expiry_month")
    exp_year = ConfigManager.get_billing("expiry_year")
    cvv = ConfigManager.get_billing("cvv")

    hpApp = HPAppWeb(driver)
    logger.info(f"Starting test_01_validate_promo")

    hpApp.launch_web()
    hpApp.create_account()
    claim_code="ABCDEFGH"
    hpApp.onboard_printer(claim_code)
    hpApp.checkout_upto_shipping_billing()
    hpApp.enter_shipping_details(ca_address["mobile"],
                                 ca_address["street"],
                                 ca_address["city"],
                                 ca_address["state"],
                                 ca_address["zip_code"])
    hpApp.enter_billing_details(card,exp_month,exp_year,cvv)
    
    hpApp.apply_and_validate_multiple_codes()
    hpApp.validate_and_checkout_till_subscription()
    hpApp.navigate_to_subscription_and_validate_plan()

    
    
    
    
    
