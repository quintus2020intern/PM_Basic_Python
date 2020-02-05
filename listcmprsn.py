list1 = ["a", "b", "c"]
list2 = [[1, 2, 3, 4]]
# list2.extend(list1)
# print(list2)
print( sum( list2, [] ) + list1 )

ip_add = "www.whatsapp.in"
if ip_add == ip_add:
    s = ip_add.split( '.' )
    print( s )
    print( s[1] )
else:
    print( "this is wrong input" )

# ip_address=['192.169.0.1','192.170.0.2','192.171.0.3']
# for val in ip_address:
#     print(val.split(',')[2],end=' ')

# def split(word):
#     return list(word)
# word = 'Dhatuonline pvt.ltd'
# print(split(word))


companyname = "Dhatuonline pvt ltd"
# c=split(companyname)
# res = re.split('', companyname)
res = companyname.replace( ' ', ' ' ).split()
print( res[0] )

# print(res)
