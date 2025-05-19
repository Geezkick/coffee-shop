# tests/coffee_test.py
import pytest
from coffee import Coffee
from customer import Customer
from order import Order


def test_coffee_init():
    c = Coffee("Latte")
    assert c.name == "Latte"
    with pytest.raises(ValueError):
        Coffee("A")


def test_coffee_orders_and_customers():
    c = Coffee("Mocha")
    cust1 = Customer("Sam")
    cust2 = Customer("Pat")
    Order(cust1, c, 3.5)
    Order(cust2, c, 4.0)
    assert len(c.orders()) == 2
    assert set(c.customers()) == {cust1, cust2}


def test_coffee_aggregates():
    c = Coffee("Americano")
    cust = Customer("Lara")
    Order(cust, c, 2.0)
    Order(cust, c, 4.0)
    assert c.num_orders() == 2
    assert c.average_price() == 3.0