n = input('Input the number:')
n = int(n)
p = -1
i = 1
while n > 1:
    i = i + 1
    if n % i == 0:
        n = n / i
        if i > p:
            p = i
print(i)
