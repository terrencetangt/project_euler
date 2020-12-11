n = 100
c = [[0 for i in range(n+1)]for j in range(n+1)]

ans = 0
m = 1000000
for i in range(n+1):
    c[i][0] = 1
    c[i][i] = 1
for i in range(n+1):
    for j in range(i+1):
        if j > 0 and j < i:
            c[i][j] = c[i-1][j-1] + c[i-1][j]
            if c[i][j] > m:
                ans += 1
print(ans)
