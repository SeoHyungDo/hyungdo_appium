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

class TestMainpage(passclass):

    def test_login_hamburger_menu_check(self):
        self.swag_home.login()
        assert self.swag_home.hamburger_menu_icon.is_displayed()

    def test_hamburger_menu_all_items_text(self):
        self.swag_home.hamburger_menu_icon.click()
        assert self.swag_home.menu_all_items_text == "ALL ITEMS"

    def test_hamburger_menu_webview_text(self):
        assert self.swag_home.menu_webview_text == "WEBVIEW"

    def test_hamburger_menu_qr_code_scanner_text(self):
        assert self.swag_home.menu_qr_text == "QR CODE SCANNER"

    def test_hamburger_menu_geo_location_text(self):
        assert self.swag_home.menu_geo_text == "GEO LOCATION"

    def test_hamburger_menu_Drawing_text(self):
        assert self.swag_home.menu_drawing_text == "DRAWING"

    def test_hamburger_menu_about_text(self):
        assert self.swag_home.menu_about_text == "ABOUT"

    def test_hamburger_menu_logout_text(self):
        assert self.swag_home.menu_logout_text == "LOGOUT"

    def test_hamburger_menu_reset_app_state_text(self):
        assert self.swag_home.menu_reset_text == "RESET APP STATE"

    def test_top_logo_display(self):
        assert self.swag_home.top_logo.is_displayed()

    def test_cart_button_display(self):
        assert self.swag_home.cart_button.is_displayed()

    def test_product_text(self):
        assert self.swag_home.product_text_check == "PRODUCTS"

    def test_text_modal_selector_button_check(self):
        assert self.swag_home.text_modal_selector_button.is_displayed()

    def test_first_product_image_display(self):
        assert self.swag_home.first_product_image_displayed.is_displayed()