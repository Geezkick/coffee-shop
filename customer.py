class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name  # Use setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be 1-15 characters")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order._orders if order.customer == self]

    def coffees(self):
        from coffee import Coffee
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        from order import Order
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        order = Order(self, coffee, price)
        Order._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee
        from order import Order
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        customer_spending = {}
        for order in coffee.orders():
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer, 0) + order.price
        if not customer_spending:
            return None
        return max(customer_spending.items(), key=lambda x: x[1])[0]