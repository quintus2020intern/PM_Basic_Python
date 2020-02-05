filenames = ['k.txt', 'b.txt']

with open( 'H.txt', 'w' ) as outfile:
    for names in filenames:
        with open( names ) as infile:
            outfile.write( infile.read() )

        outfile.write( "\n" )
