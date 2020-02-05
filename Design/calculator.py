import sys


def add(x, y):
    return x + y
    sys.exit()


def sub(x, y):
    return x - y
    sys.exit()


def mult(x, y):
    return x * y
    sys.exit()


def div(x, y):
    return x / y
    sys.exit()


print( "Select Operation:" )
print( "1.ADD" )
print( "2.SUB" )
print( "3.MUL" )
print( "4.DIV" )
print( "4.EXIT" )
choice = (input( "Enter choice(1/2/3/4/5):" ))
num1 = int( input( "Enter first number:" ) )
num2 = int( input( "Enter second number:" ) )
if choice == '1':
    print( num1, "+", num2, "=", add( num1, num2 ) )
elif choice == '2':
    print( num1, "-", num2, "=", sub( num1, num2 ) )
elif choice == '3':
    print( num1, "*", num2, "=", mult( num1, num2 ) )
elif choice == '4':
    print( num1, "/", num2, "=", div( num1, num2 ) )
else:
    print( "Invalid input" )
