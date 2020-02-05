# connection establish


mydb = mysql.connector.connect(
    host="localhost",
    user="myusername",
    passwd="mypassword"
)

print( mydb )
