class Passport:
    """ Модель паспортные данные заёмщика """

    def __init__(
            self,
            series=None,
            number=None,
            issue_date=None,
            issuer_code=None,
            issuer=None
    ):
        self.series = series
        self.number = number
        self.issue_date = issue_date
        self.issuer_code = issuer_code
        self.issuer = issuer

    def __repr__(self):
        return "<%s instance at %s>" % (self.__class__.__name__, id(self))

    def __str__(self):
        result = f"Паспорт:\n"
        result += f"  Серия/номер: {self.series} {self.number}\n"
        result += f"  Выдан: {self.issue_date} {self.issue_date}\n"
        result += f"  Код подразделения: {self.issuer_code}\n"

        return result
