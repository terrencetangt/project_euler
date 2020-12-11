n = 1001
q = 2
r = 3
s = 1
for i in range(2, n * n + 1):
    if i % q == 1:
        s += i
    if i == r * r:
        q += 2
        r += 2
print(s)
