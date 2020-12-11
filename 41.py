from math import factorial as f
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

def prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

n = 9
i = 2
ans = 0
d = [1]
while i <= n:
    s = []
    for j in range(1, (i + 1)):
        s.append(j)
    for j in range(1, f(i)):
        s = perm_next(s)
        p=""
        for k in range(i):
            p = p + str(s[k])
        if prime(int(p)) == True:
            if int(p) > ans:
                ans = int(p)
    i += 1
print(ans)
