num_list = [1, 2, 3, 4]
num_list1 = [0, 1, 2, 3]
num_list3 = list( (num_list1 + num_list) )
print( num_list3 )
num = dict.fromkeys( num_list3, 4 )
print( num )
# new_dict =  {}
# for n in num_list:
#     for n1 in num_list1:
#
