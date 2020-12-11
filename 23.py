def d(n):
    s = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s = s + i
            if i != int(n/i):
                s = s + int(n/i)
    return s

n = 28123
list = []
for i in range(1, n):
    if d(i) > i:
        list.append(i)

b = [True for i in range(n)]


for i in range(len(list)):
    for j in range(len(list)):
        s = list[i] + list[j]
        if s < n:
            b[s] = False

ans = 0
for i in range(n):
    if b[i] == True:
        ans += i

print(ans)
