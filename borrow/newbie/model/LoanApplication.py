class LoanApplication:
    """ Модель заявки на займ для первичника """

    def __init__(
            self,
            term=None,
            amount=None,
            borrower=None,
    ):
        self.id = None
        self.term = term
        self.amount = amount
        self.borrower = borrower
        self.number = None
        self.loan_id = None

    def __repr__(self):
        return "<%s instance at %s>" % (self.__class__.__name__, id(self))

    def __str__(self):
        result = f"Заявка на займ. Сумма: {self.amount}, срок: {self.term}\n\n"
        result += f"{self.borrower}"

        return result
