def even_num(l):
    num = []
    for n in l:
        if n % 2 == 0:
            num.append( n )
    return num


print( even_num( [1, 4, 3, 2, 6, 8, 7, 9] ) )
