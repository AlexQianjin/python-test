import os
import action
import config
import locator

from dotenv import load_dotenv
load_dotenv()

def login(driver):
    action.maximize_window(driver)
    action.open_url(driver, config.TEST_ENV_URL)

    username = os.getenv('TEST_USERNAME')
    password = os.getenv('TEST_PASSWORD')
