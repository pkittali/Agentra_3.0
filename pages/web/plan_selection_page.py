import allure
from pages.base_page import BasePage
from resources.locators.web_locators import PlanSelectionPageLocators
from utils.waits import WaitUtils
from core.logger import get_logger


class PlanSelectionPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def click_monthly_plan(self):
        self.logger.info("Clicking Monthly plan button")
        with allure.step("Clicked Monthly plan button"):
            self.click(*PlanSelectionPageLocators.MONTHLY_PLAN_SELECT_BUTTON)

    def click_ink_and_paper_plan(self):
        self.logger.info("Clicking Ink and Paper plan button")
        with allure.step("Clicked Ink and Paper plan button"):
            self.click(*PlanSelectionPageLocators.INK_AND_PAPER_PLAN_SELECT_BUTTON)

    def plan_selection(self):
        self.logger.info("Selecting plan on Plan Selection Page")
        with allure.step("Selected plan on Plan Selection Page"):
            self.click_monthly_plan()
            self.click_ink_and_paper_plan()