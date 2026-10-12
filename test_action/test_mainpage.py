import allure
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

    @allure.step("메인 페이지 > 좌측 상단 햄버거 버튼이 노출되는 경우 정상")
    def test_login_hamburger_menu_check(self):
        self.swag_home.login()
        assert self.swag_home.hamburger_menu_icon.is_displayed()

    @allure.step("메인 페이지 > 좌측 상단 햄버거 버튼 > 'ALL ITEMS' 버튼이 노출되는 경우 정상")
    def test_hamburger_menu_all_items_text(self):
        self.swag_home.hamburger_menu_icon.click()
        assert self.swag_home.menu_all_items_text == "ALL ITEMS"

    @allure.step("메인 페이지 > 좌측 상단 햄버거 버튼 > 'WEBVIEW' 버튼이 노출되는 경우 정상")
    def test_hamburger_menu_webview_text(self):
        assert self.swag_home.menu_webview_text == "WEBVIEW"

    @allure.step("메인 페이지 > 좌측 상단 햄버거 버튼 > 'QR CODE SCANNER' 버튼이 노출되는 경우 정상")
    def test_hamburger_menu_qr_code_scanner_text(self):
        assert self.swag_home.menu_qr_text == "QR CODE SCANNER"

    @allure.step("메인 페이지 > 좌측 상단 햄버거 버튼 > 'GEO LOCATION' 버튼이 노출되는 경우 정상")
    def test_hamburger_menu_geo_location_text(self):
        assert self.swag_home.menu_geo_text == "GEO LOCATION"

    @allure.step("메인 페이지 > 좌측 상단 햄버거 버튼 > 'DRAWING' 버튼이 노출되는 경우 정상")
    def test_hamburger_menu_drawing_text(self):
        assert self.swag_home.menu_drawing_text == "DRAWING"

    @allure.step("메인 페이지 > 좌측 상단 햄버거 버튼 > 'ABOUT' 버튼이 노출되는 경우 정상")
    def test_hamburger_menu_about_text(self):
        assert self.swag_home.menu_about_text == "ABOUT"

    @allure.step("메인 페이지 > 좌측 상단 햄버거 버튼 > 'LOGOUT' 버튼이 노출되는 경우 정상")
    def test_hamburger_menu_logout_text(self):
        assert self.swag_home.menu_logout_text == "LOGOUT"

    @allure.step("메인 페이지 > 좌측 상단 햄버거 버튼 > 'RESET APP STATE' 버튼이 노출되는 경우 정상")
    def test_hamburger_menu_reset_app_state_text(self):
        assert self.swag_home.menu_reset_text == "RESET APP STATE"

    @allure.step("메인 페이지 > 햄버거 메뉴를 닫고, 상단 로고가 노출되는 경우 정상")
    def test_top_logo_display(self):
        self.swag_home.close_menu_if_open()
        assert self.swag_home.top_logo.is_displayed()

    @allure.step("메인 페이지 > 우측 상단 cart 버튼이 노출되는 경우 정상")
    def test_cart_button_display(self):
        assert self.swag_home.cart_button.is_displayed()

    @allure.step("메인 페이지 > 상단 'PRODUCTS' 명칭이 노출되는 경우 정상")
    def test_product_text(self):
        assert self.swag_home.product_text_check == "PRODUCTS"

    @allure.step("메인 페이지 > 상단 modal selector 버튼이 노출되는 경우 정상")
    def test_text_modal_selector_button_check(self):
        assert self.swag_home.text_modal_selector_button.is_displayed()

    @allure.step("메인 페이지 > 좌측 상단 첫번째 상품 이미지가 노출되는 경우 정상")
    def test_first_product_image_display(self):
        self.swag_home.scroll_until_text("Sauce Labs Backpack")
        assert self.swag_home.first_product_image_displayed.is_displayed()

    @allure.step("메인 페이지 > 좌측 상단 첫번째 상품 상품명이 'Sauce Labs Backpack'로 노출되는 경우 정상")
    def test_first_product_name_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Backpack")
        assert self.swag_home.first_product_name_text == "Sauce Labs Backpack"

    @allure.step("메인 페이지 > 좌측 상단 첫번째 상품 가격이 '$29.99'로 노출되는 경우 정상")
    def test_first_product_price_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Backpack")
        assert self.swag_home.first_product_price_text == "$29.99"

    @allure.step("메인 페이지 > 좌측 상단 첫번째 상품 하단에 'ADD TO CART' 버튼이 노출되는 경우 정상")
    def test_first_product_add_to_cart_button_text_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Backpack")
        assert self.swag_home.first_product_add_to_cart_button_click_obj.text == "ADD TO CART"

    @allure.step("메인 페이지 > 좌측 상단 두번째 상품 이미지가 노출되는 경우 정상")
    def test_second_product_image_display(self):
        self.swag_home.scroll_until_text("Sauce Labs Bike Light")
        assert self.swag_home.second_product_image_displayed.is_displayed()

    @allure.step("메인 페이지 > 좌측 상단 두번째 상품 상품명이 'Sauce Labs Bike Light'로 노출되는 경우 정상")
    def test_second_product_name_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Bike Light")
        assert self.swag_home.second_product_name_text == "Sauce Labs Bike Light"

    @allure.step("메인 페이지 > 좌측 상단 두번째 상품 가격이 '$9.99'로 노출되는 경우 정상")
    def test_second_product_price_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Bike Light")
        assert self.swag_home.second_product_price_text == "$9.99"

    @allure.step("메인 페이지 > 좌측 상단 두번째 상품 하단에 'ADD TO CART' 버튼이 노출되는 경우 정상")
    def test_second_product_add_to_cart_button_text_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Bike Light")
        assert self.swag_home.second_product_add_to_cart_button_click_obj.text == "ADD TO CART"

    @allure.step("메인 페이지 > 세번째 상품 이미지가 노출되는 경우 정상")
    def test_third_product_image_display(self):
        self.swag_home.scroll_until_text("Sauce Labs Bolt T-Shirt")
        assert self.swag_home.third_product_image_displayed.is_displayed()

    @allure.step("메인 페이지 > 세번째 상품 상품명이 'Sauce Labs Bolt T-Shirt'로 노출되는 경우 정상")
    def test_third_product_name_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Bolt T-Shirt")
        assert self.swag_home.third_product_name_text == "Sauce Labs Bolt T-Shirt"

    @allure.step("메인 페이지 > 세번째 상품 가격이 '$15.99'로 노출되는 경우 정상")
    def test_third_product_price_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Bolt T-Shirt")
        assert self.swag_home.third_product_price_text == "$15.99"

    @allure.step("메인 페이지 > 세번째 상품 하단에 'ADD TO CART' 버튼이 노출되는 경우 정상")
    def test_third_product_add_to_cart_button_text_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Bolt T-Shirt")
        assert self.swag_home.third_product_add_to_cart_button_click_obj.text == "ADD TO CART"

    @allure.step("메인 페이지 > 네번째 상품 이미지가 노출되는 경우 정상")
    def test_fourth_product_image_display(self):
        self.swag_home.scroll_until_text("Sauce Labs Fleece Jacket")
        assert self.swag_home.fourth_product_image_displayed.is_displayed()

    @allure.step("메인 페이지 > 네번째 상품 상품명이 'Sauce Labs Fleece Jacket'로 노출되는 경우 정상")
    def test_fourth_product_name_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Fleece Jacket")
        assert self.swag_home.fourth_product_name_text == "Sauce Labs Fleece Jacket"

    @allure.step("메인 페이지 > 네번째 상품 가격이 '$49.99'로 노출되는 경우 정상")
    def test_fourth_product_price_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Fleece Jacket")
        assert self.swag_home.fourth_product_price_text == "$49.99"

    @allure.step("메인 페이지 > 네번째 상품 하단에 'ADD TO CART' 버튼이 노출되는 경우 정상")
    def test_fourth_product_add_to_cart_button_text_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Fleece Jacket")
        assert self.swag_home.fourth_product_add_to_cart_button_click_obj.text == "ADD TO CART"

    @allure.step("메인 페이지 > 다섯번째 상품 이미지 노출되는 경우 정상")
    def test_fifth_product_image_display(self):
        self.swag_home.scroll_until_text("Sauce Labs Onesie")
        assert self.swag_home.fifth_product_image_displayed.is_displayed()

    @allure.step("메인 페이지 > 다섯번째 상품 상품명 'Sauce Labs Onesie' 로 노출되는 경우 정상")
    def test_fifth_product_name_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Onesie")
        assert self.swag_home.fifth_product_name_text == "Sauce Labs Onesie"

    @allure.step("메인 페이지 > 다섯번째 상품 가격이 '$7.99' 로 노출되는 경우 정상")
    def test_fifth_product_price_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Onesie")
        assert self.swag_home.fifth_product_price_text == "$7.99"

    @allure.step("메인 페이지 > 다섯번째 상품 하단에 'ADD TO CART' 버튼이 노출되는 경우 정상")
    def test_fifth_product_add_to_cart_button_text_check(self):
        self.swag_home.scroll_until_text("Sauce Labs Onesie")
        assert self.swag_home.fifth_product_add_to_cart_button_click_obj.text == "ADD TO CART"

    @allure.step("메인 페이지 > 여섯번쨰 상품 이미지가 정상 노출되는 경우 정상")
    def test_sixth_product_image_display(self):
        self.swag_home.scroll_until_text("Test.allTheThings() T-Shirt (Red)")
        assert self.swag_home.sixth_product_image_displayed.is_displayed()

    @allure.step("메인 페이지 > 여섯번쨰 상품 상품명이 'Test.allTheThings() T-Shirt (Red)'로 노출되는 경우 정상")
    def test_sixth_product_name_check(self):
        self.swag_home.scroll_until_text("Test.allTheThings() T-Shirt (Red)")
        assert self.swag_home.sixth_product_name_text == "Test.allTheThings() T-Shirt (Red)"

    @allure.step("메인 페이지 > 여섯번쨰 상품 가격이 '$15.99'로 노출되는 경우 정상")
    def test_sixth_product_price_check(self):
        self.swag_home.scroll_until_text("Test.allTheThings() T-Shirt (Red)")
        assert self.swag_home.sixth_product_price_text == "$15.99"

    @allure.step("메인 페이지 > 여섯번쨰 상품 하단에 'ADD TO CART' 버튼이 노출되는 경우 정상")
    def test_sixth_product_add_to_cart_button_text_check(self):
        self.swag_home.scroll_until_text("Test.allTheThings() T-Shirt (Red)")
        assert self.swag_home.sixth_product_add_to_cart_button_click_obj.text == "ADD TO CART"

    @allure.step("메인 페이지 > 최하단에 'X' 버튼이 노출되는 경우 정상")
    def test_x_button_check(self):
        btn = self.swag_home.get_bottom_button("x")
        assert btn.is_displayed()

    @allure.step("메인 페이지 > 최하단에 'facebook' 버튼이 노출되는 경우 정상")
    def test_facebook_button_check(self):
        btn = self.swag_home.get_bottom_button("facebook")
        assert btn.is_displayed()

    @allure.step("메인 페이지 > 최하단에 'google' 버튼이 노출되는 경우 정상")
    def test_google_button_check(self):
        btn = self.swag_home.get_bottom_button("google")
        assert btn.is_displayed()

    @allure.step("메인 페이지 > 최하단에 'linkedin' 버튼이 노출되는 경우 정상")
    def test_linkedin_button_check(self):
        btn = self.swag_home.get_bottom_button("linkedin")
        assert btn.is_displayed()

    @allure.step("메인 페이지 > 최하단에 '© 2026 Sauce Labs. All Rights Reserved.' 문구가 노출되는 경우 정상")
    def test_reserved_text_check(self):
        self.swag_home.scroll_until_text("© 2026 Sauce Labs. All Rights Reserved.")
        assert self.swag_home.reserved_text_obj == "© 2026 Sauce Labs. All Rights Reserved."

    @allure.step("메인 페이지 > 최하단에 'Terms of Service | Privacy Policy' 문구가 노출되는 경우 정상")
    def test_policy_text_check(self):
        assert self.swag_home.policy_text_obj == "Terms of Service | Privacy Policy"