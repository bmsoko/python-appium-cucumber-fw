from pages.base_page import Page
from selenium.webdriver.common.by import By


class RidesPage(Page):
    MAIN_MENU_BTN = (By.ID, 'com.hdw.james.rider:id/MAIN_MENU_ID')
    INVITE_BTN = (By.XPATH, '(//android.widget.ImageView[@resource-id="com.hdw.james.rider:id/image"])[1]')
    RIDES_PAGE_TITLE = (By.XPATH, '//android.widget.TextView[@text="Rides"]')

    def tap_main_menu(self):
        self.click(*self.MAIN_MENU_BTN)

    def get_page_title(self):
        text_title = self.find_element(*self.RIDES_PAGE_TITLE).text
        return text_title
