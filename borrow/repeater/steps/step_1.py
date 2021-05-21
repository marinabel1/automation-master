# encoding: utf-8

import time
from borrow.newbie.steps.base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Step1(Base):
    """ 4. Получение денег: Данные карты """

    SELECTOR_INPUT_CARD_NUMBER = "//*[@name='cardNumber']"
    SELECTOR_INPUT_CARD_HOLDER = "//*[@name='holderName']"
    SELECTOR_INPUT_CARD_DATE = "//*[@name='expDate']"

    # На странице подписания оферты
    def fill_all(self, loan_application):
        super().waiting_for_input_appear_on_page('cardNumber')
        super().print_step_name()

        card = loan_application.borrower.card

        self.find_element(self.SELECTOR_INPUT_CARD_NUMBER).send_keys(card.number)
        self.find_element(self.SELECTOR_INPUT_CARD_HOLDER).send_keys(card.holder)
        self.find_element(self.SELECTOR_INPUT_CARD_DATE).send_keys(card.date)

        self.find_element(super().BUTTON_NEXT_SELECTOR).click()

        self.save_screenshot()
        self.log_browser_console()
