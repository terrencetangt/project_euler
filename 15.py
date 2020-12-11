def comb(n,r):
    if r == 0:
        return 1
    elif n == r:
        return 1
    else:
        return int((comb(n-1,r-1) * n) /r)

print(comb(40, 20))
