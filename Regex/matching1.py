import re

# match=re.finditer('[abc]','az7@bd9k')#either a b c
# match=re.finditer('[^abc]','az7@bd9k')#except a b c
match = re.finditer( '/D', 'az7@bd9k' )
for m in match:
    print( m.start(), '....', m.group() )
