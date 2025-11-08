class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator_type, locator_value):
        self.driver.wait_for_element(locator_type, locator_value)
        self.driver.click(locator_type, locator_value)

    def enter_text(self, locator_type, locator_value, text):
        self.driver.wait_for_element(locator_type, locator_value)
        self.driver.send_keys(locator_type, locator_value, text)

    def get_text(self, locator_type, locator_value):
        el = self.driver.find_element(locator_type, locator_value)
        return el.text if el else None
