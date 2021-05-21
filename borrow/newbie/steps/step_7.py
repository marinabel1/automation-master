# encoding: utf-8

import time
from borrow.newbie.steps.base import Base
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Step7(Base):
    """ Подписание оферты """

    SELECTOR_INPUT_CARD_NUMBER = "//*[@name='cardNumber']"
    SELECTOR_INPUT_CARD_HOLDER = "//*[@name='holderName']"
    SELECTOR_INPUT_CARD_DATE = "//*[@name='expDate']"

    BUTTON_SIGN_SELECTOR = "//button[contains(text(), ' Соглашаюсь и подписываю')]"

    # На странице подписания оферты
    def fill_all(self, loan_application):
        try:
            WebDriverWait(self.web_driver, 100).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//div[contains(concat(' ', @class, ' '), ' info--approve ')]"
                ))
            )
        except TimeoutException:
            self.web_driver.quit()
            raise Exception("Expected page is not loaded")

        super().print_step_name()
        time.sleep(10)

        # self.find_element(
        #     "//div[contains(concat(' ', @class, ' '), ' loan-step__agreement ')]"
        #     + "//span[contains(concat(' ', @class, ' '), ' checkbox__element ')]"
        # ).click()
        self.find_element(self.BUTTON_SIGN_SELECTOR).click()

        self.save_screenshot()
        self.log_browser_console()
