# f=open("redawrite.txt","x")#create a specified file
# f = open("redawrite.txt","a")#append in a file
# f = open("redawrite.txt","wb")#write a file and override
# f.write("hello buddy!!!!")
# f.close()
f1 = open( "pasport.jpg", "rb" )  # read a file
print( f1.read() )
f1.close()  # close a file
