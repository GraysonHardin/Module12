import unittest
from custom_exception.custom_exceptions import InvalidCustomerIdException, InvalidNameException, InvalidPhoneNumberFormat


class MyTestCase(unittest.TestCase):
    def test_invalid_customer_id_exception(self):
        with self.assertRaises(InvalidCustomerIdException) as err:
            raise InvalidCustomerIdException
        self.assertTrue('Invalid customer ID!' in str(err.exception))

    def test_invalid_name_exception(self):
        with self.assertRaises(InvalidNameException) as err:
            raise InvalidNameException
        self.assertTrue('Invalid name!' in str(err.exception))

    def test_invalid_phone_number_exception(self):
        with self.assertRaises(InvalidPhoneNumberFormat) as err:
            raise InvalidPhoneNumberFormat
        self.assertTrue('Invalid phone number!' in str(err.exception))


if __name__ == '__main__':
    unittest.main()
