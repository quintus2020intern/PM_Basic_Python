# Write a Python program to write a list content to a file.


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
f = open( 'read write.txt', "w" )
for c in color:
    f.write( "%s\n" % c )
content = open( 'read write.txt' )
print( content.read() )
