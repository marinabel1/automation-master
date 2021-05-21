from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random
import transliterate


def get_gender():
    return random.choice(('male', 'female'))


class NameGenerator:
    def __init__(self, gender=None):
        if gender is None:
            self.gender = get_gender()
        else:
            self.gender = gender

        self.surname = None
        self.name = None
        self.patronymic = None
        self.email = None

        self.files = {
            'surname:female': self.__get_dict_path('dist.female.surname'),
            'name:female': self.__get_dict_path('dist.female.name'),
            'patronymic:female': self.__get_dict_path('dist.female.patronymic'),

            'surname:male': self.__get_dict_path('dist.male.surname'),
            'name:male': self.__get_dict_path('dist.male.name'),
            'patronymic:male': self.__get_dict_path('dist.male.patronymic'),
        }

    def __get_dict_path(self, filename):
        return abspath(join(dirname(__file__), 'files', filename))

    def __get_random_line(self, filename):
        lines = open(filename, "r", encoding="utf-8").read().splitlines()
        return random.choice(lines)

    def get_gender(self):
        return self.gender

    def get_surname(self, gender=None):
        if gender is None:
            gender = self.gender
        if gender not in ('male', 'female'):
            raise ValueError("Only 'male' and 'female' are supported as gender")

        self.surname = self.__get_random_line(self.files['surname:%s' % gender]).capitalize()

        return self.surname

    def get_name(self, gender=None):
        if gender is None:
            gender = self.gender
        if gender not in ('male', 'female'):
            raise ValueError("Only 'male' and 'female' are supported as gender")
        self.name = self.__get_random_line(self.files['name:%s' % gender]).capitalize()

        return self.name

    def get_patronymic(self, gender=None):
        if gender is None:
            gender = self.gender
        if gender not in ('male', 'female'):
            raise ValueError("Only 'male' and 'female' are supported as gender")
        self.patronymic = self.__get_random_line(self.files['patronymic:%s' % gender]).capitalize()

        return self.patronymic

    def get_full_name(self, gender=None):
        if gender is None:
            gender = get_gender()
        if gender not in ('male', 'female'):
            raise ValueError("Only 'male' and 'female' are supported as gender")
        return f"{self.get_surname(gender)} {self.get_name(gender)} {self.get_patronymic(gender)}"

    def get_email(self, domain="test.ru"):
        self.email = \
            transliterate.translit(self.name, reversed=True).lower() \
            + "." \
            + transliterate.translit(self.surname, reversed=True).lower() \
            + "@" \
            + domain

        return self.email

    def get_birth_day(self):
        return f"26.12.1980"

    def get_birth_place(self):
        return f"Дер. Большая Маленького р-на Какой-то области"
