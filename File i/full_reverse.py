f1 = open( "K.txt", "w" )
# output written in a file

with open( "rawfile.txt", "r" ) as myfile:
    # open in a read mode from where we catch the data
    data = myfile.read()

data_1 = data[::-1]

f1.write( data_1 )

f1.close()
