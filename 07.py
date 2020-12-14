def prime(p):
    for i in range(2, int(p**0.5)+ 2):
        if p % i == 0:
            return False
    return True

n = 10001
c = 1
p = 2
while c < n:
    p += 1
    if prime(p) == True:
        c +=1
print(p)
