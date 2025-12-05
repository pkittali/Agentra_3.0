import random
import string
import time
import allure
import pytest
from pages.base_page import BasePage
from utils.waits import WaitUtils
from selenium.webdriver.common.by import By
from resources.locators.web_locators import CreateAccountPageLocators, LoginPageLocators, OnboardPrinterPageLocators, PlanSelectionPageLocators, PrinterSelectionPageLocators
from core.logger import get_logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains

class PlanSelectionPage(BasePage):
    def __init__(self, driver):

        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)
        self.wait = WaitUtils(driver)

    def click_continue(self):
        self.logger.info("Clicking Continue button")
        with allure.step("Clicked Continue button"):
            self.click(*PlanSelectionPageLocators.CONTINUE_BUTTON) 

    def scroll_to_continue(self):
        self.logger.info("Scrolling to continue button")
        with allure.step("Scrolled to Continue button"):
            continue_button = self.wait.wait_for_element_to_be_clickable(*PlanSelectionPageLocators.CONTINUE_BUTTON, timeout=10)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", continue_button)
            time.sleep(1)
    
    def click_pay_as_you_print_plan(self):
        self.logger.info("Clicking Pay as you print button")
        with allure.step("Clicked Pay as you print button"):
            self.click(*PlanSelectionPageLocators.PAY_AS_YOU_PRINT_SELECT_BUTTON)

    def click_monthly_plan(self):
        self.logger.info("Clicking Monthly plan button")
        with allure.step("Clicked Monthly plan button"):
            self.wait.wait_until_clickable(*PlanSelectionPageLocators.MONTHLY_PLAN_SELECT_BUTTON)
            self.click(*PlanSelectionPageLocators.MONTHLY_PLAN_SELECT_BUTTON)

    def click_ink_and_paper_plan(self):
        self.logger.info("Clicking Ink and Paper plan button")
        with allure.step("Clicked Ink and Paper plan button"):
            self.click(*PlanSelectionPageLocators.INK_AND_PAPER_PLAN_SELECT_BUTTON)

    # def plan_selection(self):
    #      self.logger.info("Selecting both Monthly and Ink & Paper plans")

    #      with allure.step("Select Monthly plan"):
    #       self.logger.info("Clicking Monthly plan")
    #       self.click(*PlanSelectionPageLocators.MONTHLY_PLAN_SELECT_BUTTON)

    #      with allure.step("Select Ink and Paper plan"):
    #       self.logger.info("Clicking Ink and Paper plan")
    #       self.click(*PlanSelectionPageLocators.INK_AND_PAPER_PLAN_SELECT_BUTTON)


    def click_yearly_paln(self):
        self.logger.info("Clicking Yearly plan button")
        with allure.step("Clicked Yearly plan button"):
            self.click(*PlanSelectionPageLocators.YEARLY_PLAN_SELECT_BUTTON)

    def click_ink_plan(self):
        self.logger.info("Clicking Ink plan button")
        with allure.step("Clicked Ink plan button"):
            self.click(*PlanSelectionPageLocators.INK_PLAN_SELECT_BUTTON)
        
    def click_ink_and_paper_plan(self):
        self.logger.info("Clicking Ink and Paper plan button")
        with allure.step("Clicked Ink and Paper plan button"):
            self.click(*PlanSelectionPageLocators.INK_AND_PAPER_PLAN_SELECT_BUTTON)

    def click_ink_and_paper_plan_learn_more(self):
        self.logger.info("Clicking Ink and Paper plan Learn More link")
        with allure.step("Clicked Ink and Paper plan Learn More link"):
            self.click(*PlanSelectionPageLocators.INK_AND_PAPER_PLAN_LEARN_MORE)

    def click_plan_combobox_open(self):
        self.logger.info("Clicking Plan combobox to open")
        with allure.step("Clicked Plan combobox to open"):
            self.click(*PlanSelectionPageLocators.PLAN_COMBOBOX_OPEN_BUTTON)
    
    def click_ink_paper_tab(self):
        self.logger.info("Clicking Ink and Paper tab")
        with allure.step("Clicked Ink and Paper tab"):
            self.click(*PlanSelectionPageLocators.INK_PAPER_TAB)

    def click_ink_only_tab(self):
        self.logger.info("Clicking Ink only tab")
        with allure.step("Clicked Ink only tab"):
            self.click(*PlanSelectionPageLocators.INK_ONLY_TAB)

    def select_light_plan(self):
        self.logger.info("Selecting Light plan from dropdown")
        with allure.step("Selected Light plan from dropdown"):
            self.click(*PlanSelectionPageLocators.PLAN_CARD_LIGHT_RADIO)

    def select_occasional_plan(self):
        self.logger.info("Selecting Occasional plan from dropdown")
        with allure.step("Selected Occasional plan from dropdown"):
            self.click(*PlanSelectionPageLocators.PLAN_CARD_OCCASIONAL_RADIO)

    def select_moderate_plan(self):
        self.logger.info("Selecting Moderate plan from dropdown")
        with allure.step("Selected Moderate plan from dropdown"):
            self.click(*PlanSelectionPageLocators.PLAN_CARD_MODERATE_RADIO)

    def select_frequent_plan(self):
        self.logger.info("Selecting Frequent plan from dropdown")
        with allure.step("Selected Frequent plan from dropdown"):
            self.click(*PlanSelectionPageLocators.PLAN_CARD_FREQUENT_RADIO)

    def select_business_plan(self):
        self.logger.info("Selecting Business plan from dropdown")
        with allure.step("Selected Business plan from dropdown"):
            self.click(*PlanSelectionPageLocators.PLAN_CARD_BUSINESS_RADIO)

    def click_select_plan_button(self):
        self.logger.info("Clicking Select Plan button")
        with allure.step("Clicked Select Plan button"):
            self.click(*PlanSelectionPageLocators.PLAN_SELECT_BUTTON)

    def get_light_plan_price(self):
        return self.get_text(*PlanSelectionPageLocators.PLAN_CARD_LIGHT_PRICE)

    def get_occasional_plan_price(self):
        return self.get_text(*PlanSelectionPageLocators.PLAN_CARD_OCCASIONAL_PRICE)

    def get_moderate_plan_price(self):
        return self.get_text(*PlanSelectionPageLocators.PLAN_CARD_MODERATE_PRICE)

    def get_frequent_plan_price(self):
        return self.get_text(*PlanSelectionPageLocators.PLAN_CARD_FREQUENT_PRICE)
    
    def get_business_plan_price(self):
        return self.get_text(*PlanSelectionPageLocators.PLAN_CARD_BUSINESS_PRICE)

    def get_light_plan_pages(self):
        return self.get_text(*PlanSelectionPageLocators.PLAN_CARD_LIGHT_PAGES)

    def get_occasional_plan_pages(self):
        return self.get_text(*PlanSelectionPageLocators.PLAN_CARD_OCCASIONAL_PAGES)
    
    def get_moderate_plan_pages(self):
        return self.get_text(*PlanSelectionPageLocators.PLAN_CARD_MODERATE_PAGES)

    def get_frequent_plan_pages(self):
        return self.get_text(*PlanSelectionPageLocators.PLAN_CARD_FREQUENT_PAGES)

    def get_business_plan_pages(self):
        return self.get_text(*PlanSelectionPageLocators.PLAN_CARD_BUSINESS_PAGES)
    
    def get_occasional_plan_tag(self):
        return self.get_text(*PlanSelectionPageLocators.PLAN_CARD_OCCASIONAL_TAG)

    def get_plan_modal_title(self):
        return self.get_text(*PlanSelectionPageLocators.PLAN_MODAL_TITLE)

    def change_plan_to_business(self):
        self.logger.info("Changing plan to Business")
        with allure.step("Changed plan to Business"):
            self.click(*PlanSelectionPageLocators.CHANGE_PLAN_TO_BUSINESS)
    
    def select_monthly_plan(self, monthly_plan_value):
        self.click(*PlanSelectionPageLocators.PLAN_CARD_CURRENT_PAGE_DROPDOWN)
        self.select_custom_dropdown_by_text(monthly_plan_value)
        

    def plan_selection(self):
        self.logger.info("Selecting plan on Plan Selection Page")
        with allure.step("Selected plan on Plan Selection Page"):
            self.click_monthly_plan()
            self.click_ink_and_paper_plan()
            
            # self.click_continue()

            
    
        
            

    