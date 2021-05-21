# encoding: utf-8

from api.LoanApplication import LoanApplication
from api.Borrower import Borrower
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from string import digits


class Base:
    ANCESTOR_FIELD_SELECTOR = "/ancestor::div[contains(concat(' ', @class, ' '), ' field ')][1]"
    ERROR_FIELD_SELECTOR = "//div[contains(concat(' ', @class, ' '), ' field__error ')][1]"
    BUTTON_NEXT_SELECTOR = "//button[contains(text(), 'Продолжить')]"
    BUTTON_BACK_SELECTOR = "//button[contains(concat(' ', @class, ' '), ' button--back ')][1]"

    def __init__(self, web_driver):
        self.web_driver = web_driver

    def get_active_tab(self):
        """Получение текущей активной вкладки на странице анкеты

        Returns:
        str: Текст на активной вкладке

        """

        active_tab = self.find_element("//*[contains(concat(' ', @class, ' '), ' loan-progress-bar__active ')][1]")
        result = active_tab.text.replace("\n", "").replace(".", "").translate(str.maketrans('', '', digits))
        return result

    def waiting_for_input_appear_on_page(self, input_name):
        """ Ожидание появления на странице элемента input с нужным значением аттрибута name"""

        try:
            WebDriverWait(self.web_driver, 100).until(
                EC.presence_of_element_located((By.NAME, input_name))
            )
        except TimeoutException:
            self.web_driver.quit()
            raise Exception("Expected page is not loaded")

    def find_element(self, element):
        """"Получить элемент по XPath

        Returns:
        str: Текст на активной вкладке

        """

        return self.web_driver.find_element_by_xpath(element)

    def fill_element(self, xpath, value):
        """Заполнить элемент input значением"""

        self.find_element(xpath).send_keys(value)

    def __get_step_name(self):
        return self.__class__.__name__

    def print_step_name(self):
        print(f"\nProcessing: {self.__get_step_name()}")

    def get_loan_application_api(self):
        return LoanApplication(
            self.web_driver.domain,
            self.web_driver.login,
            self.web_driver.password
        )

    def get_borrower_api(self):
        return Borrower(
            self.web_driver.domain,
            self.web_driver.login,
            self.web_driver.password
        )

    def save_screenshot(self):
        file_name = f"{self.__get_step_name()}.png"
        self.web_driver.save_screenshot(f"{self.web_driver.result_path}/{file_name}")

    def log_browser_console(self):
        browser_log = self.web_driver.get_log('browser')
        if browser_log:
            log_file = f"{self.web_driver.result_path}/{self.__get_step_name()}_browser_log.txt"
            print('-Console log in browser: ')
            print('------------------------')
            for entry in browser_log:
                print(entry)
                with open(log_file, 'a') as f:
                    print(entry, file=f)
            print('------------------------')
