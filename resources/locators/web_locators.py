"""
Locator definitions for the <PAGE NAME> of the Web application.

This module contains all Selenium-compatible web element locators for the
corresponding page. Each locator is defined as a constant tuple using a
Selenium `By` strategy and its associated value.

Purpose:
    - Centralize all web selectors for maintainability.
    - Provide clean separation between structure (locators) and behavior (Page Objects).
    - Avoid hard-coded selectors inside page logic.
    - Simplify UI updates — changes occur here, not in tests or page classes.

Locator Format:
    LOCATOR_NAME = (By.<STRATEGY>, "locator_value")

Common Strategies:
    - By.ID
    - By.NAME
    - By.XPATH
    - By.CSS_SELECTOR
    - By.CLASS_NAME
    - By.LINK_TEXT
    - By.TAG_NAME

Example:
    USERNAME_INPUT = (By.ID, "username")
    LOGIN_BUTTON   = (By.XPATH, "//button[@id='submit']")

Usage:
    Page objects import these constants and use them with WebDriver's
    find_element(), click(), send_keys(), and wait utilities.

Naming Convention:
    - CONSTANTS in UPPER_SNAKE_CASE
    - Group locators logically by page sections if needed
"""
import logging
from selenium.webdriver.common.by import By

# class LoginPageLocators:
#     USERNAME_INPUT = (By.ID, "username")
#     PASSWORD_INPUT = (By.ID, "password")
#     LOGIN_BUTTON = (By.XPATH, "//button[@id='submit1']")
#     SUCCESS_MESSAGE = (By.XPATH, "//*[text()='Logged In Successfully']")
#     ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")


# class EnrollmentPageLocators:
#     START_BUTTON = (By.XPATH, "//button[text()='Start Enrollment']")
#     CONTINUE_BUTTON = (By.XPATH, "//button[text()='Continue']")
#     SHIPPING_ADDRESS_INPUT = (By.NAME, "shippingAddress")
#     SUBMIT_BUTTON = (By.XPATH, "//button[text()='Submit']")


# class SpecialOfferModalLocators:
#     EK_CODE_INPUT = (By.ID, "ek-code")
#     APPLY_BUTTON = (By.XPATH, "//button[text()='Apply']")
#     SUCCESS_TOAST = (By.CSS_SELECTOR, ".toast-success")
#     NOTIFICATION_MESSAGE = (By.XPATH, "//*[contains(text(),'payment method is needed')]")
#     CREDITS_BREAKDOWN_SECTION = (By.CSS_SELECTOR, ".credits-breakdown")
#     CODE_NAME_TEXT = (By.XPATH, "//div[contains(@class, 'code-name')]")
#     TRIAL_MONTHS_TEXT = (By.XPATH, "//div[contains(@class, 'trial-months')]")



class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//*[text()='Logged In Successfully']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    

class LandingPageLocators:
    ACCEPT_BUTTON = (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    SIGN_UP_NOW_BUTTON=(By.XPATH, "//button[@data-testid='header-sign-up-button']")
   # MAIN_PAGE_IDENTIFIER = (By.CSS_SELECTOR, "header")

class CreateAccountPageLocators:
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-testid='create-account-button']")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
    EMAIL_HELPER_TEXT = (By.XPATH, "//p[@id='email-helper-text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//button[@aria-label='Show password']")
    MARKETING_CONSENT_CHECKBOX = (By.XPATH, "//input[@id='market']")
    MARKETING_CONSENT_TEXT = (By.XPATH, "//span[contains(text(),'HP may email me')]")
    PRIVACY_STATEMENT_LINK = (By.XPATH, "//a[@id='privacy_link']")
    SUBMIT_CREATE_ACCOUNT = (By.XPATH, "//button[@id='sign-up-submit']")
    VERIFY_BUTTON = (By.XPATH, "//button[contains(@id,'submit-code')]")
    VERIFICATION_CODE_INPUT = (By.XPATH, "//input[@id='code']")

class OnboardPrinterPageLocators:
    CLAIM_CODE_INPUT = (By.XPATH, "//input[@id='claim-code-input' and @type='text']")
    CANCEL_BUTTON = (By.XPATH, "//a[@id='AddPrinter-cancel-btn' and contains(@class, 'button')]")
    ADD_BUTTON = (By.XPATH, "//a[@id='AddPrinter-add-btn' and contains(@class, 'button')]")
    ACCEPT_BUTTON= (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")

class PrinterSelectionPageLocators:
    PRINTER_SELECTION_STEP = (By.XPATH, "//div[@data-testid='printer-selection-step']")
    PRINTER_SELECTION_TITLE = (By.XPATH, "//div[@data-testid='printer-selection-step']//h4[contains(text(),'Confirm a printer for HP Instant Ink')]")
    PRINTER_CARD = (By.XPATH, "//div[@data-testid='printer-card']")
    PRINTER_CARD_TITLE = (By.XPATH, "//div[@data-testid='printer-card']//h6[@class='printer-title']")
    PRINTER_CARD_SERIAL = (By.XPATH, "//div[@data-testid='printer-card']//p[@class='printer-details']")
    PRINTER_CARD_BENEFITS = (By.XPATH, "//div[@data-testid='printer-card']//div[contains(@class,'PrinterBenefitsContent')]")
    PRINTER_CARD_BENEFITS_TEXT = (By.XPATH, "//div[@data-testid='printer-card']//div[contains(@class,'PrinterBenefitsMessage')]")
    PRINTER_CARD_RADIO = (By.XPATH, "(//div[@data-testid='printer-card']//input[@type='radio'])[1]/following-sibling::span")
    ADD_PRINTER_CARD = (By.XPATH, "//div[@data-testid='add-printer-card']")
    ADD_PRINTER_CARD_RADIO = (By.XPATH, "//div[@data-testid='printer-card' and .//p[contains(text(),'Serial No. ')]]//input[@type='radio']")
    ADD_PRINTER_CARD_TITLE = (By.XPATH, "//div[@data-testid='add-printer-card']//h5")
    ADD_PRINTER_CARD_DESC = (By.XPATH, "//div[@data-testid='add-printer-card']//p")
    SLICK_PREV_BUTTON = (By.XPATH, "//button[contains(@class,'slick-prev')]")
    SLICK_NEXT_BUTTON = (By.XPATH, "//button[contains(@class,'slick-next')]")
    ERROR_MESSAGE_CONTAINER = (By.XPATH, "//div[contains(@class,'ErrorMessageContainer')]")
    ERROR_MESSAGE_TEXT = (By.XPATH, "//div[contains(@class,'ErrorMessage')]//p")
    CONNECTIVITY_GUIDE_LINK = (By.XPATH, "//a[contains(@class,'ConnectivityGuide')]")
    CONTINUE_BUTTON = (By.XPATH, "//button[@data-testid='continue-button' and span[text()='Continue']]")

class PlanSelectionPageLocators:
    # Pay As You Print Plan
    PAY_AS_YOU_PRINT_PLAN_CARD = (By.XPATH, "//div[@data-testid='i_pay_as_you_print-type-card-content-container']")
    PAY_AS_YOU_PRINT_PLAN_TITLE = (By.XPATH, "//p[@data-testid='plan-type-card-title' and text()='Pay As You Print plan']")
    PAY_AS_YOU_PRINT_PLAN_SAVINGS = (By.XPATH, "//p[@data-testid='plan-type-card-savings']")
    PAY_AS_YOU_PRINT_PLAN_STARTING_PRICE = (By.XPATH, "//p[@data-testid='plan-type-card-starting-price']")
    PAY_AS_YOU_PRINT_PLAN_BENEFIT = (By.XPATH, "//p[@data-testid='plan-type-card-benefit-text']")
    PAY_AS_YOU_PRINT_SELECT_BUTTON = (By.XPATH, "//button[@data-testid='i_pay_as_you_print-plan-type-card-select-button']")
    # Monthly Plan
    MONTHLY_PLAN_CARD = (By.XPATH, "//div[@data-testid='i_ink-type-card-content-container']")
    MONTHLY_PLAN_LABEL = (By.XPATH, "//div[@data-testid='card-label-i_ink']//p[contains(text(),'MOST POPULAR')]")
    MONTHLY_PLAN_TITLE = (By.XPATH, "//p[@data-testid='plan-type-card-title' and text()='Monthly plan']")
    MONTHLY_PLAN_SAVINGS = (By.XPATH, "//p[@data-testid='plan-type-card-savings']")
    MONTHLY_PLAN_STARTING_PRICE = (By.XPATH, "//p[@data-testid='plan-type-card-starting-price']")
    MONTHLY_PLAN_BENEFIT = (By.XPATH, "//p[@data-testid='plan-type-card-benefit-text']")
    MONTHLY_PLAN_SELECT_BUTTON = (By.XPATH, "//button[@data-testid='i_ink-plan-type-card-select-button']")
    # Yearly Plan
    YEARLY_PLAN_CARD = (By.XPATH, "//div[@data-testid='i_yearly_ink-type-card-content-container']")
    YEARLY_PLAN_LABEL = (By.XPATH, "//div[@data-testid='card-label-i_yearly_ink']//p[contains(text(),'BEST SAVINGS')]")
    YEARLY_PLAN_TITLE = (By.XPATH, "//p[@data-testid='plan-type-card-title' and text()='Yearly plan']")
    YEARLY_PLAN_SAVINGS = (By.XPATH, "//p[@data-testid='plan-type-card-savings']")
    YEARLY_PLAN_STARTING_PRICE = (By.XPATH, "//p[@data-testid='plan-type-card-starting-price']")
    YEARLY_PLAN_BENEFIT = (By.XPATH, "//p[@data-testid='plan-type-card-benefit-text']")
    YEARLY_PLAN_SELECT_BUTTON = (By.XPATH, "//button[@data-testid='i_yearly_ink-plan-type-card-select-button']")
    # Plan Selector V3
    PLAN_SELECTOR_CONTENT_CONTAINER = (By.XPATH, "//div[@data-testid='plan-selector-v3-content-container']")
    MONTHLY_PLANS_HEADING = (By.XPATH, "//h1[normalize-space()='Monthly plans']")
    CURRENT_PAGE_PLAN_SELECTION_LABEL = (By.XPATH, "//div[contains(@class,'Title-@jarvis/react-instant-ink-plans__sc-uqs771-1') and contains(text(),'Current page plan selection')]")
    PLAN_COMBOBOX = (By.XPATH, "//div[@data-testid='plans-selector-v3-combobox']")
    PLAN_COMBOBOX_SELECTED_OPTION = (By.XPATH, "//div[@data-testid='plans-selector-v3-combobox']//span[contains(@class,'titleLabel')]")
    PLAN_COMBOBOX_OPEN_BUTTON = (By.XPATH, "//div[@data-testid='plans-selector-v3-combobox']//div[@aria-label='Open']")
    # Ink Plan Card
    INK_PLAN_CARD = (By.XPATH, "//div[@data-testid='card-content-container-plan-info'][.//div[contains(text(),'Ink plan')]]")
    INK_PLAN_TITLE = (By.XPATH, "//div[contains(@class,'Title-@jarvis/react-instant-ink-plans__sc-1vubsqb-3') and text()='Ink plan']")
    INK_PLAN_DESCRIPTION = (By.XPATH, "//div[contains(@class,'Description-@jarvis/react-instant-ink-plans__sc-1vubsqb-4')]//p")
    INK_PLAN_ATTRIBUTE_ORIGINAL_HP_INK = (By.XPATH, "//div[contains(text(),'Original HP ink')]")
    INK_PLAN_ATTRIBUTE_RECYCLING = (By.XPATH, "//div[contains(text(),'Ink cartridge recycling')]")
    INK_PLAN_ATTRIBUTE_SHIPPING = (By.XPATH, "//div[contains(text(),'Shipping included')]")
    INK_PLAN_PRICE = (By.XPATH, "//div[contains(@class,'PlanPriceContainer')]//h1")
    INK_PLAN_SELECT_BUTTON = (By.XPATH, "//button[@data-testid='select-plan-ink-only']")
    # Ink + Paper Plan Card
    INK_AND_PAPER_PLAN_CARD = (By.XPATH, "//div[@data-testid='card-content-container-plan-info'][.//div[contains(text(),'Ink + paper plan')]]")
    INK_AND_PAPER_PLAN_TITLE = (By.XPATH, "//div[contains(@class,'Title-@jarvis/react-instant-ink-plans__sc-1vubsqb-3') and text()='Ink + paper plan']")
    INK_AND_PAPER_PLAN_DESCRIPTION = (By.XPATH, "//div[contains(@class,'Description-@jarvis/react-instant-ink-plans__sc-1vubsqb-4')]//p")
    INK_AND_PAPER_PLAN_LEARN_MORE = (By.XPATH, "//a[contains(text(),'Learn more')]")
    INK_AND_PAPER_PLAN_ATTRIBUTE_ORIGINAL_HP_INK = (By.XPATH, "//div[contains(text(),'Original HP ink')]")
    INK_AND_PAPER_PLAN_ATTRIBUTE_QUALITY_PAPER = (By.XPATH, "//div[contains(text(),'High-quality HP Paper')]")
    INK_AND_PAPER_PLAN_ATTRIBUTE_RECYCLING = (By.XPATH, "//div[contains(text(),'Ink cartridge recycling')]")
    INK_AND_PAPER_PLAN_ATTRIBUTE_SHIPPING = (By.XPATH, "//div[contains(text(),'Shipping included')]")
    INK_AND_PAPER_PLAN_PRICE = (By.XPATH, "//div[contains(@class,'PlanPriceContainer')]//h1")
    INK_AND_PAPER_PLAN_SELECT_BUTTON = (By.XPATH, "//button[@data-testid='select-plan-ink-and-paper']")
    #New locators for plan selection page
    # Main Containers and Titles
    PLAN_INFO_MODAL = (By.XPATH, "//div[@data-testid='plan-info']")
    PLAN_MODAL_TITLE = (By.XPATH, "//h1[contains(text(),'Select your printing plan')]")
    PLAN_TABS = (By.XPATH, "//nav[contains(@class,'Tabs')]")
    INK_PAPER_TAB = (By.XPATH, "//div[@id='i_ink_paper']")
    INK_ONLY_TAB = (By.XPATH, "//div[@id='i_ink']")
    INK_PAPER_TAB_IMAGE = (By.XPATH, "//img[@data-testid='ink-paper-image-tab']")
    INK_ONLY_TAB_IMAGE = (By.XPATH, "//img[@data-testid='ink-only-image-tab']")
    INK_PAPER_TAB_LABEL = (By.XPATH, "//div[@id='i_ink_paper']//span[contains(text(),'Ink + Paper Plans')]")
    INK_ONLY_TAB_LABEL = (By.XPATH, "//div[@id='i_ink']//span[contains(text(),'Ink Plans')]")
    PLAN_SUBTITLE = (By.XPATH, "//span[@data-testid='ii-ink-paper']")
    PLAN_MORE_INFO = (By.XPATH, "//span[@data-testid='plans-selector-plan-cards-more-info']")
    PLAN_INFO_ICON = (By.XPATH, "//svg[@data-testid='plans-consumer-plan-content-info-icon']")
    PLAN_SELECT_BUTTON = (By.XPATH, "//button[@data-testid='consumer-plans-select-plans']")
    # Plan Cards
    PLAN_CARD_LIGHT = (By.XPATH, "//div[@data-testid='plans-selector-desktop-plan-card-0']")
    PLAN_CARD_OCCASIONAL = (By.XPATH, "//div[@data-testid='plans-selector-desktop-plan-card-1']")
    PLAN_CARD_MODERATE = (By.XPATH, "//div[@data-testid='plans-selector-desktop-plan-card-2']")
    PLAN_CARD_FREQUENT = (By.XPATH, "//div[@data-testid='plans-selector-desktop-plan-card-3']")
    PLAN_CARD_BUSINESS = (By.XPATH, "//div[@data-testid='plans-selector-desktop-plan-card-4']")
    # Plan Names
    PLAN_CARD_LIGHT_TITLE = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-0-plan-name-title']")
    PLAN_CARD_OCCASIONAL_TITLE = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-1-plan-name-title']")
    PLAN_CARD_MODERATE_TITLE = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-2-plan-name-title']")
    PLAN_CARD_FREQUENT_TITLE = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-3-plan-name-title']")
    PLAN_CARD_BUSINESS_TITLE = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-4-plan-name-title']")
    # Plan Pages
    PLAN_CARD_CURRENT_PAGE_DROPDOWN = (By.XPATH, "//*[@data-testid='plans-selector-v3-combobox']")
    PLAN_CARD_OCCASIONAL_PAGES = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-1-pages-title']")
    PLAN_CARD_MODERATE_PAGES = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-2-pages-title']")
    PLAN_CARD_FREQUENT_PAGES = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-3-pages-title']")
    PLAN_CARD_BUSINESS_PAGES = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-4-pages-title']")
    # Plan Prices
    PLAN_CARD_LIGHT_PRICE = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-0-price-title']")
    PLAN_CARD_OCCASIONAL_PRICE = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-1-price-title']")
    PLAN_CARD_MODERATE_PRICE = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-2-price-title']")
    PLAN_CARD_FREQUENT_PRICE = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-3-price-title']")
    PLAN_CARD_BUSINESS_PRICE = (By.XPATH, "//h1[@data-testid='plans-selector-plan-card-4-price-title']")
    # Plan Tags
    PLAN_CARD_OCCASIONAL_TAG = (By.XPATH, "//span[@data-testid='plans-selector-plan-card-1-plan-tag-title']")
    # Plan Radio Buttons
    PLAN_CARD_LIGHT_RADIO = (By.XPATH, "//input[@data-testid='plan-radio-button-i_ink_paper-10']")
    PLAN_CARD_OCCASIONAL_RADIO = (By.XPATH, "//input[@data-testid='plan-radio-button-i_ink_paper-50']")
    PLAN_CARD_MODERATE_RADIO = (By.XPATH, "//input[@data-testid='plan-radio-button-i_ink_paper-100']")
    PLAN_CARD_FREQUENT_RADIO = (By.XPATH, "//input[@data-testid='plan-radio-button-i_ink_paper-300']")
    PLAN_CARD_BUSINESS_RADIO = (By.XPATH, "//input[@data-testid='plan-radio-button-i_ink_paper-700']")
    CONTINUE_BUTTON = (By.XPATH, "//button[@data-testid='consumer-plans-select-plans']")
    #Change plan
    CHANGE_PLAN_TO_BUSINESS= (By.XPATH,"(//span[contains(@class, 'vn-radio-button__icon')])[5]")

class HPCheckoutPageLocators:
    EXPRESS_CHECKOUT_CARDS_CONTAINER = (By.XPATH, "//div[@data-testid='express-checkout-cards']")
    PLAN_CARD = (By.XPATH, "//div[@data-testid='plan-card']")
    PLAN_CARD_TITLE = (By.XPATH, "//h6[normalize-space()='Your Plan']")
    PLAN_CARD_TOOLTIP = (By.XPATH, "//svg[@data-testid='plan-card-tooltip']")
    PLAN_INFO_FREQUENCY = (By.XPATH, "//h6[contains(@class,'Frequency')]")
    PLAN_INFO_PAGES_PER_MONTH = (By.XPATH, "//p[contains(@class,'PagesPerMonth')]")
    PLAN_INFO_PRICE_PER_MONTH = (By.XPATH, "//p[contains(@class,'PricePerMonth')]")
    EDIT_PLAN_BUTTON = (By.XPATH, "//button[@data-testid='edit-plan']")
    EXPRESS_CHECKOUT_TITLE = (By.XPATH, "//div[@data-testid='hp-express-checkout-card']//h6[normalize-space()='Checkout']")
    EXPRESS_CHECKOUT_BUTTONS_CONTAINER = (By.XPATH, "//div[@id='express-checkout-buttons']")
    EXPRESS_CHECKOUT_TEXT = (By.XPATH, "//p[contains(text(),'Express checkout')]")
    PAYPAL_EXPRESS_BUTTON = (By.XPATH, "//div[@data-testid='choose-paypal-express']")
    PAYPAL_WEB_BUTTON = (By.XPATH, "//div[@data-testid='web-paypal-express']")
    HP_CHECKOUT_BUTTON = (By.XPATH, "//button[@data-testid='choose-HP-checkout']")

class SpecialOffersPageLocators:   
    logger = logging.getLogger()
    
    SPECIAL_OFFERS_BOX = (By.XPATH, "//div[@data-testid='special-offers-box']")
    SPECIAL_OFFERS_HEADER = (By.XPATH, "//h4[normalize-space()='Special Offers']")
    SPECIAL_OFFERS_TOOLTIP_LINK = (By.XPATH,
                                   "//a[@data-analyticsid='SpecialOffersTooltipLink' and contains(text(),\"What's this?\")]")
    SPECIAL_OFFERS_ENTRY_PROMPT = (By.XPATH,
                                   "//p[contains(@class,'EntryPrompt') and contains(text(),'Enter promo or PIN code')]")
    SPECIAL_OFFERS_ENTRY_BOX = (By.XPATH, "//input[@id='code-entry']")
    SPECIAL_OFFERS_MESSAGE = (By.XPATH,
                              "//div[contains(@class,'styles__Message-@jarvis/react-smb-instant-ink-signup__w7xsxk-11')]")
    SPECIAL_OFFERS_APPLY_BUTTON = (By.XPATH, "//button[@name='Apply' and @data-analyticsid='SpecialOffersApplyButton']")
    INVALID_CODE_MESSAGE = (By.XPATH, "//p[normalize-space()='Oops! Invalid code. Please try again.']")
    PROMOTION_ICON_MESSAGE = (By.CSS_SELECTOR, "div[class*='IconMessage']")
    PROMOTION_ICON = (By.CSS_SELECTOR, "div[class*='IconMessage'] svg")
    PROMOTION_TEXT = (By.XPATH, "//div[contains(@class, 'styles__IconMessage')]//p[text()='Promotion Applied.']")
    REQUIRED_BILLING_TEXT = (By.XPATH,"//p[contains(@class, 'styles__RequireBilling') and contains(text(), 'A payment method is needed on file')]")
    PROMOTION_TEXT = (By.CSS_SELECTOR, "div[class*='IconMessage'] p")
    SPECIAL_OFFERS_ENTER_PROMOCODE = (By.XPATH,"//*[contains(text(),'Enter promo or PIN code')]")
    MULTI_PROMOTION_TEXT = (By.XPATH, "//div[contains(@class, 'styles__IconMessage')]//p[text()='Multiple Promotions Applied.']")
    SPECIAL_PURL_OFFER_FREE_MONTHS_LANDING_PAGE = (By.XPATH,"//*[starts-with(text(), 'Congratulations! You have')]")
    SPECIAL_PURL_OFFER_FREE_MONTHS_OFFER_REDEEMED_TEXT = (By.XPATH,"//*[starts-with(text(), '6')]")
    SPECIAL_PURL_OFFER_FREE_MONTHS_SEE_DETAILS_TEXT = (By.XPATH,"//a[@data-analyticsid='BenefitsTooltipLink']")
    PROMO_CODE_MONTHS_CONTAINER = (By.CSS_SELECTOR, "div[data-testid='promo-code-months']")
    PROMO_CODE_LABEL = (By.XPATH,
                        "//div[@data-testid='promo-code-months']//div[contains(@class,'BenefitName')]//p[text()='Promo Code']")
    PROMO_CODE_MONTHS_TEXT = (By.XPATH, "//div[@data-testid='promo-code-months']//div/p[not(text()='Promo Code')]")
    PROMO_CODE_POPUP_FREE_MONTHS = (By.XPATH,"//div[@data-testid='promo-code-months']//div[contains(@class,'BenefitName')]//following-sibling::div//p[contains(text(),'months')]")
    PROMO_CODE_BENEFITS = (By.XPATH,"//*[@data-analyticsid='BenefitsTooltipLink']")
    SPECIAL_PURL_OFFER_PREPAID_MESSAGE= (By.XPATH,"//div[@id='purl_reward_container']/div[2]/img/following-sibling::h1/following-sibling::h4")
    SPECIAL_PURL_OFFER_PREPAID_CONGRAT_MESSAGE= (By.XPATH,"//h1[contains(text(),'Congratulations!')]")
    SPECIAL_PURL_OFFER_PREPAID_ENROLL_NOW= (By.XPATH,"//*[contains(text(),'Enroll Now')]")
    REQUIRE_BILLING_ICON_MESSAGE = (By.CSS_SELECTOR,"div[class*='IconMessage']")
    REQUIRE_BILLING_ICON = (By.CSS_SELECTOR,"div[class*='IconMessage'] svg")
    REQUIRE_BILLING_TEXT = (By.CSS_SELECTOR,"p[class*='RequireBilling']")
    BREAKDOWN_TITLE_CONTAINER = (By.CSS_SELECTOR,"div[class*='BreakdownTitle']")
    BREAKDOWN_TITLE_TEXT = (By.XPATH,"//div[contains(@class,'BreakdownTitle')]//div[text()='Breakdown of credits']")
    BREAKDOWN_PROMO_TEXT= (By.XPATH,"//*[@class='styles__BenefitsBreakdown-@jarvis/react-smb-instant-ink-signup__sc-1sl6jwf-1 fVfVnb']")
    ENROLLMENT_KEY_MONTHS_CONTAINER = (By.CSS_SELECTOR, "div[data-testid='enrollment-key-months']")
    ENROLLMENT_KEY_LABEL = (By.XPATH,
                            "//div[@data-testid='enrollment-key-months']//div[contains(@class,'BenefitName')]//p[text()='Enrollment Key']")
    ENROLLMENT_KEY_MONTHS_TEXT = (By.XPATH,
                                  "//div[@data-testid='enrollment-key-months']//div/p[not(text()='Enrollment Key')]")
    PREPAID_CONTAINER = (By.XPATH, "div[data-testid='prepaid-balance-currency']")
    PREPAID_CODE_LABEL = (By.XPATH,
                          "//div[@data-testid='prepaid-balance-currency']//div[contains(@class,'BenefitName')]//p[text()='Prepaid credits']")
    PREPAID_CREDITS_TEXT = (By.XPATH,
                            "//div[@data-testid='prepaid-balance-currency']//div/p[not(text()='Prepaid credits')]")
    FREE_TRIAL_MONTHS_CONTAINER = (By.XPATH, "//div[@data-testid='free-trial-months']")
    FREE_TRIAL_LABEL = (By.XPATH,
                        "//div[@data-testid='free-trial-months']//div[contains(@class,'BenefitName')]//p[text()='Free Trial']")
    FREE_TRIAL_MONTHS_TEXT = (By.XPATH, "//div[@data-testid='free-trial-months']//div/p[not(text()='Free Trial')]")
    ERROR_MESSAGE_CONTAINER = (By.XPATH, "//div[contains(@class, 'styles__Message') and @result='error']")
    ERROR_ICON_MESSAGE = (By.XPATH, "//div[contains(@class, 'styles__IconMessage')]")
    ERROR_ICON = (By.XPATH,
                  "//div[contains(@class, 'styles__IconMessage')]//svg[contains(@class, 'styles__MinusCircleIcon')]")
    ERROR_TEXT = (By.XPATH,
                  "//div[contains(@class, 'styles__IconMessage')]//p[contains(text(), 'Oops! This code has expired.')]")
    CLOSE_SOB_MODAL = (By.XPATH, "//button[@aria-label='Close modal' and not(ancestor::*[@aria-hidden='true'])]") 


class EnrollmentPageLocators:
    START_BUTTON = (By.XPATH, "//button[text()='Start Enrollment']")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Continue']")
    SHIPPING_ADDRESS_INPUT = (By.NAME, "shippingAddress")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Submit']")


class SpecialOfferModalLocators:
    EK_CODE_INPUT = (By.ID, "ek-code")
    APPLY_BUTTON = (By.XPATH, "//button[text()='Apply']")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".toast-success")
    NOTIFICATION_MESSAGE = (By.XPATH, "//*[contains(text(),'payment method is needed')]")
    CREDITS_BREAKDOWN_SECTION = (By.CSS_SELECTOR, ".credits-breakdown")
    CODE_NAME_TEXT = (By.XPATH, "//div[contains(@class, 'code-name')]")
    TRIAL_MONTHS_TEXT = (By.XPATH, "//div[contains(@class, 'trial-months')]")

class ShippingBillingPageLocators:
    PRE_ENROLL_CARDS_CONTAINER = (By.XPATH, "//div[contains(@class,'PreEnrollCards')]")
    # Shipping Card
    SHIPPING_CARD = (By.XPATH, "//div[@data-testid='shipping-card']")
    SHIPPING_CARD_TITLE = (By.XPATH, "//h6[normalize-space()='Shipping']")
    SHIPPING_CARD_DESCRIPTION = (By.XPATH, "//p[contains(text(),'Let us know where to ship your ink.')]")
    ADD_SHIPPING_BUTTON = (By.XPATH, "//button[@data-testid='add-shipping']")
    # Billing Card
    BILLING_CARD = (By.XPATH, "//div[@data-testid='billing-card']")
    BILLING_CARD_TITLE = (By.XPATH, "//h6[normalize-space()='Billing']")
    BILLING_CARD_TOOLTIP = (By.XPATH, "//svg[@data-analyticsid='billing-card-tooltip']")
    BILLING_CARD_DESCRIPTION = (By.XPATH, "//p[contains(text(),'Please enter your billing information.')]")
    ADD_BILLING_BUTTON = (By.XPATH, "//button[@data-testid='add-billing']")
    APPLY_PROMOTION_BUTTON = (By.XPATH, "//button[@data-testid='apply-promotion-button']")
    BILLING_CARD_TEXT = (By.XPATH,"//*[contains(@class, 'Description')]/p")
    # Benefits and summary section
    BENEFITS_HEADER = (By.XPATH, "//p[@data-testid='benefits-header']")
    #see details link
    BENEFITS_TOOLTIP_LINK = (By.XPATH, "//a[@data-analyticsid='BenefitsTooltipLink']")
    SUMMARY_SECTION = (By.XPATH, "//div[@data-testid='summary-section']")
    ITEMIZED_PRODUCT_INFO = (By.XPATH, "//div[@data-testid='itemized-product-info']")
    PRODUCT_AND_PRICE = (By.XPATH, "//div[contains(@class,'ProductAndPrice')]//p[1]")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class,'ProductAndPrice')]//p[contains(@class,'Price')]")
    PLAN_TRIAL_PRODUCT_AND_PRICE = (By.XPATH, "//div[contains(@class,'PlanTrialProductAndPrice')]//p")
    TOTAL_NOW_SECTION = (By.XPATH, "//div[contains(@class,'TotalNow')]")
    TOTAL_NOW_LABEL = (By.XPATH, "//div[contains(@class,'TotalNow')]//p[1]")
    #TOTAL_NOW_PRICE = (By.XPATH, "//div[contains(@class,'TotalNowPrice')]")
    TOTAL_AFTER_TRIAL_SECTION = (By.XPATH, "//div[@data-testid='total-after-trial']")
    TOTAL_AFTER_TRIAL_LABEL = (By.XPATH, "//div[@data-testid='total-after-trial']//p[1]")
    #TOTAL_AFTER_TRIAL_PRICE = (By.XPATH, "//div[contains(@class,'TotalAfterTrialPrice')]")
    INK_TRIAL_TEXT = (By.XPATH,
                      "//div[@data-testid='itemized-product-info']//div[contains(@class,'styles__InkPaperTrial')]//p[contains(text(),'ink trial')]")
    PAPER_TRIAL_TEXT = (By.XPATH,
                        "//div[@data-testid='itemized-product-info']//div[contains(@class,'styles__InkPaperTrial')]//p[contains(text(),'paper trial')]")
    #Change Plan
    CHANGE_PLAN =(By.XPATH,"//button[@data-testid='edit-plan']//span[contains(@class, 'css-hq5xek-icon')]")
    #Contuine to Enroll
    CONTINUE_TO_ENROLL= (By.XPATH,"//button[@data-testid='printer-enroll-continue-button']")
    #Contuine to Enroll without printer
    CONTINUE_TO_ENROLL_BTN= (By.XPATH,"//*[@data-testid='preenroll-continue-button']")
    TOTAL_AFTER_TRIAL_PRICE = (By.XPATH, "//p[contains(@class,'TotalAfterTrialPrice')]")
    TOTAL_NOW_PRICE = (By.XPATH, "//p[contains(@class,'TotalNowPrice')]")


class AddShippingPageLocators:
    SHIPPING_CONTENT_CONTAINER = (By.XPATH, "//form[@id='shipping-content-container']")
    ADD_SHIPPING_ADDRESS_HEADING = (By.XPATH, "//h4[normalize-space()='Add Shipping Address']")

    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='last-name']")
    COMPANY_INPUT = (By.XPATH, "//input[@id='company']")
    MOBILE_NUMBER_INPUT = (By.XPATH, "//input[@id='phoneNumberSmall']")

    STREET1_INPUT = (By.XPATH, "//input[@id='street1']")
    STREET2_INPUT = (By.XPATH, "//input[@id='street2']")
    CITY_INPUT = (By.XPATH, "//input[@id='city']")

    STATE_COMBOBOX = (By.XPATH, "//div[@data-testid='state']")
    STATE_COMBOBOX_OPEN = (By.XPATH, "//div[@data-testid='state']//div[@aria-label='Open']")

    ZIP_CODE_INPUT = (By.XPATH, "//input[@id='zip-code']")
    COUNTRY_INPUT = (By.XPATH, "//input[@id='country']")

    TEXT_MESSAGE_OPTION_CHECKBOX = (By.XPATH, "//span[contains(@class,'vn-checkbox__span')]")

    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='cancel-button']")
    SAVE_BUTTON = (By.XPATH, "//button[@data-testid='save-button']")
    EDIT_SHIPPING_BUTTON = (By.XPATH, "//button[@data-testid='edit-shipping']")
    SHIP_TO_THIS_ADDRESS_BUTTON= (By.XPATH, "//button[contains(normalize-space(text()), 'Ship to this address')]")


    @staticmethod
    def STATE_BY_TEXT(state_name):
        return (By.XPATH, f"//ul[@id='state-listbox']/li[normalize-space()='{state_name}']")

class BillingInformationPageLocators:
    BILLING_TITLE = (By.XPATH, "//h2[normalize-space()='Billing']")
    STEP_INDICATOR = (By.XPATH, "//span[contains(@class,'StyledStepNumber')]")
    STEP_TITLE = (By.XPATH, "//span[contains(@class,'StyledStepTitle')]")
    CONSUMER_RADIO_BUTTON = (By.XPATH, "//input[@data-testid='consumer-radio-button']/following::span")
    BUSINESS_RADIO_BUTTON = (By.XPATH, "//input[@data-testid='business-radio-button']/following::span")
    CREDIT_CARD_RADIO_BUTTON = (By.XPATH, "//input[@data-testid='credit-card-radio-button']/following::span")
    CREDIT_CARD_ICON = (By.XPATH, "//svg[@data-testid='credit-card-icon']")
    GPAY_ICON = (By.XPATH, "//svg[@data-testid='gpay-icon']")
    PAYPAL_ICON = (By.XPATH, "//img[@data-testid='paypal-icon']")
    USE_SHIPPING_ADDRESS_CHECKBOX = (By.XPATH, "(//input[@id='use-shipping-address']/following-sibling::span[contains(@class,'checkbox')])[1]")
    USE_SHIPPING_ADDRESS_LABEL = (By.XPATH, "//label[@for='use-shipping-address']//span[contains(text(),'Same as shipping address')]")
    ADDRESS_PREVIEW_CARD = (By.XPATH, "//div[@data-testid='address-preview-card']")
    ADDRESS_PREVIEW_FULL_NAME = (By.XPATH, "//p[contains(@class,'StyledFullName')]")
    ADDRESS_PREVIEW_DETAIL = (By.XPATH, "//p[contains(@class,'StyledShippingCardDetail')]")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='cancel-button']")
    CONTINUE_BUTTON = (By.XPATH, "//button[@data-testid='continue-button']")

    # Payment Options & Iframes
    BACK_BUTTON_PAYMENT = (By.XPATH, "//button[@data-testid='previous-screen-button']")
    GPAY_BUTTON = (By.XPATH, "//div[@data-testid='gpay-button']")
    GPAY_IFRAME = (By.XPATH, "//iframe[@id='pgs-gpay-iframe']")
    PAYPAL_BUTTON = (By.XPATH, "//div[@data-testid='paypal-button']")
    PAYPAL_WEB_BUTTON_FRAME = (By.XPATH, "//div[@data-testid='web-paypal-express']")
    PAYPAL_IFRAME = (By.XPATH, "//iframe[contains(@class,'zoid-component-frame')]")
    OR_SECTION_SEPARATOR = (By.XPATH, "//div[contains(@class,'OrSection')]//span[normalize-space()='or']")
    PGS_FORM_SECTION = (By.XPATH, "//div[contains(@class,'PgsFormSection')]")
    PGS_IFRAME = (By.XPATH, "//iframe[@id='pgs-iframe']")

class BillingPageLocators:
    # Step and Title
    STEP_NUMBER = (By.XPATH, "//span[contains(@class,'StyledStepNumber') and contains(text(),'Step 2 of 2')]")
    STEP_TITLE = (By.XPATH, "//span[contains(@class,'StyledStepTitle') and contains(text(),'Complete your payment.')]")

    # Google Pay
    GPAY_BUTTON_CONTAINER = (By.XPATH, "//div[@data-testid='gpay-button']")
    GPAY_IFRAME = (By.XPATH, "//iframe[@id='pgs-gpay-iframe']")

    # PayPal
    PAYPAL_BUTTON_CONTAINER = (By.XPATH, "//*[@data-testid='paypal-button']")
    PAYPAL_WEB_BUTTON_FRAME = (By.XPATH, "//div[@data-testid='web-paypal-express']")
    PAYPAL_IFRAME = (By.XPATH, "//iframe[contains(@class,'zoid-component-frame')]")

    # Or Section
    OR_SECTION = (By.XPATH, "//div[contains(@class,'OrSection')]//span[normalize-space()='or']")

    # PGS Form Section
    PGS_FORM_SECTION = (By.XPATH, "//div[contains(@class,'PgsFormSection')]")
    PGS_IFRAME = (By.XPATH, "//iframe[@id='pgs-iframe']")

    # Card Number
    CARD_NUMBER_INPUT = (By.XPATH, "//input[@id='txtCardNumber']")
    CARD_NUMBER_LABEL = (By.XPATH, "//label[@for='txtCardNumber']")
    CARD_NUMBER_WARNING = (By.ID, "errormsg_BinCheck")

    # Card Type Images
    VISA_IMG = (By.ID, "imgVI")
    MASTERCARD_IMG = (By.ID, "imgMC")
    AMEX_IMG = (By.ID, "imgAX")
    DISCOVER_IMG = (By.ID, "imgDI")

    # Expiration
    EXP_MONTH_SELECT = (By.XPATH, "//select[@id='drpExpMonth']")
    EXP_MONTH_LABEL = (By.XPATH, "//label[@for='drpExpMonth']")
    EXP_YEAR_SELECT = (By.XPATH, "//select[@id='drpExpYear']")
    EXP_YEAR_LABEL = (By.XPATH, "//label[@for='drpExpYear']")

    # CVV
    CVV_INPUT = (By.XPATH, "//input[@id='txtCVV']")
    CVV_LABEL = (By.XPATH, "//label[@for='txtCVV']")
    CVV_INDICATOR_IMG = (By.XPATH, "//img[contains(@class,'cvv-indicator')]")

    # Error Message
    BILLING_ERROR_MESSAGE = (By.ID, "mp-message")

    # Next Button
    NEXT_BUTTON = (By.ID, "btn_pgs_card_add")

    # Overlay/Loading
    OVERLAY_DIV = (By.ID, "divOverLay")
    BILLING_ERROR_TEXT = (By.XPATH, "//div[@id='mp-message']//p[@class='text-danger']")
    BILLING_ERROR_SUB_MSG = (By.ID, "mp-sub-msg")


class SpecialOffersLocators:
    # Container / header
    SPECIAL_OFFERS_BOX = (By.XPATH, "//div[@data-testid='special-offers-box']")
    SPECIAL_OFFERS_HEADER = (By.XPATH, "//h4[normalize-space()='Special Offers']")
    SPECIAL_OFFERS_ENTER_PROMOCODE = (By.XPATH, "//*[contains(text(),'Enter promo or PIN code')]")
    CLOSE_SOB_MODAL = (By.XPATH, "//button[@aria-label='Close modal' and not(ancestor::*[@aria-hidden='true'])]")

    # Entry / action
    INPUT_FIELD = (By.XPATH, "//input[@id='code-entry']")
    APPLY_BUTTON = (By.XPATH, "//button[@name='Apply' and @data-analyticsid='SpecialOffersApplyButton']")

    # Messages / toast / icon
    PROMOTION_ICON = (By.CSS_SELECTOR, "div[class*='IconMessage'] svg")
    PROMOTION_TEXT = (By.XPATH, "//div[contains(@class, 'styles__IconMessage')]//p[text()='Promotion Applied.']")
    PROMOTION_TEXT_ERROR = (By.CSS_SELECTOR, "div[class*='IconMessage'] p")
    SPECIAL_OFFERS_MESSAGE = (By.XPATH, "//div[contains(@class,'styles__Message-')]" )

    # Specific user-visible messages
    INVALID_CODE_MESSAGE = (By.XPATH, "//p[normalize-space()='Oops! Invalid code. Please try again.']")
    DUPLICATE_CODE_MESSAGE = (By.XPATH, "//p[normalize-space()='Oops! This Prepaid key has already been used.']")
    REQUIRED_BILLING_TEXT = (By.XPATH,"//p[contains(@class, 'styles__RequireBilling') and contains(text(), 'A payment method is needed on file')]")

    # Promo breakdown / benefits
    PROMO_CODE_MONTHS_CONTAINER = (By.CSS_SELECTOR, "div[data-testid='promo-code-months']")
    PROMO_CODE_MONTHS_TEXT = (By.XPATH, "//div[@data-testid='promo-code-months']//div/p[not(text()='Promo Code')]")
    PROMO_CODE_LABEL = (By.XPATH, "//div[@data-testid='promo-code-months']//div[contains(@class,'BenefitName')]//p[text()='Promo Code']")

    ENROLLMENT_KEY_MONTHS_CONTAINER = (By.CSS_SELECTOR, "div[data-testid='enrollment-key-months']")
    ENROLLMENT_KEY_MONTHS_TEXT = (By.XPATH, "//div[@data-testid='enrollment-key-months']//div/p[not(text()='Enrollment Key')]")
    PREPAID_CONTAINER = (By.XPATH, "div[data-testid='prepaid-balance-currency']")
    PREPAID_CREDITS_TEXT = (By.XPATH, "//div[@data-testid='prepaid-balance-currency']//div/p[not(text()='Prepaid credits')]")

    # Breakdown / UI helpers
    BREAKDOWN_TITLE_CONTAINER = (By.CSS_SELECTOR,"div[class*='BreakdownTitle']")
    BREAKDOWN_PROMO_TEXT = (By.XPATH,"//*[contains(@class, 'styles__BenefitsBreakdown') or @data-testid='prepaid-balance-currency']")

    # Generic error box (icon + text)
    ERROR_MESSAGE_CONTAINER = (By.XPATH, "//div[contains(@class, 'styles__Message') and @result='error']")
    ERROR_ICON_MESSAGE = (By.XPATH, "//div[contains(@class, 'styles__IconMessage')]")
    ERROR_TEXT = (By.XPATH, "//div[contains(@class, 'styles__IconMessage')]//p[contains(text(), 'Oops! This code has expired.')]")

    # PURL / special offer landing elements (kept but optional)
    SPECIAL_PURL_OFFER_FREE_MONTHS_LANDING_PAGE = (By.XPATH,"//*[starts-with(text(), 'Congratulations! You have')]")
    SPECIAL_PURL_OFFER_FREE_MONTHS_OFFER_REDEEMED_TEXT = (By.XPATH,"//*[starts-with(text(), '6')]")
    SPECIAL_PURL_OFFER_FREE_MONTHS_SEE_DETAILS_TEXT = (By.XPATH,"//a[@data-analyticsid='BenefitsTooltipLink']")
    SPECIAL_PURL_OFFER_PREPAID_ENROLL_NOW = (By.XPATH,"//*[contains(text(),'Enroll Now')]")


class DeepLinkLocators:
    # URL validation
    EXPECTED_URL_SUBSTRING = "instantink-pre-enroll/connect"

    # Button locator
    CONNECT_PRINTER_LATER = (
        By.XPATH,
        "//div//button//span[normalize-space(text())='Connect Printer Later']"
    )

class EnrollmentLocators:
    # Continue to Enroll button
    CONTINUE_TO_ENROLL = (
        By.XPATH,
        "//button[@data-testid='printer-enroll-continue-button']"
        "|//*[@data-testid='preenroll-continue-button']"
    )

class Cookies:
    # accept cookies
    ACCEPT_COOKIES_BUTTON = (
            By.XPATH, "//button[@id='onetrust-accept-btn-handler']")