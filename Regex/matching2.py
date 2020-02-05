import re

s = input( "Enter pattern to check : " )
m = re.fullmatch( s, 'abcdefgh' )
if m != None:
    print( "match is available at the beginning of the string" )
    print( 'start index{} and End index:{} '.format( m.start(), m.end() ) )
else:
    print( 'match is not available at the beg of the string' )
