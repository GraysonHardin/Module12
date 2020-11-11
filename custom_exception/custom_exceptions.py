class InvalidCustomerIdException(Exception):
    def __init__(self):
        super().__init__('Invalid customer ID!')


class InvalidNameException(Exception):
    def __init__(self):
        super().__init__('Invalid name!')


class InvalidPhoneNumberFormat(Exception):
    def __init__(self):
        super().__init__('Invalid phone number!')


