d = 0
i = 1
p = 0
ans = 1
while p < 6:
    s = str(i)
    for j in range(len(s)):
        d += 1
        if d == 10 ** p:
            ans *= int(s[j])
            p += 1
    i += 1
print(ans)
