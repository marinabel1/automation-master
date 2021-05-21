# encoding: utf-8

import time
from api.LoanApplication import LoanApplication
from borrow.newbie.steps.base import Base


class Step2(Base):
    """ Подтверждение номера """

    # Код из SMS
    SELECTOR_INPUT_SMS_CODE = "//input[@name='code']"
    SELECTOR_FIELD_SMS_CODE = f"{SELECTOR_INPUT_SMS_CODE}{Base.ANCESTOR_FIELD_SELECTOR}"
    SELECTOR_ERROR_SMS_CODE = f"{SELECTOR_FIELD_SMS_CODE}{Base.ERROR_FIELD_SELECTOR}"

    # Счётчик "Отправить код повторно"
    SELECTOR_RESEND_COUNTER = f"//*[@class='percent']"
    # Отправить повторно
    SELECTOR_RESEND_LINK = f"//*[@class='link']"

    # Подтверждаем номер телефона с помощью кода
    def fill_all(self, loan_application):
        super().waiting_for_input_appear_on_page('code')
        super().print_step_name()

        # Без таймаута ошибка:
        # Internal error.
        # Получения статуса неавторизованным пользователем
        # или пользователем которому не принадлежит данная заявка на займ
        time.sleep(2)
        loan_application_id = self.__get_loan_application_id()
        loan_application.id = loan_application_id
        confirmation_code = self.__get_confirmation_code(loan_application_id)
        loan_application.borrower.password = confirmation_code

        self.find_element(self.SELECTOR_INPUT_SMS_CODE).send_keys(confirmation_code)

        time.sleep(1)

        self.find_element(super().BUTTON_NEXT_SELECTOR).click()

        self.save_screenshot()
        self.log_browser_console()

    def __get_loan_application_id(self):
        php_session_id = self.web_driver.get_cookie('PHPSESSID')['value']
        print(f"PHPSESSID: {php_session_id}")
        return super().get_loan_application_api().get_loan_application_id(php_session_id)

    def __get_confirmation_code(self, loan_application_id):
        return super().get_loan_application_api().get_confirmation_code(
            loan_application_id,
            LoanApplication.CONFIRMATION_TYPE_PERSONAL_INFO_CONFIRM
        )
