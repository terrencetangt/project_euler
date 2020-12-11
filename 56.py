def sum_digit(n):
    sn = str(n)
    sum = 0
    for i in sn:
        sum += int(i)
    return sum

n = 100
p = 0
ans = 0
s = 0
for a in range(1, n):
    for b in range(1, n):
        p = a ** b
        s = sum_digit(p)
        if s > ans:
            ans = s
print(ans)
