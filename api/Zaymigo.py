# encoding: utf-8

from api.Base import Base


class Zaymigo(Base):
    def __init__(self, domain='zver480011.develz.ru', login=None, password=None):
        super().__init__(domain, '/api/test', login, password)

    def approve_by_operator(self, loan_id):
        result = self.run(
            "approveByOperator",
            {
                "loanId": loan_id
            }
        )

        if 'result' not in result['result']:
            raise ValueError(f"No uuid key in response.result.result:\n\t{result}")

        return result['result']['result']

    def approve_loan_to_date(self, loan_id, date):
        result = self.run(
            "approveLoanToDate",
            {
                "loanId": loan_id,
                "date": date
            }
        )

        if 'status' not in result:
            raise ValueError(f"No status key in response.result:\n\t{result}")

        return result['status']

    def cancel_withdraw(self, loan_id):
        result = self.run(
            "cancelWithdraw",
            {
                "loanId": loan_id
            }
        )

        if 'status' not in result:
            raise ValueError(f"No status key in response.result:\n\t{result}")

        return result['status']
