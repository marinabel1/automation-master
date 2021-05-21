# encoding: utf-8

import time
from api.LoanApplication import LoanApplication
from borrow.newbie.steps.base import Base
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# Подтверждение займа
class Step4(Base):
    # Код из SMS
    # У инпута нет name!!!
    # ToDo: на форме этот элемент без name
    # SELECTOR_INPUT_SMS_CODE = "//*[@name='code']"

    SELECTOR_INPUT_SMS_CODE = "//div[contains(concat(' ', @class, ' '), ' loan-information__code ')]//input"

    SELECTOR_FIELD_SMS_CODE = f"{SELECTOR_INPUT_SMS_CODE}{Base.ANCESTOR_FIELD_SELECTOR}"
    SELECTOR_ERROR_SMS_CODE = f"{SELECTOR_FIELD_SMS_CODE}{Base.ERROR_FIELD_SELECTOR}"

    # Счётчик "Отправить код повторно"
    SELECTOR_RESEND_COUNTER = f"//*[@class='percent']"
    # Отправить повторно
    SELECTOR_RESEND_LINK = f"//*[@class='link']"

    def fill_all(self, loan_application):
        # ToDo: на форме этот элемент без name
        # super().waiting_for_input_appear_on_page('code')

        try:
            WebDriverWait(self.web_driver, 100).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    self.SELECTOR_INPUT_SMS_CODE
                ))
            )
        except TimeoutException:
            self.web_driver.quit()
            raise Exception("Expected page is not loaded")

        super().print_step_name()

        time.sleep(2)
        confirmation_code = self.__get_confirmation_code(loan_application.id)

        self.find_element(self.SELECTOR_INPUT_SMS_CODE).send_keys(confirmation_code)

        time.sleep(1)

        self.find_element(super().BUTTON_NEXT_SELECTOR).click()

        self.save_screenshot()
        self.log_browser_console()



    def __get_confirmation_code(self, loan_application_id):
        return super().get_loan_application_api().get_confirmation_code(
            loan_application_id,
            LoanApplication.CONFIRMATION_TYPE_AGREEMENT_CONFIRM
        )
