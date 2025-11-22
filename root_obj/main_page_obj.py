from http.client import responses
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from root_obj.login_page_obj import swaglabs_home
import time

class swaglabs_main_page:

    def __init__(self, driver) :
        self.driver = driver

        self.hamburger_menu_locator = (AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-Menu"]/android.view.ViewGroup')

        self.input_Username_locator = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
        self.input_pw_locator = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
        self.login_button_locator = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

    @property
    def input_Username(self):
        return self.driver.find_element(*self.input_Username_locator)

    @property
    def input_pw(self):
        return self.driver.find_element(*self.input_pw_locator)

    @property
    def login_button(self):
        return self.driver.find_element(*self.login_button_locator)

    def login(self):
        self.input_Username.click()
        self.input_Username.clear()
        self.input_Username.send_keys("standard_user")

        self.input_pw.click()
        self.input_pw.clear()
        self.input_pw.send_keys("secret_sauce")
        self.login_button.click()

    @property
    def hamburger_menu(self):
        return self.driver.find_element(*self.hamburger_menu_locator)