class Card:
    """ Модель банковской карты """

    def __init__(
            self,
            number,
            holder,
            date
    ):
        self.number = number
        self.holder = holder
        self.date = date

    def __repr__(self):
        return "<%s instance at %s>" % (self.__class__.__name__, id(self))

    def __str__(self):
        return f"Карта: {self.number}, {self.holder} до {self.date}"
