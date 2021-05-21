import random
from pprint import pprint


class CityGenerator:
    def get_city(self):
        city = random.choice(open('/generator/name\\files\dist.city', "r", 100000, encoding="utf-8").read().splitlines())
        return city


    def get_cityCode(self):
        if self.get_city == "Москва":
            cityCode = "770-001"
            return cityCode
        elif self.get_city == "Санкт-Петербург":
            cityCode = "780-001"
            return cityCode
        elif self.get_city == "Новосибирск":
            cityCode = "540-001"
            return cityCode
        elif self.get_city == "Екатеринбург":
            cityCode = "660-001"
            return cityCode
        elif self.get_city == "Казань":
            cityCode = "160-001"
            return cityCode
        elif self.get_city == "Нижний Новгород":
            cityCode = "520-001"
            return cityCode
        elif self.get_city == "Челябинск":
            cityCode = "740-001"
            return cityCode
        elif self.get_city == "Самара":
            cityCode = "	630-001"
            return cityCode
        elif self.get_city == "Омск":
            cityCode = "550-001"
            return cityCode
        elif self.get_city == "Ростов-на-Дону":
            cityCode = "610-001"
            return cityCode
        elif self.get_city == "Уфа":
            cityCode = "020-001"
            return cityCode
        elif self.get_city == "Красноярск":
            cityCode = "241-001"
            return cityCode
        elif self.get_city == "Воронеж":
            cityCode = "360-001"
            return cityCode
        elif self.get_city == "Пермь":
            cityCode = "590-001"
            return cityCode
        elif self.get_city == "Волгоград":
            cityCode = "340-001"
            return cityCode
