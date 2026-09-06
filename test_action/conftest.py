import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from root_obj.login_page_obj import swaglabs_home
from root_obj.main_page_obj import swaglabs_main_page
from utility.wait import Wait
from root_obj.cart_page_obj import cart_page
import subprocess # 연결기기 탐색
from datetime import datetime # 스크린샷 자동으로 남기기
import os

def get_connected_device(): # 연결된 기기 자동 탐색
    result = subprocess.run(
        ["adb", "devices"],
        capture_output=True,
        text=True,
        check=True
    )

    devices = []

    for line in result.stdout.splitlines()[1:]:
        if "\tdevice" in line:
            devices.append(line.split("\t")[0])

    if not devices:
        raise RuntimeError("연결된 Android 기기가 없습니다.")

    if len(devices) > 1:
        raise RuntimeError(
            f"Android 기기가 여러 대 연결되어 있습니다: {devices}"
        )

    return devices[0]

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # 실제 테스트 수행(call) 단계에서 실패했을 때만 캡처
    if report.when == "call" and report.failed:

        driver = None

        # 현재 테스트 클래스에 저장된 Appium driver 가져오기
        if item.instance and hasattr(item.instance, "driver"):
            driver = item.instance.driver

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"screenshots/{item.name}_{now}.png"

            driver.save_screenshot(file_name)

            print(f"\n📸 실패 스크린샷 저장: {file_name}")

@pytest.fixture(scope="class")
def setup(request):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UIAutomator2"
    options.udid = get_connected_device() # 연결된 기기 자동 탐색

    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.SplashActivity"


    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )
    driver.implicitly_wait(10)

    request.cls.driver = driver
    request.cls.swag = swaglabs_home(driver)
    request.cls.swag_home = swaglabs_main_page(driver)
    request.cls.wait = Wait(driver)
    request.cls.cart = cart_page(driver)

    yield driver

    driver.quit()