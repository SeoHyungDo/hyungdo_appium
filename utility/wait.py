from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Wait:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def visible(self, locator): # 요소가 화면에 보이는 상태 까지 대기
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def clickable(self, locator): # 요소가 클릭 가능한 상태 까지 대기
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def present(self, locator): # 요소가 DOM에 존재만 하면 통과
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )