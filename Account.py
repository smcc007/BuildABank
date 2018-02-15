class Account:
    def __init__(self): #this is the constructor
        self.balance = 0

    def __str__(self): #define the default print behaviour
        return "The current balance is:  %d" %self.balance
