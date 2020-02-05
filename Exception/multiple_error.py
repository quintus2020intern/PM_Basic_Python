try:
    a = 3
    if a < 4:
        # throws ZeroDivisionError for a = 3
        print( a )
        b = a / (a - 3)
        print( b )

        # throws NameError if a >= 4
    print( "Value of b = ", b )

# note that braces () are necessary here for multiple exceptions
except(ZeroDivisionError, NameError):
    print( "\nError Occurred and Handled" )
