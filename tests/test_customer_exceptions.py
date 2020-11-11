from custom_exception.customer_exception import Customer
from custom_exception.custom_exceptions import InvalidCustomerIdException, InvalidNameException, InvalidPhoneNumberFormat
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(customer_id=1000, last_name='Hardin', first_name='Grayson', phone_number='123-123-1234')

    def tearDown(self):
        del self.customer

    def test_customer_with_invalid_customer_id_given_it_exceeds_lower_boundary(self):
        with self.assertRaises(InvalidCustomerIdException) as err:
            Customer(customer_id=999, last_name='Hardin', first_name='Grayson', phone_number='123-123-1234')
        self.assertTrue('Invalid customer ID!' in str(err.exception))

    def test_customer_with_invalid_customer_id_given_it_exceeds_upper_boundary(self):
        with self.assertRaises(InvalidCustomerIdException) as err:
            Customer(customer_id=10000, last_name='Hardin', first_name='Grayson', phone_number='123-123-1234')
        self.assertTrue('Invalid customer ID!' in str(err.exception))

    def test_customer_with_invalid_last_name(self):
        with self.assertRaises(InvalidNameException) as err:
            Customer(customer_id=1000, last_name='4', first_name='Grayson', phone_number='123-123-1234')
        self.assertTrue('Invalid name!' in str(err.exception))

    def test_customer_with_invalid_first_name(self):
        with self.assertRaises(InvalidNameException) as err:
            Customer(customer_id=1000, last_name='Hardin', first_name='4', phone_number='123-123-1234')
        self.assertTrue('Invalid name!' in str(err.exception))

    def test_customer_with_invalid_phone_number(self):
        with self.assertRaises(InvalidPhoneNumberFormat) as err:
            Customer(customer_id=1000, last_name='Hardin', first_name='Grayson', phone_number='123-123-12345')
        self.assertTrue('Invalid phone number!' in str(err.exception))

# Valid Tests
    def test_customer_id_with_valid_all_valid_attributes(self):
        variable = Customer(customer_id=1000, last_name='Hardin', first_name='Grayson', phone_number='123-123-1234')
        self.assertEqual(variable.customer_id, 1000)

    def test_customer_str(self):
        expected = 'The Customer ID is: 1000 The last name is: Hardin The first name is: Grayson The phone number is: 123-123-1234'
        self.assertEqual(self.customer.__str__(), expected)


if __name__ == '__main__':
    unittest.main()
