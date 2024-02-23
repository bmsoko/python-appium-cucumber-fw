from pages.main_page import MainPage
from pages.phone_number_page import PhoneNumberPage
from pages.digit_code_verification_page import DigitCodeVerificationPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.account_page import AccountPage
from pages.rides_page import RidesPage


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.phone_number_page = PhoneNumberPage(driver)
        self.digit_code_verification_page = DigitCodeVerificationPage(driver)
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        self.account_page = AccountPage(driver)
        self.rides_page = RidesPage(driver)
