# l=[]
# n=input("Enter a String:")
# l1=n.split('')
# print(l1)
# user_input=input("Enter a string :")
# print("input string",+str(user_input))
# v=('a','e','i','o','u',)
# new_string=""
# l1=[]
# for i in range(0,len(user_input)):
#     if user_input[i] in v:
#         new_string=user_input.replace(i,'#')
#         print
# s="How Are you"
# l=s.split(" ")
# print(l)
# l1=[]
# v={'a','e','i','o','u'}
#
# for x in l:
#     if x[0] in v:
#         x.replace(l[0],'#')
#
#     if x[1] in consonant:
#
# s=input("Enter some string:")
s = "How are you"
l = s.split()
print( l )
v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
l1 = []
for value in l[0]:
    # print(char[0])
    if value in v:
        d = l[0].replace( value, '#' )
        l1.append( d )
print( l1 )

for temp in l[1]:
    if temp not in v:
        d = l[1].replace( temp, '$' )
        l1.append( d )
print( l1 )
e = l[2].upper()
l1.append( e )
print( l1 )
f = ' '.join( l1 )
print( f )
