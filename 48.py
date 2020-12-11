n = 1000
m = 10 ** 10

ans = 0
for i in range(1, n + 1):
    sum = 1
    for j in range(1, i + 1):
        sum *= i
        sum = sum % m
    ans += sum
    ans = ans % m

print(ans)
