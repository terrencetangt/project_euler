def perm_next(a):
    #Step 1
    p = -1
    for k in range(len(a)-1):
        if a[k] < a[k+1]:
            p = k
    if p == -1:
        return []
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

from math import factorial

def npr(n, r):
    return int(factorial(n)/factorial(n - r))

s = [1,2,3,4,5,6,7,8,9]
m = [0,0,0]
product = []
ans = 0
l = npr(len(s), len(s))
for i in range(l):
    perm_next(s)
    m[0] = s[0] * 10 + s[1]
    m[1] = s[2] * 100 + s[3] * 10 + s[4]
    m[2] = s[5] * 1000 + s[6] * 100 + s[7] * 10 + s[8]
    if m[0] * m[1] == m[2]:
        if m[2] not in product:
            product.append(m[2])
    m[0] = s[0]
    m[1] = s[1] * 1000 + s[2] * 100 + s[3] * 10 + s[4]
    m[2] = s[5] * 1000 + s[6] * 100 + s[7] * 10 + s[8]
    if m[0] * m[1] == m[2]:
        if m[2] not in product:
            product.append(m[2])
for i in product:
    ans += i
print(ans)
