try:
    num = int( input( "Enter a positive integer:  " ) )
    if num <= 0:
        raise ValueError( "That is not a positive number!" )
except ValueError as ve:
    print( ve )
