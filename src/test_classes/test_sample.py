import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from ..sikulix4python import *
from pathlib import WindowsPath

from ..utils import func
from ..utils import common
from ..utils import locator
from ..utils import action

def func_test(x):
    return x + 1

def test_answer():
    assert func_test(3) == 5

@pytest.mark.skip(reason="skip this case")
def test_bing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://cn.bing.com')
    # element = driver.find_element_by_id('sb_form_q')
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('sb_form_q'))
    element.send_keys('Selenium' + Keys.RETURN)
    result_element = driver.find_element_by_xpath('/html/body/header/nav/ul/li[1]/a')

    result = result_element.text
    print(result)
    assert result == 'WEB'

@pytest.mark.skip(reason="skip this case")
def test_view_activity():
    driver = common.get_driver()
    func.login(driver)
    assert 0

@pytest.mark.skip(reason="skip sikuliX demo case")
def test_sikuli4python():
    images_path = str(WindowsPath.joinpath(WindowsPath.cwd(), 'src', 'images'))
    print(images_path)

    addImagePath(images_path)

    openLink('https://cn.bing.com')

    screen = Screen()
    screen.getCenter()

    # a Match object is completely handled at the Java level
    # not defined at the Python level
    match = screen.exists('bing_input.png', 3.0) # number must be float/double
    print(match)
    if match:
        match.type("SikuliX")
        match.type(SXKey.ENTER)
    else:
        print('not match')
    assert 0

@pytest.mark.skip(reason="skip this case")
def test_launch_the_activity_page():
    driver = common.get_driver()
    func.admin_login(driver)
    action.click(driver, 'xpath', locator.courseAllCourses)
    # Click on next page
    action.click(driver, 'xpath', locator.coursePageNext)
    # Click on AVEVA SimLMS
    action.click(driver, 'xpath', locator.courseAVEVASimLMS)
    # Click on category QA
    action.click(driver, 'xpath', locator.courseCategoryAutomation)
    # Click on course
    action.click(driver, 'xpath', locator.courseTitleAutomationTestCourse)
    # Click on Activities
    action.click(driver, 'xpath', locator.courseActivities)
    action.click(driver, 'xpath', locator.instanceAutomationTestProjectActivity)
    launchButtonIsVisible = action.get_text(driver, 'xpath', locator.instanceLaunchButton)
    if launchButtonIsVisible:
        print("start to launch")
    else:
        action.click(driver, 'xpath', locator.courseActivities)
        action.click(driver, 'xpath',locator.instanceAutomationTestProjectActivity)
    # To launch instance
    action.click(driver, 'xpath', locator.instanceLaunchButton)
    # Get all window handles
    handles = driver.window_handles
    # switch to the new TAB
    driver.switch_to.window(handles[1])
    # Get tht new TAB url
    currentWinUrl = driver.current_url
    print('New window url:' + currentWinUrl)
    time.sleep(3)
    # Get the session ID
    sessionNo = action.get_text(driver, 'xpath', locator.instanceSessionNO)
    print('The sessin ID is :' + sessionNo)
    # Get session status
    sessionStatus = action.get_text(driver, 'id', locator.instanceSessionStatus)
    print('The sessin status is :' + sessionStatus)
    assert sessionStatus == 'STARTING'    