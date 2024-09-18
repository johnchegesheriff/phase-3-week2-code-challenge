class Order:

    all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price  
        Order.all.append(self)
        print(f"New order created: {self.customer.name} ordered {self.coffee.name} for ${self.price}")
     
    @property
    def price(self):
        return self._price
     
    @price.setter
    def price(self, new_price): 
        if isinstance(new_price, float) and 1.0 <= new_price <= 10.0:
            self._price = new_price
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0")

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        from customer import Customer  
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise ValueError("Invalid customer provided, must be a Customer instance.")
     
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        from coffee import Coffee  
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise ValueError("Invalid coffee provided, must be a Coffee instance.")
