# l=[]
# for i in 'ppm':
#  l.append(i)
# print(l)
i = []
l = [i * 2 for i in {3, 1, 2}]
l1 = [i for i in range(10) if i % 2 == 0 if i % 3 == 0]
print(l)
print(l1)
value = 123
print(value, 'is', 'even' if value % 2 == 0 else 'odd')
