import os

# to deleting a file import os module
if os.path.exists( "redawrite.txt" ):
    os.remove( "redawrite.txt" )
else:
    print( "The file does not exist" )
# os.rmdir("File i")#delete folder
