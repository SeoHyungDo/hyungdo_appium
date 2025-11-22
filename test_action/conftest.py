import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from root_obj.login_page_obj import swaglabs_home

@pytest.fixture(scope="class")
def setup(request):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UIAutomator2"
    options.udid = "R3CW107YQMB"

    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.SplashActivity"


    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )
    driver.implicitly_wait(10)

    request.cls.driver = driver
    request.cls.swag = swaglabs_home(driver)

    yield driver

    driver.quit()