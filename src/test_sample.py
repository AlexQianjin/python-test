import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

def test_bing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://cn.bing.com')
    # element = driver.find_element_by_id('sb_form_q')
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('sb_form_q'))
    element.send_keys('Selenium' + Keys.RETURN)
    result_element = driver.find_element_by_xpath('/html/body/header/nav/ul/li[1]/a')
    result_element.get_attribute()
    result = result_element.text
    print(result)
    assert result == 'WEB'
