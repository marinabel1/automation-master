class Borrow:

    def __init__(self, loan_application_form=None):
        self.loan_application_form = loan_application_form

    def help(self):
        pass


class Newbie:
    def __init__(self):
        pass

    def help(self):

        return "Newbie"


class Repeater:
    def __init__(self):
        pass

    def help(self):
        return "Repeater"
