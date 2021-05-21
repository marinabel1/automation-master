from pprint import pprint

import time
import pathlib
import os
from datetime import datetime, date
from pathlib import Path
from borrow.newbie.model.LoanApplication import LoanApplication
from webdriver.webdriver import WebDriver
from api.LoanApplication import LoanApplication as LoanApplicationApi
from api.Zaymigo import Zaymigo as ZaymigoApi
from api.TestTool import TestTool as TestToolApi


web_driver = WebDriver(
    browser=WebDriver.BROWSER_CHROME,
    domain="pre-prod.develz.ru",
    start_page="borrow.pre-prod.develz.ru",
    login="zaymigo",
    password="CC4d9ngpX4jvJj2U",
    # mobileEmulation=WebDriver.MOBILE_GALAXY_S5,
    isHeadless=True
).get_driver()

result_path = f"{pathlib.Path().absolute()}/results/{os.path.basename(__file__)}/{datetime.now().strftime('%Y/%m/%d/%H_%M_%S')}/"
Path(result_path).mkdir(parents=True, exist_ok=True)
web_driver.result_path = result_path

loan_application = LoanApplication(
    term=12,
    amount=8000
)
loan_application.id = 306634


data_file = f"{web_driver.result_path}/data.txt"
with open(data_file, 'a') as f:
    print(loan_application, file=f)


##############################################################
# 2. Одобрение заявки оператором
##############################################################

loanApplicationApi = LoanApplicationApi(
    web_driver.domain,
    web_driver.login,
    web_driver.password
)

loan_application.loan_id = loanApplicationApi.get_loan_id(loan_application.id)
print("Loan application ID: %s" % loan_application.id)
print("Loan ID: %s" % loan_application.loan_id)

with open(data_file, 'a') as f:
    print(f"\nloan_id: {loan_application.loan_id}", file=f)

zaymigoApi = ZaymigoApi(
    web_driver.domain,
    web_driver.login,
    web_driver.password
)

# zaymigoApi.approve_by_operator(loan_application.loan_id)
# print("approve_by_operator done!")

##############################################################
# 3. Выдача займа
##############################################################

zaymigoApi.approve_loan_to_date(
    loan_application.loan_id,
    date.today().strftime('%Y-%m-%dT%H:%M:%SZ')
)
print("approve_loan_to_date done!")

##############################################################
# 4. Оплата займа
##############################################################

TestToolApi(
    web_driver.domain,
    web_driver.login,
    web_driver.password
).pay(
    TestToolApi.PAYMENT_SYSTEM_TINKOFF,
    loan_application.loan_id,
    loan_application.amount
)
print("pay done")
