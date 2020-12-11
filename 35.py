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

def cir_prime(n):
    if n < 10:
        return True
    else:
        s = str(n)
        for i in range(1, len(s)):
            s = s[1:] + s[:1]
            if prime(int(s)) == False:
                return False
        return True

pri_list = []
cpri_list = []
n = 1000000
for i in range(n):
    if prime(i) == True:
        pri_list.append(i)

for i in pri_list:
    if cir_prime(i) == True:
        cpri_list.append(i)

print(len(cpri_list))
