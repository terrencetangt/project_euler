y = 1900
m = 1
d = 1
w = 1

def feb_day(y):
    if y % 400 == 0:
        return 28
    elif y % 100 == 0:
        return 29
    elif y % 4 == 0:
        return 29
    else:
        return 28

c = 0
while not(y == 2000 and m == 12 and d == 31):
    if m in [1,3,5,7,8,10] and d == 31:
        m += 1
        d = 1
    elif m in [4,6,9,11] and d == 30:
        m += 1
        d = 1
    elif m == 2 and d == feb_day(y):
        m += 1
        d = 1
    elif m == 12 and d == 31:
        y += 1
        m = 1
        d = 1
    else:
        d += 1
    w += 1
    if w == 7:
        w = 0
    if w == 1 and d == 1 and y >= 1901:
        c += 1
print(c)
