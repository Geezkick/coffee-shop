import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.coffee = Coffee("Latte")
        self.customer = Customer("Alice")
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            Coffee(123)
        with self.assertRaises(ValueError):
            Coffee("Ab")
        with self.assertRaises(AttributeError):
            self.coffee.name = "NewName"

    def test_orders(self):
        self.assertEqual(len(self.coffee.orders()), 1)
        self.assertEqual(self.coffee.orders()[0].price, 5.0)

    def test_customers(self):
        self.assertEqual(len(self.coffee.customers()), 1)
        self.assertEqual(self.coffee.customers()[0].name, "Alice")

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 1)

    def test_average_price(self):
        Order(Customer("Bob"), self.coffee, 3.0)
        self.assertEqual(self.coffee.average_price(), 4.0)

if __name__ == '__main__':
    unittest.main()