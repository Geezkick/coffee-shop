from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers and coffees
alice = Customer("Alice")
bob = Customer("Bob")
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create some orders
order1 = alice.create_order(latte, 5.0)
order2 = alice.create_order(espresso, 3.5)
order3 = bob.create_order(latte, 4.5)

# Test relationships
print(f"Alice's orders: {[order.price for order in alice.orders()]}")
print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")
print(f"Latte's orders: {[order.price for order in latte.orders()]}")
print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")
print(f"Latte's number of orders: {latte.num_orders()}")
print(f"Latte's average price: {latte.average_price()}")
print(f"Most aficionado for Latte: {Customer.most_aficionado(latte).name}")