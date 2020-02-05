# def longest_word(filename):
#         file= open(filename, 'r')
#         words = file.read().split()
#         max_len = len(max(words, key=len))
#         return [word for word in words if len(word) == max_len]
#
# print(longest_word('read write.txt'))
def file_lengthy(fname):
    with open( fname ) as f:
        for i, l in enumerate( f ):
            pass
    return i + 1


print( "Number of lines in the file: ", file_lengthy( "read write.txt" ) )
