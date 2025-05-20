from customer import Customer
from coffee import Coffee
from order import Order

# Sample data for testing
alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

# Creating orders using create_order
alice.create_order(latte, 3.5)
alice.create_order(mocha, 4.5)
bob.create_order(latte, 5.0)
bob.create_order(mocha, 6.0)
bob.create_order(mocha, 7.5)

# Inspect orders
print("\n-- All Orders --")
for order in Order.all:
    print(f"{order.customer.name} ordered {order.coffee.name} for ${order.price}")

# Debugging output
print("\n-- Debug Info --")
print(f"Latte total orders: {latte.num_orders()}")
print(f"Mocha average price: ${mocha.average_price():.2f}")
print(f"Alice's coffees: {[c.name for c in alice.coffees()]}")
