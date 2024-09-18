class Customer:
    def __init__(self, name):
        self.name = name
        print(f"Created customer: {self.name}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        from order import Order  
        customer_orders = [order for order in Order.all if order.customer == self]
        print(f"{self.name}'s orders: {customer_orders}")
        return customer_orders

    def coffees(self):
        customer_coffees = {order.coffee for order in self.orders()}
        print(f"{self.name}'s coffees: {customer_coffees}")
        return list(customer_coffees)

    def create_order(self, coffee, price):
        from order import Order  
        new_order = Order(self, coffee, price)
        print(f"{self.name} created an order for {coffee.name} at ${price}")
        return new_order
