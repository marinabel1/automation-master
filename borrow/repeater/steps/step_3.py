# encoding: utf-8

from borrow.newbie.steps.base import Base
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Step3(Base):
    """ Подписание оферты """

    SELECTOR_INPUT_CARD_NUMBER = "//*[@name='cardNumber']"
    SELECTOR_INPUT_CARD_HOLDER = "//*[@name='holderName']"
    SELECTOR_INPUT_CARD_DATE = "//*[@name='expDate']"

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

        self.find_element("//label[@class='checkbox__wrapper']").click()
        self.find_element(super().BUTTON_NEXT_SELECTOR).click()

        self.save_screenshot()
        self.log_browser_console()
