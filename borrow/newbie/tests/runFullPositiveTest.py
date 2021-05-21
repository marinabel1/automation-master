# -*- coding: utf-8 -*-

import time
import pathlib
import os
from datetime import datetime, date
from pathlib import Path
from borrow.newbie.model.Passport import Passport
from borrow.newbie.model.AddressRegister import AddressRegister
from borrow.newbie.model.AddressReal import AddressReal
from borrow.newbie.model.Card import Card
from borrow.newbie.model.Borrower import Borrower
from borrow.newbie.model.Contact import Contact
from borrow.newbie.model.LoanApplication import LoanApplication
from borrow.newbie.tests.UI import bench, testBench
from generator.name.name import NameGenerator
from generator.phone.phone import PhoneGenerator
from generator.passport.passport import PassportGenerator
from generator.card.card import CardGenerator
from webdriver.webdriver import WebDriver
from borrow.newbie.steps.step_1 import Step1
from borrow.newbie.steps.step_2 import Step2
from borrow.newbie.steps.step_3 import Step3
from borrow.newbie.steps.step_4 import Step4
from borrow.newbie.steps.step_5 import Step5
from borrow.newbie.steps.step_6 import Step6
from borrow.newbie.steps.step_7 import Step7
from borrow.newbie.steps.step_8 import Step8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By





web_driver = WebDriver(
    browser=WebDriver.BROWSER_CHROME,
    domain=testBench[bench] + ".develz.ru",
    start_page="borrow." + testBench[bench] + ".develz.ru",
    login="zaymigo",
    password="CC4d9ngpX4jvJj2U",
    # mobileEmulation=WebDriver.MOBILE_GALAXY_S5,
    # isHeadless=True
).get_driver()

result_path = f"{pathlib.Path().absolute()}/results/{os.path.basename(__file__)}/{datetime.now().strftime('%Y/%m/%d/%H_%M_%S')}/"
Path(result_path).mkdir(parents=True, exist_ok=True)
web_driver.result_path = result_path


passport_generator = PassportGenerator()
name_generator = NameGenerator()
phones_generator = PhoneGenerator()
cards_generator = CardGenerator()

passport = Passport(
    series=passport_generator.get_series(),
    number=passport_generator.get_number(),
    issuer=passport_generator.get_issuer(),
    issuer_code=passport_generator.get_issuer_code(),
    issue_date=passport_generator.get_issue_date()
)

contact = Contact(
    contact_type='la_friend',
    phone=phones_generator.generate_random_phone("992"),
    name=name_generator.get_full_name()
)

address_register = AddressRegister(
    region='Нижегородская',
    city='Нижний Новгород',
    street='Минина',
    house='1',
    block='',
    flat='52'
)

address_real = AddressReal(
    region='Нижегородская',
    city='Нижний Новгород',
    street='Ковровская',
    house='15',
    block='2',
    flat='4'
)

card = Card(
    number=cards_generator.get_nunber(),
    holder=cards_generator.get_holder(),
    date=cards_generator.get_date()
)

borrower = Borrower(
    phone=phones_generator.generate_random_phone(),
    gender=name_generator.get_gender(),
    surname=name_generator.get_surname(),
    name=name_generator.get_name(),
    patronymic=name_generator.get_patronymic(),
    email=name_generator.get_email(),
    birth_day=name_generator.get_birth_day(),
    birth_place=name_generator.get_birth_place(),
    passport=passport,
    address_real=address_real,
    address_register=address_register,
    contacts=[contact],
    card=card
)

loan_application = LoanApplication(
    term=12,
    amount=10000,
    borrower=borrower
)

data_file = f"{web_driver.result_path}/data.txt"
with open(data_file, 'a') as f:
    print(loan_application, file=f)

##############################################################
# 1. Заполнение анкеты первичника
##############################################################

start_time = time.time()
Step1(web_driver).fill_all(loan_application)
print("--- %.6f seconds ---" % (time.time() - start_time))

start_time = time.time()
Step2(web_driver).fill_all(loan_application)
print("--- %.6f seconds ---" % (time.time() - start_time))

start_time = time.time()
Step3(web_driver).fill_all(loan_application)
print("--- %.6f seconds ---" % (time.time() - start_time))

with open(data_file, 'a') as f:
    print(f"\nloan_application.id: {loan_application.id}", file=f)

    print(f"\nAuth data: +7{loan_application.borrower.phone} | {loan_application.borrower.password}", file=f)
    print(f"\nborrower.id: {loan_application.borrower.id}", file=f)
    print(f"\nborrower.uuid: {loan_application.borrower.uuid}", file=f)

start_time = time.time()
Step4(web_driver).fill_all(loan_application)
print("--- %.6f seconds ---" % (time.time() - start_time))

start_time = time.time()
Step5(web_driver).fill_all(loan_application)
print("--- %.6f seconds ---" % (time.time() - start_time))

start_time = time.time()
Step6(web_driver).fill_all(loan_application)
print("--- %.6f seconds ---" % (time.time() - start_time))

start_time = time.time()
Step7(web_driver).fill_all(loan_application)
print("--- %.6f seconds ---" % (time.time() - start_time))

start_time = time.time()
Step8(web_driver).fill_all(loan_application)
print("--- %.6f seconds ---" % (time.time() - start_time))

wait = WebDriverWait(web_driver, 20)
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'в личном кабинете')))
web_driver.find_element_by_link_text('в личном кабинете').click()
