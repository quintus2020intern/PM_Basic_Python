import json

data = """{
    "city":["bam","delhi","mumbai","calcutta"],
    "rank":["1st","2nd","3rd","4th"],
    "name":["punu","gudu","gulu","mulu"],
    "score1":[44,56,76,87],
    "score2":[56,78,97,43]
}"""

data1 = json.loads( data )  # deserialise json into python dict obj
print( data1 )
print( type( data1 ) )
# print(data1["name"][3])
data2 = json.dumps( data1 )  # serialise python dict obj  into json string
print( data2 )
print( type( data2 ) )
# df=pd.DataFrame(data2)
# print(df)
