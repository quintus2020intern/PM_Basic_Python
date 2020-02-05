try:
    print( 10 / 0 )
except ZeroDivisionError as msg:
    print( "The type of error:", type( msg ) )
    print( "The type of class object:", msg.__class__ )
    print( "The type of class name:", msg.__class__.__name__ )
    print( "The description of error:", msg )
