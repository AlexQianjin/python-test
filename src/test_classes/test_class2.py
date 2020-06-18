import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from ..sikulix4python import *
from pathlib import WindowsPath

from ..utils import func
from ..utils import common


@pytest.fixture(scope='class')
def driver_init(request):
    web_driver = webdriver.Chrome()
    print('driver init')
    request.cls.driver = web_driver

    images_path = str(WindowsPath.joinpath(WindowsPath.cwd(), 'src', 'images'))
    print(images_path)
    addImagePath(images_path)
    yield
    print('quit driver')
    web_driver.quit()


@pytest.mark.usefixtures('driver_init')
class BasicChromeTest:
    pass


class TestClass2(BasicChromeTest):
    def test_bing(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://cn.bing.com')
        # element = driver.find_element_by_id('sb_form_q') //*[@id="b-scopeListItem-web"]/a
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('sb_form_q'))
        element.send_keys('Selenium' + Keys.RETURN)
        result_element = driver.find_element_by_xpath('/html/body/header/nav/ul/li[1]/a')
        result = result_element.text
        print(result)
        assert result == 'WEB'

    def test_bing2(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://cn.bing.com')
        time.sleep(3)

        screen = Screen()
        screen.getCenter()
        match = screen.exists('bing_input.png', 3.0)  # number must be float/double
        print(match)
        if match:
            match.type("SikuliX")
            match.type(SXKey.ENTER)
        else:
            print('not match')
        time.sleep(3)
        result_element = driver.find_element_by_xpath('//*[@id="b-scopeListItem-images"]/a')
        result = result_element.text
        print(result)
        assert result == 'IMAGES'

    def test_bing_search(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://cn.bing.com')
        time.sleep(3)
        screen = Screen()
        screen.getCenter()
        match = screen.exists('bing_input.png', 3.0)  # number must be float/double
        print(match)
        if match:
            match.type("SikuliX")
            # time.sleep(3)
            match_search = screen.exists('bing_search.png', 3.0)
            if match_search:
                match_search.click()
            else:
                print('search not found')
        else:
            print('not match')
        time.sleep(3)
        result_element = driver.find_element_by_xpath('//*[@id="b-scopeListItem-images"]/a')
        result = result_element.text
        print(result)
        assert result == 'IMAGES'
