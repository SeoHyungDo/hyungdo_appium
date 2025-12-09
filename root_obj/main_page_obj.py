from appium.webdriver.common.appiumby import AppiumBy


class swaglabs_main_page:

    def __init__(self, driver):
        self.driver = driver

        self.hamburger_menu_locator = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Menu"]/android.view.ViewGroup')
        self.top_logo_locator = (AppiumBy.XPATH,
                                 '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView[2]')

        self.input_Username_locator = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
        self.input_pw_locator = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
        self.login_button_locator = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

        self.exit_button_locator = (AppiumBy.ACCESSIBILITY_ID, 'test-Close')
        self.menu_all_items_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="ALL ITEMS"]')
        self.menu_webview_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="WEBVIEW"]')
        self.menu_qr_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="QR CODE SCANNER"]')
        self.menu_geo_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="GEO LOCATION"]')
        self.menu_drawing_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="DRAWING"]')
        self.menu_about_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="ABOUT"]')
        self.menu_logout_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="LOGOUT"]')
        self.menu_reset_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="RESET APP STATE"]')
        self.cart_locator = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart drop zone"]')
        self.product_text = (AppiumBy.XPATH, '//android.widget.TextView[@text="PRODUCTS"]')
        self.text_modal_selector = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Modal Selector Button"]')
        self.button_area = (AppiumBy.XPATH,'//android.widget.ScrollView[@content-desc="test-PRODUCTS"]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/*')
        self.reserved_text_area = (AppiumBy.XPATH,'//android.widget.TextView[@text="© 2025 Sauce Labs. All Rights Reserved."]')
        self.policy_text_area = (AppiumBy.XPATH,'//android.widget.TextView[@text="Terms of Service | Privacy Policy"]')

        self.first_product_image = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Backpack"]]'
            '//android.widget.ImageView'
        )
        self.first_product_name = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@content-desc="test-Item title" and @text="Sauce Labs Backpack"]'
        )
        self.first_product_price = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Backpack"]]'
            '//android.widget.TextView[@content-desc="test-Price"]'
        )
        self.first_product_add_to_cart_button = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Backpack"]]'
            '//android.widget.TextView[@text="ADD TO CART"]'
        )


        self.second_product_image = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Bike Light"]]'
            '//android.widget.ImageView'
        )
        self.second_product_name = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@content-desc="test-Item title" and @text="Sauce Labs Bike Light"]'
        )
        self.second_product_price = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Bike Light"]]'
            '//android.widget.TextView[@content-desc="test-Price"]'
        )
        self.second_product_add_to_cart_button = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Bike Light"]]'
            '//android.widget.TextView[@text="ADD TO CART"]'
        )

        self.third_product_image = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Bolt T-Shirt"]]'
            '//android.widget.ImageView'
        )
        self.third_product_name = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@content-desc="test-Item title" and @text="Sauce Labs Bolt T-Shirt"]'
        )
        self.third_product_price = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Bolt T-Shirt"]]'
            '//android.widget.TextView[@content-desc="test-Price"]'
        )
        self.third_product_add_to_cart_button = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Bolt T-Shirt"]]'
            '//android.widget.TextView[@text="ADD TO CART"]'
        )

        self.fourth_product_image = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Fleece Jacket"]]'
            '//android.widget.ImageView'
        )
        self.fourth_product_name = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@content-desc="test-Item title" and @text="Sauce Labs Fleece Jacket"]'
        )
        self.fourth_product_price = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Fleece Jacket"]]'
            '//android.widget.TextView[@content-desc="test-Price"]'
        )
        self.fourth_product_add_to_cart_button = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Fleece Jacket"]]'
            '//android.widget.TextView[@text="ADD TO CART"]'
        )

        self.fifth_product_image = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Onesie"]]'
            '//android.widget.ImageView'
        )
        self.fifth_product_name = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@content-desc="test-Item title" and @text="Sauce Labs Onesie"]'
        )
        self.fifth_product_price = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Onesie"]]'
            '//android.widget.TextView[@content-desc="test-Price"]'
        )
        self.fifth_product_add_to_cart_button = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Sauce Labs Onesie"]]'
            '//android.widget.TextView[@text="ADD TO CART"]'
        )

        self.sixth_product_image = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Test.allTheThings() T-Shirt (Red)"]]'
            '//android.widget.ImageView'
        )
        self.sixth_product_name = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@content-desc="test-Item title" and @text="Test.allTheThings() T-Shirt (Red)"]'
        )
        self.sixth_product_price = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Test.allTheThings() T-Shirt (Red)"]]'
            '//android.widget.TextView[@content-desc="test-Price"]'
        )
        self.sixth_product_add_to_cart_button = (
            AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="test-Item"]'
            '[.//android.widget.TextView[@text="Test.allTheThings() T-Shirt (Red)"]]'
            '//android.widget.TextView[@text="ADD TO CART"]'
        )

        self.bottom_buttons_area = (
            AppiumBy.XPATH,
            '//android.widget.ScrollView[@content-desc="test-PRODUCTS"]'
            '/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup'
        )

        # 버튼 별칭 매핑
        self.BUTTON_INDEX = {
            "x": 0,
            "facebook": 1,
            "google": 2,
            "linkedin": 3
        }

    def get_bottom_button_by_index(self, index: int):
        container = self.driver.find_element(*self.bottom_buttons_area)
        buttons = container.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")

        if index >= len(buttons):
            raise Exception(f"요청한 index {index} 가 버튼 갯수({len(buttons)})보다 큼.")

        return buttons[index]

    def get_bottom_button(self, name: str):
        if name not in self.BUTTON_INDEX:
            raise KeyError(f"등록되지 않은 버튼 키: {name}, 등록된 키: {list(self.BUTTON_INDEX.keys())}")

        idx = self.BUTTON_INDEX[name]
        return self.get_bottom_button_by_index(idx)

    def scroll_until_text(self, text):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))'
        )

    def scroll_until_product_image(self, product_name: str):
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{product_name}"))'
        ).find_element(
            AppiumBy.XPATH,
            '../../..//android.widget.ImageView'
        )

    def get_add_to_cart_button_by_product(self, product_name: str):
        self.scroll_until_text(product_name)
        return self.driver.find_element(
            AppiumBy.XPATH,
            f'//android.view.ViewGroup[@content-desc="test-Item"]'
            f'[.//android.widget.TextView[@text="{product_name}"]]'
            f'//android.widget.TextView[@text="ADD TO CART"]'
        )

    def product_price_text(self, product_name: str) -> str:
        self.scroll_until_text(product_name)
        el = self.driver.find_element(
            AppiumBy.XPATH,
            f'//android.view.ViewGroup[@content-desc="test-Item"]'
            f'[.//android.widget.TextView[@text="{product_name}"]]'
            f'//android.widget.TextView[@content-desc="test-Price"]'
        )
        return el.text

    def product_card(self, product_name: str):
        self.scroll_until_text(product_name)
        return self.driver.find_element(
            AppiumBy.XPATH,
            f'//android.view.ViewGroup[@content-desc="test-Item"]'
            f'[.//android.widget.TextView[@content-desc="test-Item title" and @text="{product_name}"]]'
        )

    def _get_product_image_by_name(self, product_name: str):
        """
        상품 이름 TextView를 기준으로 위로 올라가면서
        가까운 조상 뷰들 안에서 ImageView를 찾아 반환한다. 구조가 조금 달라도 웬만하면 커버되도록 만든 안전형 헬퍼.
        """
        self.scroll_until_text(product_name)

        title_el = self.driver.find_element(
            AppiumBy.XPATH,
            f'//android.widget.TextView[@content-desc="test-Item title" and @text="{product_name}"]'
        )

        # 제목 기준으로 위로 최대 4단계까지 올라가면서, 그 조상/조상들 아래에서 ImageView 찾기 시도
        current = title_el
        for _ in range(4):
            try:
                # 현재 노드(or 조상) 아래에서 ImageView를 찾아본다.
                img = current.find_element(AppiumBy.CLASS_NAME, 'android.widget.ImageView')
                return img
            except Exception:
                # 못 찾으면 한 단계 위로 올라감
                try:
                    current = current.find_element(AppiumBy.XPATH, '..')
                except Exception:
                    break

        raise Exception(f'상품 "{product_name}" 에 대한 이미지를 찾지 못했습니다.')


    @property
    def input_Username(self):
        return self.driver.find_element(*self.input_Username_locator)

    @property
    def input_pw(self):
        return self.driver.find_element(*self.input_pw_locator)

    @property
    def login_button(self):
        return self.driver.find_element(*self.login_button_locator)

    def login(self):
        self.input_Username.click()
        self.input_Username.clear()
        self.input_Username.send_keys("standard_user")

        self.input_pw.click()
        self.input_pw.clear()
        self.input_pw.send_keys("secret_sauce")
        self.login_button.click()

    @property
    def hamburger_menu_icon(self):
        return self.driver.find_element(*self.hamburger_menu_locator)

    @property
    def menu_all_items(self):
        return self.driver.find_element(*self.menu_all_items_locator)

    @property
    def menu_all_items_text(self):
        return self.driver.find_element(*self.menu_all_items_locator).text

    @property
    def menu_webview(self):
        return self.driver.find_element(*self.menu_webview_locator)

    @property
    def menu_webview_text(self):
        return self.driver.find_element(*self.menu_webview_locator).text

    @property
    def menu_qr(self):
        return self.driver.find_element(*self.menu_qr_locator)

    @property
    def menu_qr_text(self):
        return self.driver.find_element(*self.menu_qr_locator).text

    @property
    def menu_geo(self):
        return self.driver.find_element(*self.menu_geo_locator)

    @property
    def menu_geo_text(self):
        return self.driver.find_element(*self.menu_geo_locator).text

    @property
    def menu_drawing(self):
        return self.driver.find_element(*self.menu_drawing_locator)

    @property
    def menu_drawing_text(self):
        return self.driver.find_element(*self.menu_drawing_locator).text

    @property
    def menu_close(self):
        return self.driver.find_element(*self.exit_button_locator)

    def close_menu_if_open(self):
        if self.driver.find_elements(*self.exit_button_locator):
            self.menu_close.click()

    @property
    def menu_about(self):
        return self.driver.find_element(*self.menu_about_locator)

    @property
    def menu_about_text(self):
        return self.driver.find_element(*self.menu_about_locator).text

    @property
    def menu_logout(self):
        return self.driver.find_element(*self.menu_logout_locator)

    @property
    def menu_logout_text(self):
        return self.driver.find_element(*self.menu_logout_locator).text

    @property
    def menu_reset(self):
        return self.driver.find_element(*self.menu_reset_locator)

    @property
    def menu_reset_text(self):
        return self.driver.find_element(*self.menu_reset_locator).text

    @property
    def top_logo(self):
        return self.driver.find_element(*self.top_logo_locator)

    @property
    def cart_button(self):
        return self.driver.find_element(*self.cart_locator)

    def cart_button_click(self):
        try:
            btn = self.cart_button
            if btn:
                btn.click()
        except Exception:
            pass

    @property
    def product_text_check(self):
        return self.driver.find_element(*self.product_text).text

    @property
    def text_modal_selector_button(self):
        return self.driver.find_element(*self.text_modal_selector)

    def text_modal_selector_button_click(self):
        try:
            btn = self.text_modal_selector_button
            if btn:
                btn.click()
        except Exception:
            pass

    @property
    def first_product_image_displayed(self):
        return self.product_card("Sauce Labs Backpack")

    @property
    def first_product_image_click(self):
        return self.first_product_image_displayed.click

    @property
    def first_product_name_text(self):
        return self.driver.find_element(*self.first_product_name).text

    @property
    def first_product_price_text(self):
        return self.driver.find_element(*self.first_product_price).text

    @property
    def first_product_add_to_cart_button_click_obj(self):
        return self.driver.find_element(*self.first_product_add_to_cart_button)

    @property
    def first_product_add_to_cart_button_click(self):
        return self.first_product_add_to_cart_button_click_obj.click()

# Second

    @property
    def second_product_image_displayed(self):
        return self.product_card("Sauce Labs Bike Light")

    @property
    def second_product_image_click(self):
        return self.second_product_image_displayed.click

    @property
    def second_product_name_text(self):
        return self.driver.find_element(*self.second_product_name).text

    @property
    def second_product_price_text(self):
        return self.driver.find_element(*self.second_product_price).text

    @property
    def second_product_add_to_cart_button_click_obj(self):
        return self.driver.find_element(*self.second_product_add_to_cart_button)

    @property
    def second_product_add_to_cart_button_click(self):
        return self.second_product_add_to_cart_button_click_obj.click()


# third
    @property
    def third_product_image_displayed(self):
        return self.product_card("Sauce Labs Bolt T-Shirt")

    @property
    def third_product_image_click(self):
        return self.third_product_image_displayed.click

    @property
    def third_product_name_text(self):
        return self.driver.find_element(*self.third_product_name).text

    @property
    def third_product_price_text(self):
        return self.driver.find_element(*self.third_product_price).text

    @property
    def third_product_add_to_cart_button_click_obj(self):
        return self.driver.find_element(*self.third_product_add_to_cart_button)

    @property
    def third_product_add_to_cart_button_click(self):
        return self.third_product_add_to_cart_button_click_obj.click()

# fourth
# 3, 4번만 같은 방식으로 했을때 에러가 나서 바꿔 놓음
    @property
    def fourth_product_image_displayed(self):
        return self.product_card("Sauce Labs Fleece Jacket")

    @property
    def fourth_product_image_click(self):
        return self.fourth_product_image_displayed.click

    @property
    def fourth_product_name_text(self):
        return self.driver.find_element(*self.fourth_product_name).text

    @property
    def fourth_product_price_text(self):
        return self.driver.find_element(*self.fourth_product_price).text

    @property
    def fourth_product_add_to_cart_button_click_obj(self):
        return self.driver.find_element(*self.fourth_product_add_to_cart_button)

    @property
    def fourth_product_add_to_cart_button_click(self):
        return self.fourth_product_add_to_cart_button_click_obj.click()


# fifth
    @property
    def fifth_product_image_displayed(self):
        return self.product_card("Sauce Labs Onesie")

    @property
    def fifth_product_image_click(self):
        return self.fifth_product_image_displayed.click

    @property
    def fifth_product_name_text(self):
        return self.driver.find_element(*self.fifth_product_name).text

    @property
    def fifth_product_price_text(self):
        return self.driver.find_element(*self.fifth_product_price).text

    @property
    def fifth_product_add_to_cart_button_click_obj(self):
        return self.driver.find_element(*self.fifth_product_add_to_cart_button)

    @property
    def fifth_product_add_to_cart_button_click(self):
        return self.fifth_product_add_to_cart_button_click_obj.click()



# sixth
    @property
    def sixth_product_image_displayed(self):
        return self.product_card("Test.allTheThings() T-Shirt (Red)")

    @property
    def sixth_product_image_click(self):
        return self.sixth_product_image_displayed.click

    @property
    def sixth_product_name_text(self):
        return self.driver.find_element(*self.sixth_product_name).text

    @property
    def sixth_product_price_text(self):
        return self.driver.find_element(*self.sixth_product_price).text

    @property
    def sixth_product_add_to_cart_button_click_obj(self):
        return self.driver.find_element(*self.sixth_product_add_to_cart_button)

    @property
    def sixth_product_add_to_cart_button_click(self):
        return self.sixth_product_add_to_cart_button_click_obj.click()

    @property
    def reserved_text_obj(self):
        return self.driver.find_element(*self.reserved_text_area).text

    @property
    def policy_text_obj(self):
        return self.driver.find_element(*self.policy_text_area).text