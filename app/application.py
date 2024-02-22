from pages.main_page import MainPage
from pages.phone_number_page import PhoneNumberPage
from pages.digit_code_verification_page import DigitCodeVerificationPage


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.phone_number_page = PhoneNumberPage(driver)
        self.digit_code_verification_page = DigitCodeVerificationPage(driver)
