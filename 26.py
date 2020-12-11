def Reciprocal_cycle(r, n):
    v = []
    q = []
    d = 0
    while True:
        c = 0
        while r < n:
            r = r * 10
            c += 1
        r = r % n
        if r == 0:
            return 0
        for i in range(len(v)):
            if r == v[i]:
                p = i
                for j in range(p+1,len(v)):
                    d += q[j]
                return d + c
        v.append(r)
        q.append(c)

d = 1000
max = 0
m = 0
for i in range(1, d):
    r = Reciprocal_cycle(1,i)
    if r > max:
        max = r
        m = i
print(m)
