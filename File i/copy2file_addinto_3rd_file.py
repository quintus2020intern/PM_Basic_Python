data = data2 = ""

with open( 'read write.txt' ) as fp:
    data = fp.read()

with open( 'K.txt' ) as fp:
    data2 = fp.read()

data += "\n"
data = data + data2

with open( 'B.txt', 'w' ) as fp:
    fp.write( data )
