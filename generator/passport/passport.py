import time
from random import randint


class PassportGenerator:
    def __init__(self):
        pass

    def get_series(self):
        return f"{randint(1000, 9999)}"

    def get_number(self):
        return f"{randint(100000, 999999)}"

    def get_issuer(self):
        return "МВД России по России в России"

    def get_issuer_code(self):
        return f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}-{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"

    def get_issue_date(self):
        return f"20.10.2010"
