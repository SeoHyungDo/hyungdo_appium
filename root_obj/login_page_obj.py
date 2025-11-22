from http.client import responses
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class swaglabs_home:

    def __init__(self, driver):
        self.driver = driver

        self.logo = (AppiumBy.ACCESSIBILITY_ID, "test-biometry")
        self.input_id_locator = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
        self.input_pw_locator = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
        self.login_button_locator = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
        self.login_button_locator_text = (AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-LOGIN"]/android.widget.TextView')
        # 버튼 내 LOGIN Text가 자식View에 있어 별도 루트 생성
        self.robot_image = (AppiumBy.XPATH,'//android.widget.ScrollView[@content-desc="test-Login"]/android.view.ViewGroup/android.widget.ImageView[2]')
        self.login_err_msg_locator = (AppiumBy.XPATH, '//*[@content-desc="test-Error message"]/*') # /* 를 붙여야 부모 요소 밑의 자식 텍스트를 읽음
        self.face_check = (AppiumBy.ACCESSIBILITY_ID, 'test-face-recognition')

    def logo_visible(self):
        try:
            self.driver.find_element(*self.robot_image)  # 이미지 locator
            return True
        except:
            return False

    def login_err_msg_text(self):
        return self.driver.find_element(*self.login_err_msg_locator).text

    @property
    def login_button(self):
        return self.driver.find_element(*self.login_button_locator)

    @property
    def input_id(self):
        return self.driver.find_element(*self.input_id_locator)

    @property
    def input_id_placeholder(self):
        return self.input_id.get_attribute("hint")

    @property
    def input_pw(self):
        return self.driver.find_element(*self.input_pw_locator)

    @property
    def input_pw_placeholder(self):
        return self.input_pw.get_attribute("hint")

    def type_id(self, username: str): # 3줄 작성 될 클릭, 클리어, 아이디 입력 코드를 1줄로 압축한다.
        self.input_id.click()
        self.input_id.clear()
        self.input_id.send_keys(username)

    def type_pw(self, password: str): # 3줄 작성 될 클릭, 클리어, 패스워드 입력 코드를 1줄로 압축한다.
        self.input_pw.click()
        self.input_pw.clear()
        self.input_pw.send_keys(password)

    def login_button_name(self):
        return self.driver.find_element(*self.login_button_locator_text).text

    def face_check_button_visible(self) :
        try:
            self.driver.find_element(*self.face_check)
            return True
        except :
            return False

    def robot_image_visible(self):
        try:
            self.driver.find_element(*self.robot_image)  # 이미지 locator
            return True
        except:
            return False