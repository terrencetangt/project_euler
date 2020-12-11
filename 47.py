def d_prime(n):
    p = 2
    c = 0
    while n > 1:
        if n % p == 0:
            c += 1
        while n % p == 0:
            n = int(n/p)
        p += 2
    return c

n = 4
c = 0
i = 10
ans = 0
while c < n:
    if d_prime(i) == n:
        c += 1
        if c == n:
            ans = i - n + 1
    else:
        c = 0
    i += 1

print(ans)
