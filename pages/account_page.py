from pages.base_page import Page
from selenium.webdriver.common.by import By


class AccountPage(Page):
    PROFILE_NAME_BTN = (By.ID, 'com.hdw.james.rider:id/profileName')
    ACCOUNT_PAGE_TITLE = (By.XPATH, '//android.widget.TextView[@text="Account"]')

    def tap_profile_btn(self):
        self.click(*self.PROFILE_NAME_BTN)
