# tests/customer_test.py
import pytest
from customer import Customer
from coffee import Coffee


def test_customer_init():
    c = Customer("Alice")
    assert c.name == "Alice"

    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("A" * 16)


def test_customer_set_name():
    c = Customer("Bob")
    c.name = "Jane"
    assert c.name == "Jane"
    with pytest.raises(ValueError):
        c.name = ""


def test_customer_orders_and_coffees():
    c = Customer("Chris")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    c.create_order(latte, 3.5)
    c.create_order(latte, 4.0)
    c.create_order(espresso, 5.0)

    assert len(c.orders()) == 3
    assert set(c.coffees()) == {latte, espresso}