# encoding: utf-8

import time
from borrow.newbie.steps.base import Base
from generator.name.name import NameGenerator
from generator.phone.phone import PhoneGenerator


class Step1(Base):
    """ Общие сведения """
    # Фамилия
    SELECTOR_INPUT_SURNAME = "//input[@name='surname']"
    SELECTOR_FIELD_SURNAME = f"{SELECTOR_INPUT_SURNAME}{Base.ANCESTOR_FIELD_SELECTOR}"
    SELECTOR_ERROR_SURNAME = f"{SELECTOR_FIELD_SURNAME}{Base.ERROR_FIELD_SELECTOR}"
    # Имя
    SELECTOR_INPUT_NAME = "//input[@name='name']"
    SELECTOR_FIELD_NAME = f"{SELECTOR_INPUT_NAME}{Base.ANCESTOR_FIELD_SELECTOR}"
    SELECTOR_ERROR_NAME = f"{SELECTOR_FIELD_NAME}{Base.ERROR_FIELD_SELECTOR}"
    # Отчество
    SELECTOR_INPUT_PATRONYMIC = "//input[@name='patronymic']"
    SELECTOR_FIELD_PATRONYMIC = f"{SELECTOR_INPUT_PATRONYMIC}{Base.ANCESTOR_FIELD_SELECTOR}"
    SELECTOR_ERROR_PATRONYMIC = f"{SELECTOR_FIELD_PATRONYMIC}{Base.ERROR_FIELD_SELECTOR}"
    # Телефон
    SELECTOR_INPUT_PHONE = "//input[@name='phone']"
    SELECTOR_FIELD_PHONE = f"{SELECTOR_INPUT_PHONE}{Base.ANCESTOR_FIELD_SELECTOR}"
    SELECTOR_ERROR_PHONE = f"{SELECTOR_FIELD_PHONE}{Base.ERROR_FIELD_SELECTOR}"
    # Электронная почта
    SELECTOR_INPUT_EMAIL = "//input[@name='email']"
    SELECTOR_FIELD_EMAIL = f"{SELECTOR_INPUT_EMAIL}{Base.ANCESTOR_FIELD_SELECTOR}"
    SELECTOR_ERROR_EMAIL = f"{SELECTOR_FIELD_EMAIL}{Base.ERROR_FIELD_SELECTOR}"

    def fill_surname(self, surname=None):
        if surname is None:
            surname = NameGenerator().get_surname()

        self.find_element(self.SELECTOR_INPUT_SURNAME).send_keys(surname)

    def fill_name(self, name=None):
        if name is None:
            name = NameGenerator().get_name()

        self.find_element(self.SELECTOR_INPUT_NAME).send_keys(name)

    def fill_patronymic(self, patronymic=None):
        if patronymic is None:
            patronymic = NameGenerator().get_name()

        self.find_element(self.SELECTOR_INPUT_PATRONYMIC).send_keys(patronymic)

    def fill_phone(self, phone=None):
        if phone is None:
            phone = PhoneGenerator.generate_random_phone()

        self.find_element(self.SELECTOR_INPUT_PHONE).send_keys(phone)

    def fill_email(self, email=None):
        if email is None:
            email = ''

        self.find_element(self.SELECTOR_INPUT_PHONE).send_keys(email)

    # На первой странице анкеты запонляем поля:
    # - Фамилия
    # - Имя
    # - Отчество
    # - Номер телефона
    # нажимаем кнопку "Продолжить"
    def fill_all(self, loan_application):
        super().waiting_for_input_appear_on_page('surname')
        super().print_step_name()

        print(f"ФИО заёмщика: {loan_application.borrower.surname} {loan_application.borrower.name} {loan_application.borrower.patronymic}")
        print(f"email: {loan_application.borrower.email}")
        print(f"Телефон: {loan_application.borrower.phone}")

        time.sleep(1)

        self.find_element(self.SELECTOR_INPUT_SURNAME).send_keys(loan_application.borrower.surname)
        self.find_element(self.SELECTOR_INPUT_NAME).send_keys(loan_application.borrower.name)
        self.find_element(self.SELECTOR_INPUT_PATRONYMIC).send_keys(loan_application.borrower.patronymic)
        self.find_element(self.SELECTOR_INPUT_PHONE).send_keys(loan_application.borrower.phone)
        self.find_element(self.SELECTOR_INPUT_EMAIL).send_keys(loan_application.borrower.email)
        # self.find_element(agreeButtonSelector).click()
        self.find_element(super().BUTTON_NEXT_SELECTOR).click()

        self.save_screenshot()
        self.log_browser_console()

        # # Если номер телефона уже зарегистрирован, то генерируем новый номер
        # while True:
        #     arr = findElement(autorizationWindow)
        #     if len(arr) > 0:
        #         phone = self.__generate_random_phone()
        #         print('Новый номер телефона', phone)
        #         self.find_element(self.SELECTOR_INPUT_PHONE).clear()
        #         self.find_element(self.SELECTOR_INPUT_PHONE).send_keys(phone)
        #         time.sleep(2)
        #         self.find_element(super().BUTTON_NEXT_SELECTOR).click()
        #     else:
        #         break
