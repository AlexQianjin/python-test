from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from . import config

def get_driver():
    if config.BROWSER == 'chrome':
        driver = webdriver.Chrome()

        return driver


def get_element_by_id(driver, id, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        lambda x: x.find_element_by_id(id))

    return element


def get_element_by_name(driver, name, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        lambda x: x.find_element_by_name(name))

    return element


def get_element_by_xpath(driver, xpath, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        lambda x: x.find_element_by_xpath(xpath))

    return element


def element_is_exist(driver, locator, timeout=10):
    flag = True
    try:
        element = WebDriverWait(driver, timeout).until(lambda x: x.find_element_by_xpath(locator))
        return flag
    except:
        flag = False
        return flag
