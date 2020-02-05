num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# sorted_dict = {x: sorted(y) for x, y in num.items()}
for x, y in num.items():
    sort = {x: sorted( y )}
    print( sort )
# print(sorted_dict)
