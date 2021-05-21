class Contact:
    """ Модель дополнительного контакта """

    def __init__(
            self,
            contact_type,
            phone,
            name=None
    ):
        self.contact_type = contact_type
        self.phone = phone
        self.name = name

    def __repr__(self):
        return "<%s instance at %s>" % (self.__class__.__name__, id(self))

    def __str__(self):
        return f"Доп. контакт: {self.phone} - {self.name}"
