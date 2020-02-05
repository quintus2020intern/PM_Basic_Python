# months=('jan','feb','mar','apr','may','june')
# for mname in months:
#     print(mname)
# i = 0
# while i != (len(months) - 1):
#     print(months[i])
#     i = i+1
man = dict( name='man1', age=20, add='bbsr' )
print( man )
print( man.items() )
x2 = (1, 2, 7, 4, 5, 7, 7, 8, 9)
# print(x2.count(7))
print( x2.index( 7 ) )
p = tuple( {1, 2, 3, 4, 5, 6, } )
print( p )
new_dictionary = {}.fromkeys( ['name', 'roll', 'phone', 'email'], 'unknown' )
print( new_dictionary )
new_dictionary = dict.fromkeys( ['name', 'roll', 'phone', 'email'], 'unknown' )
print( new_dictionary )

new_dictionary = dict.fromkeys( range( 1, 10 ), 'unknown' )
print( new_dictionary )
