from http.client import responses
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class cart_page:


    def __init__(self, driver):
        self.driver = driver

        self.first_product_remove = (AppiumBy.XPATH, '//android.widget.TextView[@text="REMOVE"]')

    @property
    def first_product_remove_button(self):
        return self.driver.find_element(*self.first_product_remove)

    def first_product_remove_button_text(self):
        return self.first_product_remove_button.text