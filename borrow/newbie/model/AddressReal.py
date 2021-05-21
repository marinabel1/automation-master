# encoding: utf-8
from borrow.newbie.model.Address import Address


class AddressReal(Address):
    """ Модель адреса проживания """

    def __repr__(self):
        return "<%s instance at %s>" % (self.__class__.__name__, id(self))

    def __str__(self):
        result = f"Адрес проживания:\n\n"
        result += f"  Регион: {self.region}\n"
        result += f"  Город: {self.city}\n"
        result += f"  Улица: {self.street}\n"
        result += f"  Дом: {self.house}\n"
        result += f"  Корпус: {self.block}\n"
        result += f"  Квартира: {self.flat}\n"

        return result
