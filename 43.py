from math import factorial as f

def perm_next(a):
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

def sub_string(n):
    if int(n[1:4]) % 2 != 0:
        return False
    if int(n[2:5]) % 3 != 0:
        return False
    if int(n[3:6]) % 5 != 0:
        return False
    if int(n[4:7]) % 7 != 0:
        return False
    if int(n[5:8]) % 11 != 0:
        return False
    if int(n[6:9]) % 13 != 0:
        return False
    if int(n[7:10]) % 17 != 0:
        return False
    return True

ans = 0
s = [0,1,2,3,4,5,6,7,8,9]
for i in range(f(len(s))):
    t = ""
    for j in range(len(s)):
        t = t + str(s[j])
    if sub_string(t) == True:
        ans += int(t)
    s = perm_next(s)
print(ans)
