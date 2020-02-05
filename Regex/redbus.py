import re
import urllib.request

u = urllib.request.urlopen( "https://www.redbus.in/info/contactus" )
text = u.read()
number = re.findall( '[0-9]{3,4}[- ][0-9-]+', str( text ), re.IGNORECASE )
for x in number:
    print( x )
