# encoding: utf-8

import requests
from api.Base import Base


class TestTool(Base):
    PAYMENT_SYSTEM_RAPIDA = 'rapida'
    PAYMENT_SYSTEM_YANDEX = 'yandex'
    PAYMENT_SYSTEM_TINKOFF = 'tinkoff'
    PAYMENT_SYSTEM_CONTACT = 'contact'

    def __init__(self, domain='zver480011.develz.ru', login=None, password=None):
        super().__init__('test-tool.' + domain, '/rpc/test', login, password)

    def pay(self, payment_system, loan_id, pay_sum, original_sum=None):
        params = {
            "payment_system": payment_system,
            "loan_id": loan_id,
            "sum": pay_sum
        }

        if original_sum:
            params["original_sum"] = original_sum

        result = self.run("pay", params)

        if 'result' not in result:
            raise ValueError(f"No result key in response.result:\n\t{result}")
        if 'result' not in result['result']:
            raise ValueError(f"No uuid key in response.result.result:\n\t{result}")

        return result['result']['result']
