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
        self.swag_home.close_menu_if_open()
        assert self.swag_home.top_logo.is_displayed()

    def test_cart_button_display(self):
        assert self.swag_home.cart_button.is_displayed()

    def test_product_text(self):
        assert self.swag_home.product_text_check == "PRODUCTS"

    def test_text_modal_selector_button_check(self):
        assert self.swag_home.text_modal_selector_button.is_displayed()

    # -----------------------------
    # 1st product - Sauce Labs Backpack
    # -----------------------------
    def test_first_product_image_display(self):
        self.swag_home.scroll_until_text("Sauce Labs Backpack")
        assert self.swag_home.first_product_image_displayed.is_displayed()

    def test_first_product_name_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Backpack")
        assert self.swag_home.first_product_name_text == "Sauce Labs Backpack"

    def test_first_product_price_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Backpack")
        assert self.swag_home.first_product_price_text == "$29.99"

    def test_first_product_add_to_cart_button_text_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Backpack")
        assert self.swag_home.first_product_add_to_cart_button_click_obj.text == "ADD TO CART"

    # -----------------------------
    # 2nd product - Sauce Labs Bike Light
    # -----------------------------
    def test_second_product_image_display(self):
        self.swag_home.scroll_until_text("Sauce Labs Bike Light")
        assert self.swag_home.second_product_image_displayed.is_displayed()

    def test_second_product_name_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Bike Light")
        assert self.swag_home.second_product_name_text == "Sauce Labs Bike Light"

    def test_second_product_price_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Bike Light")
        assert self.swag_home.second_product_price_text == "$9.99"

    def test_second_product_add_to_cart_button_text_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Bike Light")
        assert self.swag_home.second_product_add_to_cart_button_click_obj.text == "ADD TO CART"

    # -----------------------------
    # 3rd product - Sauce Labs Bolt T-Shirt
    # -----------------------------
    def test_third_product_image_display(self):
        self.swag_home.scroll_until_text("Sauce Labs Bolt T-Shirt")
        assert self.swag_home.third_product_image_displayed.is_displayed()

    def test_third_product_name_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Bolt T-Shirt")
        assert self.swag_home.third_product_name_text == "Sauce Labs Bolt T-Shirt"

    def test_third_product_price_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Bolt T-Shirt")
        assert self.swag_home.third_product_price_text == "$15.99"

    def test_third_product_add_to_cart_button_text_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Bolt T-Shirt")
        assert self.swag_home.third_product_add_to_cart_button_click_obj.text == "ADD TO CART"

    # -----------------------------
    # 4th product - Sauce Labs Fleece Jacket
    # -----------------------------
    def test_fourth_product_image_display(self):
        self.swag_home.scroll_until_text("Sauce Labs Fleece Jacket")
        assert self.swag_home.fourth_product_image_displayed.is_displayed()

    def test_fourth_product_name_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Fleece Jacket")
        assert self.swag_home.fourth_product_name_text == "Sauce Labs Fleece Jacket"

    def test_fourth_product_price_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Fleece Jacket")
        assert self.swag_home.fourth_product_price_text == "$49.99"

    def test_fourth_product_add_to_cart_button_text_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Fleece Jacket")
        assert self.swag_home.fourth_product_add_to_cart_button_click_obj.text == "ADD TO CART"

    # -----------------------------
    # 5th product - Sauce Labs Onesie
    # -----------------------------
    def test_fifth_product_image_display(self):
        self.swag_home.scroll_until_text("Sauce Labs Onesie")
        assert self.swag_home.fifth_product_image_displayed.is_displayed()

    def test_fifth_product_name_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Onesie")
        assert self.swag_home.fifth_product_name_text == "Sauce Labs Onesie"

    def test_fifth_product_price_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Onesie")
        assert self.swag_home.fifth_product_price_text == "$7.99"

    def test_fifth_product_add_to_cart_button_text_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Onesie")
        assert self.swag_home.fifth_product_add_to_cart_button_click_obj.text == "ADD TO CART"


    def test_sixth_product_image_display(self):
        self.swag_home.scroll_until_text("Test.allTheThings() T-Shirt (Red)")
        assert self.swag_home.sixth_product_image_displayed.is_displayed()

    def test_sixth_product_name_check(self):
        self.swag_home.scroll_until_text("Test.allTheThings() T-Shirt (Red)")
        assert self.swag_home.sixth_product_name_text == "Test.allTheThings() T-Shirt (Red)"

    def test_sixth_product_price_check(self):
        self.swag_home.scroll_until_text("Test.allTheThings() T-Shirt (Red)")
        assert self.swag_home.sixth_product_price_text == "$15.99"

    def test_sixth_product_add_to_cart_button_text_check(self):
        self.swag_home.scroll_until_text("Test.allTheThings() T-Shirt (Red)")
        assert self.swag_home.sixth_product_add_to_cart_button_click_obj.text == "ADD TO CART"