def pal(n):
    s=str(n)
    l = len(s)-1
    for i in range(l):
        if s[i] != s[l-i]:
            return False
    return True

ans = 0
n = 1000000
for i in range(n):
    b = str(bin(i)).replace("0b", "")
    if pal(i) == True and pal(b) == True:
        ans +=i
print(ans)
