def div_no(n):
    c = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            c += 1
    c *= 2
    return c

nd = 500
n = 1
i = 1
while div_no(n)<=nd:
    i+=1
    n+=i
print(n)
