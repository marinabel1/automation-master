from pprint import pprint

import time
import pathlib
import os
from datetime import datetime, date
from pathlib import Path
from borrow.repeater.model.Passport import Passport
from borrow.repeater.model.Card import Card
from borrow.repeater.model.Borrower import Borrower
from borrow.repeater.model.LoanApplication import LoanApplication
from generator.name.name import NameGenerator
from generator.phone.phone import PhoneGenerator
from generator.passport.passport import PassportGenerator
from generator.card.card import CardGenerator
from webdriver.webdriver import WebDriver
from borrow.repeater.steps.login import Login
from borrow.repeater.steps.step_1 import Step1
from borrow.repeater.steps.step_2 import Step2
from borrow.repeater.steps.step_3 import Step3
from borrow.repeater.steps.step_4 import Step4


web_driver = WebDriver(
    browser=WebDriver.BROWSER_CHROME,
    domain="andrey.develz.ru",
    start_page="borrow.andrey.develz.ru",
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

card = Card(
    number=cards_generator.get_nunber(),
    holder=cards_generator.get_holder(),
    date=cards_generator.get_date()
)

borrower = Borrower(
    phone='+79907087246',
    password='174778',
    passport=passport,
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
# 0. Авторизация
##############################################################

start_time = time.time()
Login(web_driver).fill_all(loan_application)
print("--- %.6f seconds ---" % (time.time() - start_time))

##############################################################
# 1. Заполнение анкеты повторника
##############################################################

start_time = time.time()
Step1(web_driver).fill_all(loan_application)
print("--- %.6f seconds ---" % (time.time() - start_time))

# start_time = time.time()
# Step2(web_driver).fill_all(loan_application)
# print("--- %.6f seconds ---" % (time.time() - start_time))
#
# start_time = time.time()
# Step3(web_driver).fill_all(loan_application)
# print("--- %.6f seconds ---" % (time.time() - start_time))
#
# start_time = time.time()
# Step4(web_driver).fill_all(loan_application)
# print("--- %.6f seconds ---" % (time.time() - start_time))
