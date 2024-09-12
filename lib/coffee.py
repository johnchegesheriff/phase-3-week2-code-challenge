class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters.")
        self._name = name
        self._orders = [] 
    
    @property
    def name(self):
        return self._name  
    
    def orders(self):
        return self._orders
    
    def customers(self):
        return list({order.customer for order in self._orders})
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if self._orders:
            return sum(order.price for order in self._orders) / len(self._orders)
        return 0


