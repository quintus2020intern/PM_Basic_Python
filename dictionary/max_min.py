my_dict = {'x': 500, 'y': 5874, 'z': 560}
max = max( my_dict.keys(), key=(lambda k: my_dict[k]) )
min = min( my_dict.keys(), key=(lambda k: my_dict[k]) )
print( 'Maximum Value: ', my_dict[max] )
print( 'Minimum Value: ', my_dict[min] )
# for x in max(my_dict.keys()):
#     print(x)
