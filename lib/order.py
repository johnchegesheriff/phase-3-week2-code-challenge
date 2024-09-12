from lib.customer import Customer
from lib.coffee import Coffee


class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if hasattr(self, '_price'):
            raise AttributeError("Cannot change price once set.")
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number.")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price = float(value)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("Customer must be an instance of Customer.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be an instance of Coffee.")
        self._coffee = value


