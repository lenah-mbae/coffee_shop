from order import order

class coffee:
    def __init__(self, name):
        self.name = name
        self._order = []

    @property
    def __init(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1<= len(value) <= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        
    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        coffee_orders = self.orders()
        if coffee_orders:
            return sum(order.price for order in coffee_orders) / len(coffee_orders)
        return 0
