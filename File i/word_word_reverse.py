f2 = open( "U.txt", "w" )
with open( "read write.txt", "r" ) as myfile:
    data = myfile.readlines()
data_2 = data[::-1]
f2.writelines( data_2 )
f2.close()
