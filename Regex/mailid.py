import re

while True:
    s = input( "Enter mailid: " )
    regex = '^\w+([\._]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    m = re.fullmatch( regex, s )
    if m != None:
        print( "valid mail-id" )
        break
    else:
        print( "invalid" )
