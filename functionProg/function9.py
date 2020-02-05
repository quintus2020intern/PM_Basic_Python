def test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for char in s:
        if char.isupper():
            d["UPPER_CASE"] += 1
        elif char.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    print( "Original String : ", s )
    print( "No. of Upper case characters : ", d["UPPER_CASE"] )
    print( "No. of Lower case Characters : ", d["LOWER_CASE"] )


print( test( 'Pragayan Paramita Mohapatra' ) )
