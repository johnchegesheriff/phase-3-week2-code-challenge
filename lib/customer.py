
from lib.coffee import Coffee
from lib.order import Order


class Customer:
    def __init__(self, name):
        # Check name validity
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name
        self._orders = []  # Track orders 
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (1 <= len(new_name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = new_name
    
    def orders(self):
        return self._orders
    
    def coffees(self):
        return list({order.coffee for order in self._orders})
    
    def create_order(self, coffee, price):
        if isinstance(coffee, Coffee) and isinstance(price, (int, float)) and 1.0 <= price <= 10.0:
            order = Order(self, coffee, price)
            self._orders.append(order)
            coffee._orders.append(order)
            return order
        else:
            raise ValueError("Invalid coffee or price value.")
        


customer1 = Customer("Alice")
customer2 = Customer("Bob")
print(customer1.name)

coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")
print(coffee1.name)

order1 = customer1.create_order(coffee1, 5.0)
order2 = customer2.create_order(coffee1, 6.0)
order3 = customer1.create_order(coffee2, 7.0)

