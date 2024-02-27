from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProfilePage(Page):
    FIRST_NAME_INPUT = (By.ID, 'com.hdw.james.rider:id/firstNameInput')
    LAST_NAME_INPUT = (By.ID, 'com.hdw.james.rider:id/lastNameInput')
    CONTINUE_BTN = (By.ID, 'com.hdw.james.rider:id/continueButton')

    def input_name_and_last(self, first, last):
        fn = self.find_element(*self.FIRST_NAME_INPUT)
        fn.clear()
        fn.send_keys(first)
        ln = self.find_element(*self.LAST_NAME_INPUT)
        ln.clear()
        ln.send_keys(last)

    def get_first_name_text(self):
        fn = self.find_element(*self.FIRST_NAME_INPUT).text
        return fn

    def get_last_name_text(self):
        ln = self.find_element(*self.LAST_NAME_INPUT).text
        return ln


