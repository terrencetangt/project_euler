def right_tri(p):
    ct = 0
    c = p
    a = 1
    while c > a:
        b = a + 1
        while c > b:
            c = p - a - b
            if ((a ** 2 + b ** 2) == c ** 2):
                ct += 1
            b += 1
        a += 1
    return ct

ans = [0,0]
c = 0
n = 1000
for i in range(n):
    c = right_tri(i)
    if c > ans[0]:
        ans[0] = c
        ans[1] = i
print(ans)
