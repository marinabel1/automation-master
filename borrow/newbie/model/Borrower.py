class Borrower:
    """ Модель заёмщика """

    def __init__(
            self,
            phone,
            email=None,
            surname=None,
            name=None,
            patronymic=None,
            gender=None,
            birth_day=None,
            birth_place=None,
            passport=None,
            address_register=None,
            address_real=None,
            contacts=None,
            card=None
    ):
        self.id = None
        self.uuid = None
        self.password = None,
        self.phone = phone
        self.email = email
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.gender = gender
        self.birth_day = birth_day
        self.birth_place = birth_place
        self.passport = passport
        self.address_register = address_register
        self.address_real = address_real
        self.contacts = contacts
        self.card = card

    def __repr__(self):
        return "<%s instance at %s>" % (self.__class__.__name__, id(self))

    def __str__(self):
        result = f"Телефон: {self.phone}\n\n"
        result += f"Фамилия: {self.surname}\n"
        result += f"Имя: {self.name}\n"
        result += f"Отчество: {self.patronymic}\n"
        result += f"Email: {self.email}\n"
        result += f"----------\n\n"
        result += f"Пол: {self.gender}\n"
        result += f"Дата рождения: {self.birth_day}\n"
        result += f"Место рождения: {self.birth_place}\n"
        result += f"{self.passport}\n"
        result += f"{self.address_register}\n"
        result += f"{self.address_real}\n"
        result += f"----------\n\n"
        result += f"{self.contacts[0]}\n"
        result += f"----------\n\n"
        result += f"{self.card}\n"

        return result
