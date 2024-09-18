from coffee import Coffee
from customer import Customer


if __name__ == "__main__":

    
    espresso = Coffee("Espresso")
    latte = Coffee("Cappuccino")  

    
    john = Customer("John")
    bob = Customer("bob")

    
    john_order = john.create_order(espresso, 5.0)  
    bob_order = bob.create_order(latte, 4.5)

    
    espresso.orders()         
    espresso.customers()      
    espresso.num_orders()     
    espresso.average_price() 

    latte.orders()           
    latte.customers()         
    latte.num_orders()       
    latte.average_price()     

   
    john.orders()   
    john.coffees()  
    bob.orders()   
    bob.coffees()  
