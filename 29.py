min = 2
max = 100
list = []
for a in range(min, max+1):
    for b in range(min, max+1):
        p = a ** b
        if p not in list:
            list.append(p)
print(len(list))
