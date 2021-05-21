# encoding: utf-8

from api.Base import Base


class Borrower(Base):
    def __init__(self, domain='zver480011.develz.ru', login=None, password=None):
        super().__init__('borrower.' + domain, '/rpc/test', login, password)

    def get_borrower_uuid_by_phone(self, phone):
        result = self.run(
            "getBorrowerUuidByPhone",
            {
                "phone": phone
            }
        )

        if 'result' not in result:
            raise ValueError(f"No result key in response.result:\n\t{result}")
        if 'uuid' not in result['result']:
            raise ValueError(f"No uuid key in response.result.result:\n\t{result}")

        return result['result']['uuid']
