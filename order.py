# order.py
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise Exception("Invalid customer")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise Exception("Invalid coffee")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise Exception("Invalid price")