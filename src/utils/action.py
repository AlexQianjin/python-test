from . import common

locator_method_dict = {'id': common.get_element_by_id, 'name': common.get_element_by_name, 'xpath': common.get_element_by_xpath}

def open_url(driver, url):
    driver.get(url)

def maximize_window(driver):
    driver.maximize_window()

def click(driver, by, locator, timeout = 10 * 1000):
    element = locator_method_dict[by](driver, locator, timeout)
    element.click()

    return element

def input_text(driver, by, locator, txt, timeout = 10 * 1000):
    element = locator_method_dict[by](driver, locator, timeout)
    element.clear()
    element.send_keys(txt)

    return element

def get_text(driver, by, locator, timeout = 10 * 1000):
    element = locator_method_dict[by](driver, locator, timeout)
    value = element.text

    return value

def get_attribute_value(driver, by, locator, timeout = 10 * 1000):
    element = locator_method_dict[by](driver, locator, timeout)
    value = element.get_attribute('value')

    return value