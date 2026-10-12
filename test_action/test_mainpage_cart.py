import pytest
import allure
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

    @allure.step("메인 페이지 > 첫번째 상품 'ADD TO CART' 버튼 클릭 > 'ADD TO CART' 버튼이 'REMOVE' 버튼으로 바뀌면 정상")
    def test_first_product_remove_button_check(self):
        self.swag_home.login()
        self.swag_home.first_product_add_to_cart_button_el.click()
        assert self.cart.first_product_remove_button_text() == "REMOVE"

        self.swag_home.cart_locator_button_el_obj.click()

    @allure.step("메인 페이지 > Cart Manu > 햄버거 메뉴가 존재하면 정상")
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

    @allure.step("메인 페이지 > Cart Manu > hamburgermenu > 'ALL ITEMS' 메뉴가 존재하면 정상")
    def test_cart_hamburger_menu_all_items_text(self):
        self.cart.cart_hamburger_button_action.click()

        assert self.cart.cart_menu_all_items_text == "ALL ITEMS"

    @allure.step("메인 페이지 > Cart Manu > hamburgermenu > 'WEBVIEW' 메뉴가 존재하면 정상")
    def test_cart_hamburger_menu_webview_text(self):
        assert self.cart.cart_menu_webview_text == "WEBVIEW"

    @allure.step("메인 페이지 > Cart Manu > hamburgermenu > 'QR CODE SCANNER' 메뉴가 존재하면 정상")
    def test_cart_hamburger_menu_qr_code_scanner_text(self):
        assert self.cart.cart_menu_qr_text == "QR CODE SCANNER"

    @allure.step("메인 페이지 > Cart Manu > hamburgermenu > 'GEO LOCATION' 메뉴가 존재하면 정상")
    def test_cart_hamburger_menu_geo_location_text(self):
        assert self.cart.cart_menu_geo_text == "GEO LOCATION"

    @allure.step("메인 페이지 > Cart Manu > hamburgermenu > 'DRAWING' 메뉴가 존재하면 정상")
    def test_cart_hamburger_menu_drawing_text(self):
        assert self.cart.cart_menu_drawing_text == "DRAWING"

    @allure.step("메인 페이지 > Cart Manu > hamburgermenu > 'ABOUT' 메뉴가 존재하면 정상")
    def test_cart_hamburger_menu_about_text(self):
        assert self.cart.cart_menu_about_text == "ABOUT"

    @allure.step("메인 페이지 > Cart Manu > hamburgermenu > 'LOGOUT' 메뉴가 존재하면 정상")
    def test_cart_hamburger_menu_logout_text(self):
        assert self.cart.cart_menu_logout_text == "LOGOUT"

    @allure.step("메인 페이지 > Cart Manu > hamburgermenu > 'RESET APP STATE' 메뉴가 존재하면 정상")
    def test_cart_hamburger_menu_reset_app_state_text(self):
        assert self.cart.cart_menu_reset_text == "RESET APP STATE"

    @allure.step("메인 페이지 > Cart Manu > 삳단 로고가 존재하면 정상")
    def test_cart_top_logo_display(self):
        self.swag_home.close_menu_if_open()
        assert self.swag_home.top_logo.is_displayed()

    @allure.step("메인 페이지 > Cart Manu > Cart 아이콘이 존재하면 정상")
    def test_cart_cart_button_display(self):
        assert self.swag_home.cart_button.is_displayed()