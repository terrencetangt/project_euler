#determine if it is a prime
def isprime(n: int) -> bool:
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

q = 2
r = 3
ct = 0
tct = 1
ans = 0
b = False
i = 2
while b == False:
    if i % q == 1:
        tct += 1
        if isprime(i) == True:
            ct += 1
    if ct / tct < 0.1 and r > 5:
        b = True
        break
    if i == r * r:
        q += 2
        r += 2
    i += 1
print(r)
