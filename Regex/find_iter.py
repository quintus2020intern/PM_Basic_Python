import re

count = 0
pattern = re.compile( 'a' )
matcher = pattern.finditer( 'abbbababbbaaabb' )
for match in matcher:
    count = count + 1
    print( "match is available at end index:", match.end() )
    print( "match is available at start index:", match.start() )
print( "The number of occurance is ", count )
