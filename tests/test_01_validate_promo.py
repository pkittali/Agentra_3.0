import allure
import pytest
from pages.web import login_page
from core.logger import get_logger
from pages.web.special_offers_page import SpecialOffersPage
from apps import hp_app

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
# @pytest.mark.parametrize('user,pwd', [('student','Password123')])
def test_01_validate_promo(hpApp): 
    
    logger.info(f"Starting test_01_validate_promo")
    hpApp.launch_web()
    hpApp.create_account()
    # hpApp.onboard_printer()
    hpApp.checkout_upto_shipping_billing()
    hpApp.enter_shipping_details()
    hpApp.enter_billing_details()
    hpApp.apply_promo_code()


    special_offers = SpecialOffersPage(hpApp.driver)
    required_billing_message = special_offers.get_require_billing_message_text().lower()
    code_name = special_offers.get_enrollment_key_label().lower()
    trail_months = special_offers.get_enrollment_key_verifymonths_text().lower()
    assert "A payment method is needed on file to enroll" in required_billing_message, "A payment method is needed on file to enroll is not found"
    assert "Enrollment Key" in code_name , "Enrollment Key should be in the breakdown text"
    assert "1 month" in trail_months, "Trial months should be mentioned in the breakdown text"
    