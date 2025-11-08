# Thin helper showing how to reuse driver's wait implementation if needed
def wait_for_visible(driver, locator_type, locator_value, timeout=10):
    driver.wait_for_element(locator_type, locator_value, timeout=timeout)
