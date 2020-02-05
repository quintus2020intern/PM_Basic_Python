import re

while True:
    s = input( "Enter Registration number: " )
    m = re.fullmatch( 'TS[012][0-9][A-Z]{2}\d{4}', s )
    if m != None:
        print( "valid number" )
        break
    else:
        print( "invalid" )
