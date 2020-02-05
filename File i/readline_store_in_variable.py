def file_read(fname):
    myfile = open( fname, "r" )
    data = myfile.readlines()
    print( data )


file_read( 'read write.txt' )
