from pages.base_page import Page
from selenium.webdriver.common.by import By


class DigitCodeVerificationPage(Page):
    TITLE = (By.ID, 'com.hdw.james.rider:id/title')

    def get_title_text(self):
        return self.find_element(*self.TITLE).text

