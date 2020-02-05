import re

count = 0
pattern = re.compile( 'ab' )
matcher = pattern.finditer( 'ababbabaabaabbab' )
for match in matcher:
    count = count + 1
    print( 'start:{},end:{},group:{}'.format( match.start(), match.end(), match.group() ) )
print( "the number of occurance is : ", count )
