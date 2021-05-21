# encoding: utf-8

class Address:
    """ Абстрактная модель адреса """

    def __init__(
            self,
            region,
            city,
            street=None,
            house=None,
            block=None,
            flat=None,
    ):
        self.region = region
        self.city = city
        self.street = street
        self.house = house
        self.block = block
        self.flat = flat
