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

def Goldbach(n):
    i = 1
    p = n
    while p > 0:
        p = n - 2 * i * i
        if prime(p) == True:
            return False
        i += 1
    return True

ans = 0
i = 9
b = False
while b == False:
    if prime(i) == False:
        if Goldbach(i) == True:
            ans = i
            b = True
    i += 2

print(ans)
