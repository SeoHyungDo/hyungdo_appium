from http.client import responses
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class swaglabs_home:

    def __init__(self, driver):
        self.driver = driver

        self.input_id_locator = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
        self.input_pw_locator = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
        self.login_button_locator = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

        self.login_err_msg_locator = (AppiumBy.XPATH, '//*[@content-desc="test-Error message"]/*') # /* 를 붙여야 부모 요소 밑의 자식 텍스트를 읽음

    def login_err_msg_text(self):
        return self.driver.find_element(*self.login_err_msg_locator).text

    @property
    def login_button(self):
        return self.driver.find_element(*self.login_button_locator)

    @property
    def input_id(self):
        return self.driver.find_element(*self.input_id_locator)

    @property
    def input_pw(self):
        return self.driver.find_element(*self.input_pw_locator)