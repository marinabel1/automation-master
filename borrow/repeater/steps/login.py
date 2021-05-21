# encoding: utf-8

import time
from borrow.newbie.steps.base import Base
from generator.name.name import NameGenerator
from generator.phone.phone import PhoneGenerator


class Login(Base):
    """ Форма авторизации """

    BUTTON_LOGIN_SELECTOR = "//button[contains(text(), 'Войти') and contains(concat(' ', @class, ' '), ' header__login ')]"

    LOGIN_FORM_SELECTOR = "//form[contains(concat(' ', @class, ' '), ' popup__body ')]"

    SELECTOR_INPUT_LOGIN = f"{LOGIN_FORM_SELECTOR}//input[@type='tel']"
    SELECTOR_FIELD_LOGIN = f"{SELECTOR_INPUT_LOGIN}{Base.ANCESTOR_FIELD_SELECTOR}"
    SELECTOR_ERROR_LOGIN = f"{SELECTOR_FIELD_LOGIN}{Base.ERROR_FIELD_SELECTOR}"

    SELECTOR_INPUT_PASSWORD = f"{LOGIN_FORM_SELECTOR}//input[@type='password']"
    SELECTOR_FIELD_PASSWORD = f"{SELECTOR_INPUT_PASSWORD}{Base.ANCESTOR_FIELD_SELECTOR}"
    SELECTOR_ERROR_PASSWORD = f"{SELECTOR_FIELD_PASSWORD}{Base.ERROR_FIELD_SELECTOR}"

    BUTTON_ENTER = f"{LOGIN_FORM_SELECTOR}//button[@type='submit']"

    def fill_all(self, loan_application):
        super().waiting_for_input_appear_on_page('surname')
        super().print_step_name()

        print(f"Login: {loan_application.borrower.phone}")
        print(f"Password: {loan_application.borrower.password}")

        time.sleep(1)

        self.find_element(self.BUTTON_LOGIN_SELECTOR).click()

        self.find_element(self.SELECTOR_INPUT_LOGIN).send_keys(loan_application.borrower.phone)
        self.find_element(self.SELECTOR_INPUT_PASSWORD).send_keys(loan_application.borrower.password)
        self.find_element(self.BUTTON_ENTER).click()

        self.save_screenshot()
        self.log_browser_console()
