"""
Program: customer_class.py
Author: Grayson Hardin
Last date modified: 11/1/2020
This takes in a list of names, customer id and various contact info. The program also shows examples of a proper input and an improper input.
"""

from custom_exception.custom_exceptions import InvalidCustomerIdException, InvalidNameException, InvalidPhoneNumberFormat


class Customer:
    def __init__(self, customer_id, last_name, first_name, phone_number):
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number

        if self.customer_id < 1000 or self.customer_id > 9999:
            raise InvalidCustomerIdException

        if not isinstance(self.last_name, str) or not isinstance(self.first_name, str):
            raise InvalidNameException

        if len(phone_number) != 12:
            raise InvalidPhoneNumberFormat

    def __str__(self):
        return 'The Customer ID is: ' + str(self.customer_id) + ' The last name is: ' + str(
            self.last_name) + ' The first name is: ' + str(self.first_name) + ' The phone number is: ' + str(
            self.phone_number)


try:
    Customer(customer_id=999, last_name='Hardin', first_name='Grayson', phone_number='123-123-1234')

except:
    print('Invalid customer ID!')

try:
    Customer(customer_id=1000, last_name='123', first_name='Grayson', phone_number='123-123-1234')

except:
    print('Invalid name!')

try:
        Customer(customer_id=1000, last_name='Hardin', first_name='123', phone_number='123-123-1234')
except:
    print('Invalid name!')



try:
    Customer(customer_id=1000, last_name='Hardin', first_name='Grayson', phone_number='123-123-12342')

except:
    print('Invalid phone number!')

customer1 = Customer(1000, 'Ruiz', 'Matthew', '515-313-1519')
print(customer1.__str__())
