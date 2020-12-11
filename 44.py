import math as m
def pentagon(n):
    return int(n * (3 * n - 1) / 2)
def ispentagon(n):
    a = (m.sqrt(24 * n + 1) + 1)/6
    b = int(a)
    if float(a) == float(b):
        return True
    else:
        return False

b = False
i = 1
p = []
ans = 0
while b == False:
    y = pentagon(i)
    if len(p) > 0:
        for x in p:
            if ispentagon(y - x) == True:
                if ispentagon(y + x) == True:
                    ans = y-x
                    b = True
    p.append(y)
    i += 1

print(ans)
