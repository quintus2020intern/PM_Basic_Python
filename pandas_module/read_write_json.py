import json

with open( "my_json.json", 'r' ) as data_file:
    data = json.load( data_file )
    print( data )
    for i in range( 0, len( data["people"] ) ):
        print( data["people"][i]["id"] )

out_file = open( 'l.txt', 'w' )
json.dump( data, out_file )
out_file.close()
