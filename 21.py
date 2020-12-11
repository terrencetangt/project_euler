def d(n):
    s = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s = s + i
            if i != int(n/i):
                s = s + int(n/i)
    return s
n = 10000
di = [0 for i in range(n)]

for i in range(n):
    di[i] = d(i)

s = 0
for i in range(n):
    if di[i] < n:
        if di[di[i]] == i and di[i] != i:
            s = s + i

print(s)
