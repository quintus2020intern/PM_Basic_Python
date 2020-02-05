import os

print( "Enter 'quit' for exisiting the program" )
user_input = input( "Enter the file name which you want to delete:" )
if user_input == 'quit':
    exit()
else:
    print( "\n starting the removal of the file !" )
    os.remove( user_input )
    print( "The file deletion is successfull" )
