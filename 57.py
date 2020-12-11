n = 1000
nu = 3
de = 2
ans = 0
for i in range(n - 1):
    temp = de
    de = de + nu
    nu = de + temp
    if len(str(nu)) > len(str(de)):
        ans += 1
print(ans)
