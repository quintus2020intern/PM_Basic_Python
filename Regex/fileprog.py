import re

f1 = open( "input.txt", 'r' )
f2 = open( "output.txt", 'w' )
for line in f1:
    list = re.findall( '[6-9]\d{9}', line )
    for number in list:
        f2.write( number + "\n" )
print( "Extracted all mobile number from input.txt into output.txt" )
f1.close()
f2.close()
