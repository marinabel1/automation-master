# encoding: utf-8
from api.Zaymigo import Zaymigo


class Admin:
    def __init__(self, web_driver):
        self.web_driver = web_driver

    def confirm_by_operator(self, loan_id):
        """ Подтверждение заявки оператором """
        return self.__get_zaymigo_api().confirm_by_operator(
            loan_id
        )

    def approve_loan_to_date(self, loan_id, date):
        """ Выдача займа """
        return self.__get_zaymigo_api().approve_loan_to_date(
            loan_id,
            date
        )

    def cancel_withdraw(self, loan_id):
        """ Отмена выдачи """
        return self.__get_zaymigo_api().cancel_withdraw(
            loan_id,
        )

    def __get_zaymigo_api(self):
        return Zaymigo(
            self.web_driver.domain,
            self.web_driver.login,
            self.web_driver.password
        )
