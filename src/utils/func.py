import os
import time
from . import action
from . import config
from . import locator

from dotenv import load_dotenv
load_dotenv()

def login(driver, url):
    action.maximize_window(driver)
    action.open_url(driver, url)
    time.sleep(5)

    username = os.getenv('TEST_USERNAME')
    password = os.getenv('TEST_PASSWORD')
    index = username.lower().find('@aveva.com')
    if index == -1:
        action.input_text(driver, 'id', locator.loginUsername, username)
        time.sleep(1)
        action.input_text(driver, 'id', locator.loginPassword, password)
        time.sleep(1)
        action.click(driver, 'id', locator.loginSubmit)
    else:
        # Login to AVEVA Cloud Traning Center with aveva account
        action.input_text(driver, 'id', locator.loginUsername, username)
        action.click(driver, 'id', locator.loginSubmit)
        time.sleep(3)
        action.input_text(driver, 'id', locator.loginAvevaPassword, password)
        action.click(driver, 'id', locator.loginAvevaSubmit)
        time.sleep(2)
        action.click(driver, 'id', locator.loginMicrosoftNo)
    time.sleep(5)

def admin_login(driver, url):
    action.maximize_window(driver)
    action.open_url(driver, url)
    time.sleep(5)

    username = os.getenv('ADMIN_USERNAME')
    password = os.getenv('ADMIN_PASSWORD')
    action.input_text(driver, 'id', locator.loginUsername, username)
    action.click(driver, 'id', locator.loginSubmit)
    time.sleep(3)
    action.input_text(driver, 'id', locator.loginAvevaPassword, password)
    action.click(driver, 'id', locator.loginAvevaSubmit)
    time.sleep(2)
    action.click(driver, 'id', locator.loginMicrosoftNo)
    time.sleep(5)

def student_login(driver, url):
    action.maximize_window(driver)
    action.open_url(driver, url)
    time.sleep(5)
    username = os.getenv('TEST_USERNAME')
    password = os.getenv('TEST_PASSWORD')
    action.click(driver, 'id', locator.loginUsername)
    action.input_text(driver, 'id', locator.loginUsername, username)
    action.input_text(driver, 'id', locator.loginPassword, password)
    action.click(driver, 'id', locator.loginSubmit)
    time.sleep(5)
