def options_checker(option):
    if option == "espresso":
        make_espresso()
    if option == "cappuccino":
        make_cappuccino()
    if option == "latte":
        make_latte()
    if option == "off":
        shutdown()

def Process_coins(quarter, dimes, nickel, pennies ):
    total_currency = 0
    toatal_dollar =  float (0.25*quarter + 0.1*dimes + 0.05*nickel + 0.01*pennies)
    return toatal_dollar
    '''
    Calculate the moneary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
    '''
    # penny -> 1 cent -> $0.01
    # nikel -> 5 cent -> $0.05
    # Dime ->  10 cent -> $0.10
    # quarter -> 25 cent ->$0.25
    # pass

def shutdown():
    return 

def Check_transaction():
    pass

def resource_checker():
    pass


def generate_report():
    pass


def make_espresso():
    if resource_checker():
        # 50ml water | 18ml coffee

        pass


def make_cappuccino():
   if resource_checker():
        # 200ml water | 24g coffee | 150ml milk
        pass
   
def make_latte():
   if resource_checker():
        # 250ml water | 24g coffee | 100ml milk
        pass 


user_choice = input("What would you like? (espresso/latte/cappuccino) OR Type 'off' : to shutdown the machine : ")
options_checker(user_choice)
