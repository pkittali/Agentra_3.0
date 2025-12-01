import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from resources.locators.web_locators import EnrollmentLocators


class EnrollmentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click Continue to Enroll button")
    def click_continue_button(self, timeout=60):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(EnrollmentLocators.CONTINUE_TO_ENROLL)
        ).click()
