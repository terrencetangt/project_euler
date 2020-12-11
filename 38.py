def pandigit(n):
    s = str(n)
    if len(s) != 9:
        return False
    for i in range(1, 10):
        if s.find(str(i)) == -1:
            return False
    return True

ans = 0
for i in range(1, 99999):
    s = ""
    m = 1
    while len(s) < 9:
        s = s + str(i * m)
        m += 1
    if pandigit(s) == True:
        if int(s) > ans:
            ans = int(s)
print(ans)
