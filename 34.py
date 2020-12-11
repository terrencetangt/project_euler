from math import factorial as f

def digit_fact(n):
    s = str(n)
    sum = 0
    if n < 10:
        return False
    else:
        for i in s:
            sum = sum + f(int(i))
    if sum == n:
        return True
    else:
        return False

u = 7 * f(9)
ans = 0
for i in range(u):
    if digit_fact(i) == True:
        ans += i
print(ans)
