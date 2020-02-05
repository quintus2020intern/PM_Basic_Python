import os

# os.chdir('C:\Users\user\PycharmProjects\EatLoad\directorie')#change directories
# print(os.getcwd())
print( os.listdir() )  # list directories
print( os.mkdir( "direcory" ) )  # making new directory ///return  none
os.rename( "change_dir.py", "change_directory" )  # rename
os.rmdir( "direcory" )  # remove empty directory
