from coffee import Coffee
from customer import Customer


if __name__ == "__main__":

    espresso = Coffee("Espresso")
    latte = Coffee("cappucino")

   
    john = Customer("John")
    jane = Customer("Jane")

    
    john_order = john.create_order(espresso, 5.0)
    jane_order = jane.create_order(latte, 4.5)

    # Testing Coffee methods
    espresso.orders()
    espresso.customers()
    espresso.num_orders()
    espresso.average_price()

    latte.orders()
    latte.customers()
    latte.num_orders()
    latte.average_price()

    # Testing Customer methods
    john.orders()
    john.coffees()
    jane.orders()
    jane.coffees()