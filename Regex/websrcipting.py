import re
import urllib.request

sites = ['http://www.quintuslabs.com', 'http://www.google.com', ]
for s in sites:
    print( 'searching.......', s )
    u = urllib.request.urlopen( s )
    text = u.read()
    # print(text)
    title = re.findall( "<title>.*</title>", str( text ), re.IGNORECASE )
    print( title[0] )
