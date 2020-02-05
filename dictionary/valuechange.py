from collections import Counter

colors = ['blue', 'red', 'blue', 'red', 'blue']
counter = Counter( colors )
print( counter )
counter['yellow'] += 1
print( counter )
print( counter.most_common()[0] )
