s = "guddi gulu golu molu pulu"
l = s.split()
i = 0
l1 = []
while i <= len(l):
    if i % 2 == 0:
        l1.append(l[i])
    else:
        l1.append(l[i][-1::-1])
        i = i + 1
print(l1)
