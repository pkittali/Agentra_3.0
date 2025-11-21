import allure
import pytest
from pages.web import login_page
from core.logger import get_logger

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

    