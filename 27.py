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

p = 0
max = [0,0]
for a in range(-999, 1000, 1):
    for b in range(-1000, 1001, 1):
        i = 0
        c = 0
        v = False
        while v == False:
            p = (i * i) + (a * i) + b
            if prime(p) == True:
                c = c + 1
            else:
                v = True
            i += 1
        if c > max[0]:
            max[0] = c
            max[1] = a * b
print(max[1])
