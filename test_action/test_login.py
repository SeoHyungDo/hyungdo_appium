import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from root_obj.login_page_obj import swaglabs_home
from utility.passclass import passclass
from root_obj import login_page_obj

class TestLoginPage(passclass):

    def clear(self, Username_pw):
        Username_pw.click()
        Username_pw.clear()

    def test_logo_check(self) :
        assert self.swag.logo_visible() == True # 상단 로고가 노출되면 PASS

    def test_Username_placeholder_check(self):
        assert self.swag.input_Username_placeholder == "Username"

    def test_pw_placeholder_check(self):# ID Inputbox에 "Username" Text 노출되면 PASS
        assert self.swag.input_pw_placeholder == "Password" # PW Inputbox에 "Username" Text 노출되면 PASS

    def test_Username_not_exist(self):
        self.swag.login_button.click()
        assert self.swag.login_err_msg_text() == self.swag.error_msg_email_not_exist # "Username is required" 노출시 정상
        self.clear(self.swag.input_Username), self.clear(self.swag.input_pw)

    def test_pw_not_exist(self):
        self.swag.type_Username("standard_user")
        self.swag.login_button.click()
        assert self.swag.login_err_msg_text() == self.swag.error_msg_password_not_exist  # "password is required" 노출시 정상
        self.clear(self.swag.input_Username), self.clear(self.swag.input_pw)

    def test_lock_out_user(self):
        self.swag.type_Username("locked_out_user")
        self.swag.type_pw("secret_sauce")
        self.swag.login_button.click()
        assert self.swag.login_err_msg_text() == self.swag.error_msg_lock_account  # "Sorry, this user has been locked out." 노출시 정상
        self.clear(self.swag.input_Username), self.clear(self.swag.input_pw)

    def test_Username_pw_not_match(self):
        self.swag.type_Username("standard_user")
        self.swag.type_pw("secret_sauc")
        self.swag.login_button.click()
        assert self.swag.login_err_msg_text() == self.swag.error_msg_Username_pw_not_equal  # "Username and password do not match any user in the service." 노출시 정상

    def test_face_check_button_visible(self):
        assert self.swag.face_check_button_visible() == True # 하단에 Facecheck 버튼이 존재한다면 PASS

    def test_login_button_check(self):
        assert self.swag.login_button_name() == self.swag.Login_button_text # LOGIN 이름과 일치하는 로그인 버튼이 있는 경우 PASS

    def test_robot_image_check(self):
        assert self.swag.robot_image_visible() == True # 하단에 로봇 이미지 노출되면 PASS

    def test_login_cart_exist(self): # test_login.py 단에서는 로그인 후 카트 메뉴 존재까지만 확인한다.
        self.swag.type_Username("standard_user")
        self.swag.type_pw("secret_sauce")
        self.swag.login_button.click() # 정상 로그인

        cart = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "test-Cart")
            )
        )
        assert cart.is_displayed()
