from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    GETSTARTED_BTN = (By.ID, 'com.hdw.james.rider:id/getStartedButton')
    SNACK_BAR = (By.ID, 'com.hdw.james.rider:id/snackbar_text')
    DONE_BTN = (By.ID, 'com.hdw.james.rider:id/DEFAULT_TEXT_ACTION_MENU_ID')

    def tap_getstared(self):
        self.click(*self.GETSTARTED_BTN)

    def get_snack_bar_text(self):
        text_from_snack = self.find_element(*self.SNACK_BAR).text
        return text_from_snack

    # Done button is used in several parts.
    def tap_done(self):
        self.click(*self.DONE_BTN)