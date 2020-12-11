x=21
n = 2
for i in range(1, x):
    if n % i == 0:
        continue
    else:
        a = i
        j = 2
        while j < a:
            if n % j == 0 and a % j == 0:
                a = int(a / j)
            else:
                j = j + 1
        n = n * a
print(n)
