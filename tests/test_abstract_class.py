from abstract_class_with_tests.abstract_class import Rider, Bicycle, Motorcycle, Car
import unittest


class MyTestCase(unittest.TestCase):
    def test_bicycle(self):
        bicycle = Bicycle('Human powered, not enclosed', '1 or 2 if tandem or a daredevil')
        self.assertEqual(bicycle.ride(), 'Human powered, not enclosed')
        self.assertEqual(bicycle.rider(), '1 or 2 if tandem or a daredevil')

    def test_motorcycle(self):
        motorcycle = Motorcycle('Engine powered, not enclosed', '1 or 2')
        self.assertEqual(motorcycle.ride(), 'Engine powered, not enclosed')
        self.assertEqual(motorcycle.rider(), '1 or 2')

    def test_car(self):
        car = Car('Engine powered, enclosed', '1 plus comfortably')
        self.assertEqual(car.ride(), 'Engine powered, enclosed')
        self.assertEqual(car.rider(), '1 plus comfortably')


if __name__ == '__main__':
    unittest.main()
