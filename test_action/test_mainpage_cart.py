import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from root_obj.login_page_obj import swaglabs_home
from utility.passclass import passclass
from root_obj import login_page_obj
from utility.wait import Wait
from root_obj.main_page_obj import swaglabs_main_page
from root_obj.cart_page_obj import cart_page

class Testcartpage(passclass):

    def test_first_product_remove_button_check(self):
        self.swag_home.login()
        self.swag_home.first_product_add_to_cart_button_el.click()
        assert self.cart.first_product_remove_button_text() == "REMOVE"

        self.swag_home.cart_locator_button_el_obj.click()

    def test_cart_hamburger_menu_check(self):
        assert self.cart.cart_hamburger_button_exist_check is not None

    #로딩이 너무 빨라 Fail이 나는 경우가 있어 명시적 대기 세팅
    def cart_menu_all_items_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.cart.cart_menu_all_items_locator
            )
        )
        return element.text

    def test_cart_hamburger_menu_all_items_text(self):
        self.cart.cart_hamburger_button_action.click()

        assert self.cart.cart_menu_all_items_text == "ALL ITEMS"

    def test_cart_hamburger_menu_webview_text(self):
        assert self.cart.cart_menu_webview_text == "WEBVIEW"

    def test_cart_hamburger_menu_qr_code_scanner_text(self):
        assert self.cart.cart_menu_qr_text == "QR CODE SCANNER"

    def test_cart_hamburger_menu_geo_location_text(self):
        assert self.cart.cart_menu_geo_text == "GEO LOCATION"

    def test_cart_hamburger_menu_drawing_text(self):
        assert self.cart.cart_menu_drawing_text == "DRAWING"

    def test_cart_hamburger_menu_about_text(self):
        assert self.cart.cart_menu_about_text == "ABOUT"

    def test_cart_hamburger_menu_logout_text(self):
        assert self.cart.cart_menu_logout_text == "LOGOUT"

    def test_cart_hamburger_menu_reset_app_state_text(self):
        assert self.cart.cart_menu_reset_text == "RESET APP STATE"

    def test_cart_top_logo_display(self):
        self.swag_home.close_menu_if_open()
        assert self.swag_home.top_logo.is_displayed()

    def test_cart_cart_button_display(self):
        assert self.swag_home.cart_button.is_displayed()