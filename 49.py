#Evaluate prime or not
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

def ispermutate(a: str, b: str):
    if len(a) != len(b):
        return False
    a_list = []
    b_list = []
    for i in range(len(a)):
        a_list.append(a[i])
        b_list.append(b[i])
    a_list.sort()
    b_list.sort()
    for i in range(len(a)):
        if a_list[i] != b_list[i]:
            return False
    return True

prime_list = []
end = 10000
for i in range(1,end):
    if isprime(i) == True:
        if i > 999:
            prime_list.append(i)
l = len(prime_list)
s = ""
for i in range(l):
    c = 0
    s = str(prime_list[i])
    for j in range(i + 1, l):
        if ispermutate(str(prime_list[i]), str(prime_list[j])) == True:
            if (prime_list[j] - prime_list[i]) % 3330 == 0:
                c += 1
                s = s + str(prime_list[j])
        if c == 2:
            print(s)
            break
