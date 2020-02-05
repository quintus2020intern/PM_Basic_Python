# def pascal_triangle(n):
#    trow = [1]
#    y = [0]
#    for x in range(max(n, 0)):
#       print(trow)
#       trow=[l+r for l,r in zip(trow+y, y+trow)]
#    return n>=1
# print(pascal_triangle(6))

x = int( input( "Enter the desired height: " ) )
l = [1]
for i in range( x ):
    # Modified v
    print( "Row", i + 1, l )
    newlist = []
    newlist.append( l[0] )
    for i in range( len( l ) - 1 ):
        newlist.append( l[i] + l[i + 1] )
    newlist.append( l[-1] )
    l = newlist
