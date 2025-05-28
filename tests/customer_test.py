import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            Customer(123)
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("A" * 16)

    def test_orders(self):
        self.assertEqual(len(self.customer.orders()), 1)
        self.assertEqual(self.customer.orders()[0].price, 5.0)

    def test_coffees(self):
        self.assertEqual(len(self.customer.coffees()), 1)
        self.assertEqual(self.customer.coffees()[0].name, "Latte")

    def test_create_order(self):
        new_coffee = Coffee("Espresso")
        order = self.customer.create_order(new_coffee, 3.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, new_coffee)
        self.assertEqual(order.price, 3.5)

    def test_most_aficionado(self):
        bob = Customer("Bob")
        Order(bob, self.coffee, 6.0)
        self.assertEqual(Customer.most_aficionado(self.coffee).name, "Bob")

if __name__ == '__main__':
    unittest.main()