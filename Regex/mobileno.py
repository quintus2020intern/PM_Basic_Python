import re

while True:
    s = input( "Enter mobile no: " )
    m = re.fullmatch( '[6-9]\d{9}', s )
    if m != None:
        print( s, "is valid mobile number" )
        break
    else:
        print( "this is not valid number" )
