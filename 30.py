n = 5
ans = 0
for i in range(11, (9 ** n * (n+1))):
    s = str(i)
    p = 0
    for j in range(len(s)):
        p += int(s[j]) ** n
    if p == i:
        ans += i
print(ans)
