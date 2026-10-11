import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from root_obj.login_page_obj import swaglabs_home
from utility.passclass import passclass
from root_obj import login_page_obj

class TestLoginPage(passclass):

    def clear(self, username_pw):
        username_pw.click()
        username_pw.clear()

    @allure.step("로그인 페이지 > 상단 로고 노출 여부 확인")
    def test_logo_check(self) :
        assert self.swag.logo_visible() == True

    @allure.step("로그인 페이지 > username textbox placeholder 'Username'으로 정상 노출 되는지 확인")
    def test_username_placeholder_check(self):
        assert self.swag.input_username_placeholder == "Username"

    @allure.step("로그인 페이지 > password textbox placeholder 'Password'으로 정상 노출 되는지 확인")
    def test_pw_placeholder_check(self):
        assert self.swag.input_pw_placeholder == "Password"

    @allure.step("로그인 페이지 > Username 미입력 상태로 로그인을 눌렀을시 'Username is required' 문구가 노출되면 정상")
    def test_username_not_exist(self):
        self.swag.login_button.click()
        assert self.swag.login_err_msg_text() == self.swag.error_msg_email_not_exist

    @allure.step("로그인 페이지 > Username은 입력, Password 미입력 상태로 로그인을 눌렀을시 password is required 문구가 노출되면 정상")
    def test_pw_not_exist(self):
        self.swag.type_username("standard_user")
        self.swag.login_button.click()
        assert self.swag.login_err_msg_text() == self.swag.error_msg_password_not_exist

    @allure.step("로그인 페이지 > 정지당한 계졍 로그인시 'Sorry, this user has been locked out.' 문구 노출되면 정상")
    def test_lock_out_user(self):
        self.swag.type_username("locked_out_user")
        self.swag.type_pw("secret_sauce")
        self.swag.login_button.click()
        assert self.swag.login_err_msg_text() == self.swag.error_msg_lock_account

    @allure.step("로그인 페이지 > ID / PW가 일치하지 않는 경우 'Username and password do not match any user in the service.' 문구 노출시 정상")
    def test_username_pw_not_match(self):
        self.swag.type_username("standard_user")
        self.swag.type_pw("secret_sauc")
        self.swag.login_button.click()
        assert self.swag.login_err_msg_text() == self.swag.error_msg_Username_pw_not_equal

    @allure.step("로그인 페이지 > 하단에 Facecheck 버튼이 존재한다면 PASS")
    def test_face_check_button_visible(self):
        assert self.swag.face_check_button_visible() == True

    @allure.step("로그인 페이지 > 'LOGIN' 버튼이 있는 경우 정상")
    def test_login_button_check(self):
        assert self.swag.login_button_name() == self.swag.Login_button_text # LOGIN 이름과 일치하는 로그인 버튼이 있는 경우 PASS

    @allure.step("로그인 페이지 > 하단에 로봇 이미지가 있다면 정상")
    def test_robot_image_check(self):
        assert self.swag.robot_image_visible() == True

    @allure.step("로그인 페이지 > 로그인 완료, 상단에 cart 버튼이 존재하는 경우 정상")
    def test_login_cart_exist(self):
        self.swag.type_username("standard_user")
        self.swag.type_pw("secret_sauce")
        self.swag.login_button.click() # 정상 로그인

        cart = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "test-Cart")
            )
        )
        assert cart.is_displayed()
