def test_prime(n):
    # if (n==1):
    #     return False
    # elif (n==2):
    #     return True;
    # else:
    for x in range( 2, n ):
        if (n % x == 0):
            return False
    return True


print( test_prime( 9 ) )
# num=407
# if num>1:
#     for i in range(2,num):
#         if(num%i)==0:
#             print(num,"is not a prime")
#             break
#         else:
#             print(num,"is a prime")
# else:
#     print(num,"is not a prime number")
