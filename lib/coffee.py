class Coffee:
    def __init__(self, name):
        self.name = name
        print(f"Created coffee: {self.name}")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, "_name"):
            if type(new_name) == str and 3 <= len(new_name):
                self._name = new_name
            else:
                raise ValueError("Name must be 3 or more characters")
    
    def orders(self):
        
        orders_for_coffee = [order for order in Order.all if order.coffee == self]
        print(f"Orders for {self.name}: {orders_for_coffee}")
        return orders_for_coffee
     
    def customers(self):
        customer_list = list({order.customer for order in self.orders()})
        print(f"Customers who ordered {self.name}: {customer_list}")
        return customer_list
    
    def num_orders(self):
        num = len(self.orders())
        print(f"Number of orders for {self.name}: {num}")
        return num
    
    def average_price(self):
        if self.num_orders() == 0:
            print(f"No orders for {self.name}, so average price is 0.")
            return 0
        sum_prices = sum([order.price for order in self.orders()], 0)
        avg_price = sum_prices / self.num_orders()
        print(f"Average price for {self.name}: {avg_price}")
        return avg_price