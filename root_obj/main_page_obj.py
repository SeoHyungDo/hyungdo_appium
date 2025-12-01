from http.client import responses
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from root_obj.login_page_obj import swaglabs_home
import time
from utility.wait import Wait

class swaglabs_main_page:

    def __init__(self, driver) :
        self.driver = driver

        self.hamburger_menu_locator = (AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-Menu"]/android.view.ViewGroup')
        self.top_logo_locator = (AppiumBy.XPATH,
                        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView[2]')

        self.input_Username_locator = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
        self.input_pw_locator = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
        self.login_button_locator = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

        self.exit_button_locator = (AppiumBy.ACCESSIBILITY_ID, 'test-Close')
        self.menu_all_items_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="ALL ITEMS"]')
        self.menu_webview_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="WEBVIEW"]')
        self.menu_qr_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="QR CODE SCANNER"]')
        self.menu_geo_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="GEO LOCATION"]')
        self.menu_drawing_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="DRAWING"]')
        self.menu_about_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="ABOUT"]')
        self.menu_logout_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="LOGOUT"]')
        self.menu_reset_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="RESET APP STATE"]')
        self.cart_locator = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart drop zone"]')
        self.product_text = (AppiumBy.XPATH, '//android.widget.TextView[@text="PRODUCTS"]')
        self.text_modal_selector = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Modal Selector Button"]')

        self.first_product_image = (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-Item"])[1]/android.view.ViewGroup/android.widget.ImageView')

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
    def hamburger_menu_icon(self):
        return self.driver.find_element(*self.hamburger_menu_locator)

    @property
    def menu_all_items(self):
        return self.driver.find_element(*self.menu_all_items_locator)

    @property
    def menu_all_items_text(self):
        return self.driver.find_element(*self.menu_all_items_locator).text

    @property
    def menu_webview(self):
        return self.driver.find_element(*self.menu_webview_locator)

    @property
    def menu_webview_text(self):
        return self.driver.find_element(*self.menu_webview_locator).text

    @property
    def menu_qr(self):
        return self.driver.find_element(*self.menu_qr_locator)

    @property
    def menu_qr_text(self):
        return self.driver.find_element(*self.menu_qr_locator).text

    @property
    def menu_geo(self):
        return self.driver.find_element(*self.menu_geo_locator)

    @property
    def menu_geo_text(self):
        return self.driver.find_element(*self.menu_geo_locator).text

    @property
    def menu_drawing(self):
        return self.driver.find_element(*self.menu_drawing_locator)

    @property
    def menu_drawing_text(self):
        return self.driver.find_element(*self.menu_drawing_locator).text

    @property
    def menu_close(self):
        return self.driver.find_element(*self.exit_button_locator)

    def close_menu_if_open(self):
        if self.driver.find_elements(*self.exit_button_locator):
            self.menu_close.click()

    @property
    def menu_about(self):
        return self.driver.find_element(*self.menu_about_locator)

    @property
    def menu_about_text(self):
        return self.driver.find_element(*self.menu_about_locator).text

    @property
    def menu_logout(self):
        return self.driver.find_element(*self.menu_logout_locator)

    @property
    def menu_logout_text(self):
        return self.driver.find_element(*self.menu_logout_locator).text

    @property
    def menu_reset(self):
        return self.driver.find_element(*self.menu_reset_locator)

    @property
    def menu_reset_text(self):
        return self.driver.find_element(*self.menu_reset_locator).text

    @property
    def top_logo(self):
        return self.driver.find_element(*self.top_logo_locator)

    @property
    def cart_button(self):
        return self.driver.find_element(*self.cart_locator)

    def cart_button_click(self):
        if self.driver.find_element(*self.cart_button) :
            self.cart_button.click()

    @property
    def product_text_check(self):
        return self.driver.find_element(*self.product_text).text

    @property
    def text_modal_selector_button(self):
        return self.driver.find_element(*self.text_modal_selector)

    def text_modal_selector_button_click(self):
        if self.driver.find_element(*self.text_modal_selector_button) :
            self.text_modal_selector_button.click()


    @property
    def first_product_image_displayed(self):
        return self.driver.find_element(*self.first_product_image)