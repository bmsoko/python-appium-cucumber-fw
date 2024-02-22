from pages.base_page import Page
from selenium.webdriver.common.by import By


class PhoneNumberPage(Page):
    COUNTRY_CODE_SELECTOR = (By.ID, 'com.hdw.james.rider:id/spinner')
    PHONE_NUMBER_INPUT = (By.ID, 'com.hdw.james.rider:id/input')
    CONTINUE_BTN = (By.ID, 'com.hdw.james.rider:id/continueButton')

    def input_phone_number(self, phone_number):
        pn = self.find_element(*self.PHONE_NUMBER_INPUT)
        pn.clear()
        pn.send_keys(phone_number)
        self.click(*self.CONTINUE_BTN)


