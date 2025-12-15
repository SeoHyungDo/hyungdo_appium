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