def pal(n):
    s=str(n)
    l = len(s)-1
    for i in range(l):
        if s[i] != s[l-i]:
            return False
    return True

m = -1
n=1000
for i in range(1,n):
    for j in range(1,n):
        x = i * j
        if (pal(x)==True) and (x > m):
            m = x
print(m)
