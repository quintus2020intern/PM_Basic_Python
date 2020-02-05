import sys


class Customer:
    '''
    customer class with bank operation details
    '''
    bankname = "State Bank of India"

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.amt = self.balance + amt
        print( "After Deposit the balance is:", self.amt )

    def withdraw(self, amt):
        if amt > self.amt:
            print( "insufficient balance" )
            sys.exit()
        self.balance = self.balance - amt
        print( "After withdraw the balance is", self.balance )


print( "welcome to ", Customer.bankname )
name = input( "Enter your name:" )
c = Customer( name )
while True:
    print( "d-deposit\nw-withdraw\ne-exit" )
    option = input( "Enter your choice:" )
    if option == 'd' or option == 'D':
        amt = float( input( "Enter the amount to deposit:" ) )
        c.deposit( amt )
    elif option == 'w' or option == 'W':
        amt = float( input( "Enter the amount to withdraw:" ) )
        c.withdraw( amt )
    elif option == 'e' or option == 'E':
        print( "Thanks for Banking" )
        sys.exit()
    else:
        print( "choice valid operation" )
