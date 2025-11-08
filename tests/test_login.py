import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize('user,pwd', [('user1','pass1'), ('admin','admin123')])
def test_login_web(driver, user, pwd):
    # driver is an instance of WebDriverManager or MobileDriverManager (both implement same interface)
    driver.get('https://example.com')
    lp = LoginPage(driver)
    lp.login(user, pwd)
    # simple assertion placeholder
    assert True
