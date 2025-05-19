from customer import Customer
from coffee import Coffee
from order import Order

# Debug examples
c1 = Customer("Alice")
c2 = Customer("Bob")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

order1 = Order(c1, coffee1, 5.5)
order2 = Order(c1, coffee2, 3.5)
order3 = Order(c2, coffee1, 4.0)

print(c1.orders())
print(coffee1.customers())
print(coffee1.num_orders())
print(coffee1.average_price())
print(Customer.most_aficionado(coffee1))