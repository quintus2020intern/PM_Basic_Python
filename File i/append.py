def file_read(fname):
    # with open(fname, "a") as myfile:
    with open( fname, "w" ) as myfile:
        myfile.write( "Python Exercises\n" )
        myfile.write( "Java Exercises\n" )
        myfile.write( "HTML Exercises\n" )
    txt = open( fname )
    print( txt.read() )


file_read( 'read write.txt' )
