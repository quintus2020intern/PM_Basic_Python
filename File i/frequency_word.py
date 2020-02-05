from collections import Counter


def word_count(fname):
    f = open( fname )
    return Counter( f.read().split() )


print( "Number of words in the file :", word_count( "read write.txt" ) )
