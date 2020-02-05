import re

s = "learning python is very easy"
res = re.search( "y$", s, re.IGNORECASE )
if res != None:
    print( "Target string ends with y" )
else:
    print( "not match" )
