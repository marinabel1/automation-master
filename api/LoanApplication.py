# encoding: utf-8
from pprint import pprint

from api.Base import Base


class LoanApplication(Base):
    # Код подтверждения на первом шаге анкеты
    CONFIRMATION_TYPE_PERSONAL_INFO_CONFIRM = 'personal_info'
    # Код подтверждения при подписании оферты
    CONFIRMATION_TYPE_AGREEMENT_CONFIRM = 'agreement'

    def __init__(self, domain='zver480011.develz.ru', login=None, password=None):
        super().__init__('loan-application.' + domain, '/rpc/test', login, password)

    def get_loan_application_id(self, php_session_id):
        cookies = {'PHPSESSID': php_session_id}

        result = self.run("getStatus", cookies=cookies, path='/rpc/v1')

        if 'data' not in result:
            raise ValueError(f"No data key in response.result:\n\t{result}")
        if 'loan_application' not in result['data']:
            raise ValueError(f"No loan_application key in response.result.data:\n\t{result}")
        if 'id' not in result['data']['loan_application']:
            raise ValueError(f"No id key in response.result.data.loan_application:\n\t{result}")

        return result['data']['loan_application']['id']

    def get_borrower_ids(self, php_session_id, tid):
        cookies = {
            'PHPSESSID': php_session_id,
            'tid': tid
        }

        result = self.run("getStatus", cookies=cookies, path='/rpc/v1')

        if 'data' not in result:
            raise ValueError(f"No data key in response.result:\n\t{result}")
        if 'loan_application' not in result['data']:
            raise ValueError(f"No loan_application key in response.result.data:\n\t{result}")
        if 'borrower' not in result['data']['loan_application']:
            raise ValueError(f"No id key in response.result.data.loan_application:\n\t{result}")
        if 'id' not in result['data']['loan_application']['borrower']:
            raise ValueError(f"No id key in response.result.data.loan_application.borrower:\n\t{result}")
        if 'uuid' not in result['data']['loan_application']['borrower']:
            raise ValueError(f"No uuid key in response.result.data.loan_application.borrower:\n\t{result}")

        borrower = result['data']['loan_application']['borrower']

        return {'id': borrower['id'], 'uuid': borrower['uuid']}

    def get_confirmation_code(self, loan_application_id, confirmation_type):
        result = self.run(
            "getConfirmationCode",
            {
                "loan_application_id": loan_application_id,
                "type": confirmation_type
            }
        )

        if 'result' not in result:
            raise ValueError(f"No result key in response.result:\n\t{result}")
        if 'code' not in result['result']:

            raise ValueError(f"No code key in response.result.result:\n\t{result}")

        return result['result']['code']

    def get_loan_id(self, loan_application_id):
        result = self.run(
            "getLoanId",
            {
                "loan_application_id": loan_application_id
            }
        )

        if 'result' not in result:
            raise ValueError(f"No result key in response:\n\t{result}")
        if 'result' not in result:
            raise ValueError(f"No result key in response.result:\n\t{result}")
        if 'loan_id' not in result['result']:
            raise ValueError(f"No loan_id key in response.result.result:\n\t{result}")

        return result['result']['loan_id']
