# tests/order_test.py
import pytest
from order import Order
from customer import Customer
from coffee import Coffee


def test_order_init():
    c = Customer("Paul")
    coffee = Coffee("Flat White")
    o = Order(c, coffee, 3.0)
    assert o.customer == c
    assert o.coffee == coffee
    assert o.price == 3.0

    with pytest.raises(TypeError):
        Order("NotCustomer", coffee, 3.0)
    with pytest.raises(TypeError):
        Order(c, "NotCoffee", 3.0)
    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)
