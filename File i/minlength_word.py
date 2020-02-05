def longest_word(filename):
    infile = open( filename, 'r' )
    words = infile.read().split()
    min_len = len( min( words, key=len ) )
    return [word for word in words if len( word ) == min_len]


print( longest_word( 'read write.txt' ) )
