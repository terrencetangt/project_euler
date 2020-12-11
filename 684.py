def sa(n):
    s = 0
    p = 0
    while n>0:
        if n >= 9:
            s += 9 * (10 ** p)
            n = n - 9
        else:
            s += n * (10 ** p)
            n = 0
        p = p + 1
    return s

def sb(n):
    s = 0
    for i in range(1, n + 1):
        s += sa(i)
    return s

a = 0
b = 1
ans = 0
for i in range(2, 91):
    t = b
    b = a + b
    a = t
    ans += sb(b)
    ans = ans % 1000000000
    print(b, ans)
