import time
from random import randint


class CardGenerator:
    def __init__(self):
        pass

    def get_nunber(self):
        return f"4276{randint(1000, 9999)}{randint(1000, 9999)}{randint(1000, 9999)}"

    def get_holder(self):
        return "MAESTRO"

    def get_date(self):
        return f"12/24"
