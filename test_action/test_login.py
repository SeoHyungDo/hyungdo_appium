import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from root_obj.login_page_obj import swaglabs_home
from utility.passclass import passclass   # 아까 만든 BaseTest
from root_obj import login_page_obj

class TestLoginPage(passclass):


    def test_login_page(self):
        driver = self.driver
        swaglabs = swaglabs_home(self.driver)

        def clear(id_pw):
            id_pw.click()
            id_pw.clear()

        error_msg_email_not_exist = "Username is required"
        error_msg_password_not_exist = "Password is required"
        error_msg_lock_account = "Sorry, this user has been locked out."
        error_msg_id_pw_not_equal = "Username and password do not match any user in this service."

        swaglabs.login_button.click()
        assert swaglabs.login_err_msg_text() == error_msg_email_not_exist # "Username is required" 노출시 정상

        clear(swaglabs.input_id), clear(swaglabs.input_pw)

        swaglabs.input_id.click()
        swaglabs.input_id.send_keys("standard_user")
        swaglabs.login_button.click()
        assert swaglabs.login_err_msg_text() == error_msg_password_not_exist  # "password is required" 노출시 정상

        clear(swaglabs.input_id), clear(swaglabs.input_pw)

        swaglabs.input_id.click()
        swaglabs.input_id.send_keys("locked_out_user")
        swaglabs.input_pw.click()
        swaglabs.input_pw.send_keys("secret_sauce")
        swaglabs.login_button.click()
        assert swaglabs.login_err_msg_text() == error_msg_lock_account  # "Sorry, this user has been locked out." 노출시 정상

        clear(swaglabs.input_id), clear(swaglabs.input_pw)

        swaglabs.input_id.click()
        swaglabs.input_id.send_keys("standard_user")
        swaglabs.input_pw.click()
        swaglabs.input_pw.send_keys("secret_sauc")
        swaglabs.login_button.click()
        assert swaglabs.login_err_msg_text() == error_msg_id_pw_not_equal  # "Username and password do not match any user in the service." 노출시 정상

        clear(swaglabs.input_id), clear(swaglabs.input_pw)

        swaglabs.input_id.click()
        swaglabs.input_id.send_keys("standard_user")

        swaglabs.input_pw.click()
        swaglabs.input_pw.send_keys("secret_sauce")
        swaglabs.login_button.click() # 정상 로그인

        cart = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "test-Cart")
            )
        )
        assert cart.is_displayed()