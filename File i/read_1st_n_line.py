def file_read_from_head(fname):
    #     from itertools import islice
    #     with open(fname) as f:
    #         for line in islice(f, nlines):
    #             print(line)
    # file_read_from_head('read write.txt', 5)
    txt = open( fname )
    print( txt.readline() )


file_read_from_head( 'read write.txt' )
