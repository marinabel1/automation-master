# encoding: utf-8
from borrow.newbie.steps.base import Base



class Step4(Base):
    """ 3. Личная информация: Контактная информация """

    SELECTOR_INPUT_ADDITIONAL_PHONE = "//input[@name='additionalPhone']"
    SELECTOR_INPUT_ADDITIONAL_NAME = "//input[@name='additionalName']"

    # На странице "Личная информация" нажимаем "Продолжить" без изменений
    def fill_all(self, loan_application):
        super().waiting_for_input_appear_on_page('additionalPhone')
        super().print_step_name()

        contact = loan_application.borrower.contacts[0]

        self.find_element(self.SELECTOR_INPUT_ADDITIONAL_PHONE).send_keys(contact.phone)
        self.find_element(self.SELECTOR_INPUT_ADDITIONAL_NAME).send_keys(contact.name)

        self.find_element(super().BUTTON_NEXT_SELECTOR).click()

        self.save_screenshot()
        self.log_browser_console()
