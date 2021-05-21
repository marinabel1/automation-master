# encoding: utf-8

import random
import time
from pprint import pprint
from faker import Faker

from borrow.newbie.steps.base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from generator.name.city import CityGenerator


class Step3(Base):
    """ 2. Паспортные данные """

    SELECTOR_INPUT_BITRHDATE = "//input[@name='birthDate']"
    SELECTOR_INPUT_PASSPORTDATE = "//input[@name='issuePassDate']"
    SELECTOR_INPUT_BIRTHPLACE = "//input[@name='birthPlace']"
    SELECTOR_INPUT_PASS_SERIES = "//input[@name='passSeries']"
    SELECTOR_INPUT_PASS_NUMBER = "//input[@name='passNumber']"
    # ToDo: Поменять название поля на фронте
    SELECTOR_INPUT_PASS_ISSUER_CODE = "//input[@name='departmentCode']"
    # ToDo: Поменять название поля на фронте
    SELECTOR_INPUT_PASS_ISSUER = "//input[@name='issuedDep']"

    SELECTOR_GENDER_MALE = "//input[@name='gender' and @value='m']/ancestor::li[1]"
    SELECTOR_GENDER_FEMALE = "//input[@name='gender' and @value='f']/ancestor::li[1]"

    # ToDo: Поменять название поля на фронте
    # SELECTOR_INPUT_REGISTER_REGION = "//input[@name='regionsRegister']"
    # SELECTOR_INPUT_REGISTER_CITY = "//input[@name='cityRegister']"
    # SELECTOR_INPUT_REGISTER_STREET = "//input[@name='streetRegister']"
    # SELECTOR_INPUT_REGISTER_HOUSE = "//input[@name='houseRegister']"
    # SELECTOR_INPUT_REGISTER_BLOCK = "//input[@name='blockRegister']"
    # SELECTOR_INPUT_REGISTER_FLAT = "//input[@name='flatRegister']"

    SELECTOR_INPUT_REGISTER_REGION = "//span[text()='Регион']/ancestor::div[contains(concat(' ', @class, ' '), ' field ')][1]//input"
    SELECTOR_INPUT_REGISTER_CITY = "//span[text()='Город / Населенный пункт']/ancestor::div[contains(concat(' ', @class, ' '), ' field ')][1]//input"
    SELECTOR_INPUT_REGISTER_STREET = "//span[text()='Улица']/ancestor::div[contains(concat(' ', @class, ' '), ' field ')][1]//input"
    SELECTOR_INPUT_REGISTER_HOUSE = "//span[text()='Дом']/ancestor::div[contains(concat(' ', @class, ' '), ' field ')][1]//input"
    SELECTOR_INPUT_REGISTER_BLOCK = "//span[text()='Строение']/ancestor::div[contains(concat(' ', @class, ' '), ' field ')][1]//input"
    SELECTOR_INPUT_REGISTER_FLAT = "//span[text()='Квартира']/ancestor::div[contains(concat(' ', @class, ' '), ' field ')][1]//input"

    SELECTOR_FIRST_IN_DROPDOWN = "//ul[contains(@class, 'l-select__list')]//li[1]"

    def fill_in(self):
        super().waiting_for_input_appear_on_page('passNumber')
        super().print_step_name()

        city_generator = CityGenerator()
        city = city_generator.get_city()
        cityCode = city_generator.get_cityCode()

        fake = Faker()
        birthDate = fake.date_between(start_date='-70y', end_date='-18y').strftime('%d.%m.%Y')
        pprint('Дата рождения' + ' ' + birthDate)

        passportDate = fake.date_between(start_date='-1y', end_date='now').strftime('%d.%m.%Y')
        pprint('Дата выдачи паспорта' + ' ' + passportDate)

        passseries = random.sample(range(9), 4)
        passnumber = random.sample(range(9), 6)
        

        # birthDate = f"{birthDateList} {birthMonthList} {birthYearList}"
        # print(f"Дата рождения: {birthDate}")
        #
        # print(f"Код подразделения: {ufmsCodeList}")
        # CitySum = str.splitlines(cityList)
        # print(f"Город регистрации: {CitySum}")
        # print(f"Серия и номер паспорта: {passSeriesList} {passNumberList}")
        # path = os.path.join(os.path.dirname(__file__), '..\\listsForRandom\\')
        # dateIssuanceOfPassportSum = str.splitlines(dateIssuanceOfPassportList + monthIssuanceList + yearIssuanceOfPassportList)
        #
        # dateOfBirthField = WebDriverWait(self.web_driver, 15).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, dateOfBirthFieldSelector)))

        self.find_element(self.SELECTOR_INPUT_BITRHDATE).send_keys(birthDate)
        self.find_element(self.SELECTOR_INPUT_PASSPORTDATE).send_keys(passportDate)
        self.find_element(self.SELECTOR_INPUT_BIRTHPLACE).send_keys(city)
        self.find_element(self.SELECTOR_INPUT_PASS_SERIES).send_keys(str(passseries))
        self.find_element(self.SELECTOR_INPUT_PASS_NUMBER).send_keys(str(passnumber))
        pprint(cityCode)
        self.find_element(self.SELECTOR_INPUT_PASS_ISSUER_CODE).send_keys(str(cityCode))

        # self.find_element(ufmsCodeFieldSelector).send_keys(ufmsCodeList)
        # self.find_element(issuedPassByFieldSelector).click()
        # self.find_element(choiceFirstOption).click()
        # self.find_element(mGenderRadiobuttonSelector).click()
        # self.find_element(regCity).send_keys(CitySum)
        # time.sleep(1)
        # choiceFirstCity = WebDriverWait(self.web_driver, 3).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, choiceFirstOption)
        #     )
        # )
        # choiceFirstCity.click()
        # self.find_element(streetFieldSelector).send_keys('ул')
        # self.find_element(choiceFirstOption).click()
        # self.find_element(homeFieldSelector).send_keys('1')
        # self.find_element(choiceFirstOption).click()
        # self.find_element(flatFieldSelector).send_keys('1')
        # self.find_element(nextButtonSelector).click()
        #
        # # Если номер паспорта уже есть в сисетеме, то гененрируем новый номер
        # while True:
        #     arr = self.find_element(errorPassportNumberSelector)
        #     if len(arr) > 0:
        #         passNumberListRef = random.choice(open(os.path.join(path, 'mpassNumber.txt')).readlines())
        #         print(f"Новый номер паспорта: {passNumberListRef}")
        #         self.find_element(passNumberFieldSelector).clear()
        #         self.find_element(passNumberFieldSelector).send_keys(passNumberList)
        #         time.sleep(2)
        #         self.find_element(nextButtonSelector).click()
        #     else:
        #         break

    def fill_all(self, loan_application):
        super().waiting_for_input_appear_on_page('passNumber')
        super().print_step_name()

        # ToDo: исправить
        # Ошибка:
        # Internal error.
        # Получения статуса неавторизованным пользователем
        # или пользователем которому не принадлежит данная заявка на займ
        time.sleep(2)
        self.__store_borrower_ids(loan_application)

        borrower = loan_application.borrower
        passport = borrower.passport
        address = borrower.address_real

        self.find_element(self.SELECTOR_INPUT_BITRHDATE).send_keys(borrower.birth_day)
        self.find_element(self.SELECTOR_INPUT_BIRTHPLACE).send_keys(borrower.birth_place)

        self.find_element(self.SELECTOR_INPUT_PASSPORTDATE).send_keys(passport.issue_date)
        self.find_element(self.SELECTOR_INPUT_PASS_SERIES).send_keys(passport.series)
        self.find_element(self.SELECTOR_INPUT_PASS_NUMBER).send_keys(passport.number)

        self.find_element(self.SELECTOR_INPUT_PASS_ISSUER_CODE).send_keys(passport.issuer_code)
        self.find_element(self.SELECTOR_INPUT_PASS_ISSUER).send_keys(passport.issuer_code)

        if borrower.gender == 'female':
            self.find_element(self.SELECTOR_GENDER_FEMALE).click()

        if borrower.gender == 'male':
            self.find_element(self.SELECTOR_GENDER_MALE).click()

        self.find_element(self.SELECTOR_INPUT_REGISTER_REGION).send_keys(address.region)
        self.__select_first()

        self.find_element(self.SELECTOR_INPUT_REGISTER_CITY).send_keys(address.city)
        self.__select_first()

        self.find_element(self.SELECTOR_INPUT_REGISTER_STREET).send_keys(address.street)
        self.__select_first()

        self.find_element(self.SELECTOR_INPUT_REGISTER_HOUSE).send_keys(address.house)
        self.__select_first()

        self.find_element(self.SELECTOR_INPUT_REGISTER_BLOCK).send_keys(address.block)

        self.find_element(self.SELECTOR_INPUT_REGISTER_FLAT).send_keys(address.flat)

        self.find_element(super().BUTTON_NEXT_SELECTOR).click()

        self.save_screenshot()
        self.log_browser_console()

    def __store_borrower_ids(self, loan_application):
        php_session_id = self.web_driver.get_cookie('PHPSESSID')['value']
        tid = self.web_driver.get_cookie('tid')['value']
        print(f"PHPSESSID: {php_session_id}")
        print(f"tid: {tid}")
        borrower_ids = self.get_loan_application_api().get_borrower_ids(php_session_id, tid)
        loan_application.borrower.id = borrower_ids['id']
        loan_application.borrower.uuid = borrower_ids['uuid']

    def __select_first(self):
        """ Выбор первого элемента из выпадающего списка """
        time.sleep(1)
        WebDriverWait(self.web_driver, 50).until(
            EC.presence_of_element_located(
                (By.XPATH, self.SELECTOR_FIRST_IN_DROPDOWN)
            )
        ).click()
