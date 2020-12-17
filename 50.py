#Sieve of Eratosthenes of generating primes
def SieveOfEratosthenes(n):
    primes = []
    primeb = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (primeb[p] == True):
            for i in range(p * 2, n + 1, p):
                primeb[i] = False
        p += 1
    primeb[0]= False
    primeb[1]= False
    for p in range(n + 1):
        if primeb[p]:
            primes.append(p)
    return tuple(primes)

ans = 0
n = 1000000
primes = SieveOfEratosthenes(n)
c = 0
for i in range(len(primes)):
    for j in range(i + c, len(primes)):
        s = sum(primes[i:j])
        d = j - i
        if s > n:
            break
        if s in primes:
            if d > c:
                c = d
                ans = s
print(ans)
