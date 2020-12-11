def prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def trun_prime(n):
    s = str(n)
    l = len(s)
    if l < 2:
        return False
    for i in range(1, l):
        if prime(int(s[:i])) == False:
            return False
        if prime(int(s[i:])) == False:
            return False
        if prime(n) == False:
            return False
    return True

n = 11
c = 0
i = 1
ans = 0
while c < n:
    if trun_prime(i) == True:
        ans += i
        c += 1
    i += 1
print(ans)
