from heapq import nlargest

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
inverse = {(value, key) for key, value in my_dict.items()}
# print (max(inverse)[1])
three_largest = nlargest( 3, my_dict, key=my_dict.get )
print( three_largest )
# view = my_dict.keys()
# print(view)
# val=list(my_dict.items())
# print(val)
# a=list(my_dict.keys())
# # b=max(a,range(0,6))
# # print(b)
# b=list(my_dict.values())
# sorted_d = sorted(d.items(), key=operator.itemgetter(1))#
# for keys in sorted(my_dict):
#     print(max(keys))
# keymax=max(my_dict,key=my_dict.get)
# print(keymax)

itemMaxValue = max( my_dict.items(), key=lambda x: x[1] )
print( 'Maximum Value in Dictionary : ', itemMaxValue[1] )
listOfKeys = list()
# Iterate over all the items in dictionary to find keys with max value
for key, value in my_dict.items():
    if value == itemMaxValue[1]:
        listOfKeys.append( key )
print( 'Keys with maximum Value in Dictionary : ', listOfKeys )
