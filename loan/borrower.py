# encoding: utf-8
from api.TestTool import TestTool


class Borrower:
    def __init__(self, web_driver):
        self.web_driver = web_driver

    def pay(self, payment_system, loan_id, pay_sum, original_sum):
        """ Оплата займа """
        return self.__get_test_tool_api().pay(
            payment_system,
            loan_id,
            pay_sum,
            original_sum
        )

    def __get_test_tool_api(self):
        return TestTool(
            self.web_driver.domain,
            self.web_driver.login,
            self.web_driver.password
        )