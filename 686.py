def p(L, n):
    c = 0
    q = 2
    t = 1
    while c < n:
        q *= 2
        t += 1
        if int(str(q)[:3]) == L:
            c += 1
    return t

for i in range(1, 200):
    print(p(123, i))
