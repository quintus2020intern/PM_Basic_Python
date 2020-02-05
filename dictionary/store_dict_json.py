# import json
#
# d = {"students": [{"firstName": "Nikki", "lastName": "Roysden"},
#                   {"firstName": "Mervin", "lastName": "Friedland"},
#                   {"firstName": "Aron ", "lastName": "Wilkins"}],
#      "teachers": [{"firstName": "Amberly", "lastName": "Calico"},
#                   {"firstName": "Regine", "lastName": "Agtarap"}]}
#
# js_c = json.dumps(d, indent=4)
# print(type(js_c))

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

xc = sorted( student_tuples, key=lambda student: student[2] )
print( xc )
