import allure
import pytest
from pages.web import login_page
from core.logger import get_logger
from pages.web.special_offers_page import SpecialOffersPage
# from apps import hp_app

logger = get_logger(__name__)

# @pytest.mark.flaky(reruns=2, reruns_delay=5)
@allure.description("""
This test validates the Sign up functionality on the web platform using valid user credentials.
It ensures that:
1. InstantInk landing page URL is launched successfully.
2. Navigating to create account
3. Entering user credentials correctly
4. Creating account
""")
def test_23_multiple_codes_ui_special_offer_enroll_oobe(hpApp): 
    
    logger.info(f"Starting test_01_validate_promo")
    hpApp.launch_web()
    hpApp.create_account()
    hpApp.onboard_printer()
    hpApp.checkout_upto_shipping_billing()
    hpApp.enter_shipping_details()
    hpApp.enter_billing_details()
    hpApp.apply_and_validate_multiple_codes()
    hpApp.validate_and_checkout_till_subscription()
    hpApp.navigate_to_subscription_and_validate_plan()

    
    
    