class Borrower:
    """ Модель заёмщика """

    def __init__(
            self,
            phone,
            password,
            passport,
            card
    ):
        self.id = None
        self.uuid = None
        self.phone = phone
        self.password = password
        self.passport = passport
        self.card = card

    def __repr__(self):
        return "<%s instance at %s>" % (self.__class__.__name__, id(self))

    def __str__(self):
        result = f"Телефон: {self.phone}\n\n"
        result += f"Пароль: {self.password}\n"
        result += f"----------\n\n"
        result += f"{self.passport}\n"
        result += f"----------\n\n"
        result += f"{self.card}\n"

        return result
