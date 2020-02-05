import re

s = open( "rawfile.txt", 'r' )
pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
finalIP = re.findall( pattern, s )
print( s.read() )
