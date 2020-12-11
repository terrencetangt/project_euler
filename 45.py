import math as m
def triangle(n):
    return int(n * (n + 1) / 2)

def ispentagon(n):
    a = (m.sqrt(24 * n + 1) + 1)/6
    b = int(a)
    if float(a) == float(b):
        return True
    else:
        return False

def ishexagon(n):
    a = (m.sqrt(8 * n + 1) + 1)/4
    b = int(a)
    if float(a) == float(b):
        return True
    else:
        return False

ans = 0
i = 2
ct = 0
n = 2
while ct < n:
    t = triangle(i)
    if ispentagon(t) == True:
        if ishexagon(t) == True:
            ans = t
            ct += 1
    i += 1
print(ans)
