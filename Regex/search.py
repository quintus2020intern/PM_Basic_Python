import re

s = "learning python is very easy"
res = re.search( "^p", s )
if res != None:
    print( "target string start with learn" )
else:
    print( "target string not match " )
