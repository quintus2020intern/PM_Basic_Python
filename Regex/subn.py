import re

t = re.subn( '\d', 'xxxx', 'a7k9j87dk' )
print( type( t ) )
print( (t[0]) )
