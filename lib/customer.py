class Customer:
    def __init__(self, name):
        self.name = name
        print(f"Created customer: {self.name}")

    @property
    def name(self):
        return self._name
   
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and 1 <= len(new_name) <= 15:
            self._name = new_name
    
    def orders(self):
        customer_orders = [order for order in Order.all if order.customer == self]
        print(f"{self.name}'s orders: {customer_orders}")
        return customer_orders
     
    def coffees(self):
        customer_coffees = list({order.coffee for order in self.orders()})
        print(f"{self.name}'s coffees: {customer_coffees}")
        return customer_coffees
      
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        print(f"{self.name} created an order for {coffee.name} at ${price}")
        return new_order
