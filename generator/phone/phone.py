import time


class PhoneGenerator:
    def __init__(self):
        pass

    def generate_random_phone(self, code="990"):
        """Генерация случайного номера телефона с указанным кодом"""
        # ToDo: при вводе телефона с +7 получается +7 (799) 0хх-хх-хх
        return f"{code}{str(int(time.time()))[-7:]}"
