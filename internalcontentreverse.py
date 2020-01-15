s = input("Enter a string")
l = s.split()
l1 = []
for w in l:
    l1.append(w[-1::-1])
output = ''.join(l1)
print(output)
