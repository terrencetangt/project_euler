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

sum = 0
n = 2000000
i = 0
while i < n :
    if prime(i) == True:
        sum = sum + i
    i += 1
print(sum)
