import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from root_obj.login_page_obj import swaglabs_home
from utility.passclass import passclass
from root_obj import login_page_obj

class TestLoginPage(passclass):


    def clear(self, id_pw):
        id_pw.click()
        id_pw.clear()

    def test_logo_check(self) :
        assert self.swag.logo_visible() == True # 상단 로고가 노출되면 PASS
        assert self.swag.input_id_placeholder == "Username" # ID Inputbox에 "Username" Text 노출되면 PASS
        assert self.swag.input_pw_placeholder == "Password" # PW Inputbox에 "Username" Text 노출되면 PASS

        error_msg_email_not_exist = "Username is required"
        error_msg_password_not_exist = "Password is required"
        error_msg_lock_account = "Sorry, this user has been locked out."
        error_msg_id_pw_not_equal = "Username and password do not match any user in this service."
        Login_button_text = "LOGIN"

        self.swag.login_button.click()
        assert self.swag.login_err_msg_text() == error_msg_email_not_exist # "Username is required" 노출시 정상

        self.clear(self.swag.input_id), self.clear(self.swag.input_pw)

        self.swag.type_id("standard_user")
        self.swag.login_button.click()
        assert self.swag.login_err_msg_text() == error_msg_password_not_exist  # "password is required" 노출시 정상

        self.clear(self.swag.input_id), self.clear(self.swag.input_pw)

        self.swag.type_id("locked_out_user")
        self.swag.type_pw("secret_sauce")
        self.swag.login_button.click()
        assert self.swag.login_err_msg_text() == error_msg_lock_account  # "Sorry, this user has been locked out." 노출시 정상

        self.clear(self.swag.input_id), self.clear(self.swag.input_pw)

        self.swag.type_id("standard_user")
        self.swag.type_pw("secret_sauc")
        self.swag.login_button.click()
        assert self.swag.login_err_msg_text() == error_msg_id_pw_not_equal  # "Username and password do not match any user in the service." 노출시 정상

        assert self.swag.face_check_button_visible() == True # 하단에 Facecheck 버튼이 존재한다면 PASS
        assert self.swag.login_button_name() == Login_button_text # LOGIN 이름과 일치하는 로그인 버튼이 있는 경우 PASS
        assert self.swag.robot_image_visible() == True # 하단에 로봇 이미지 노출되면 PASS

        self.clear(self.swag.input_id), self.clear(self.swag.input_pw)

        self.swag.type_id("standard_user")
        self.swag.type_pw("secret_sauce")
        self.swag.login_button.click() # 정상 로그인

        cart = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "test-Cart")
            )
        )
        assert cart.is_displayed()
