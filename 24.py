def perm_next(a):
    #Step 1
    p = -1
    for k in range(len(a)-1):
        if a[k] < a[k+1]:
            p = k
    if p == -1:
        return False
    v = -1
    for l in range(p,len(a)):
        if a[p] < a[l]:
            v = l
    if v >= 0:
        t = a[p]
        a[p] = a[v]
        a[v] = t
    for i in range(int((len(a) - p - 1) / 2)):
        t = a[p +1+ i]
        a[p+1+i] = a[len(a) - i-1]
        a[len(a) - i-1] = t
    return a

list = [0,1,2,3,4,5,6,7,8,9]
n = 1000000

for i in range(n - 1):
    list = perm_next(list)

s = ""
for i in range(len(list)):
    s = s + str(list[i])

print(s)
