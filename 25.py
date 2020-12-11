def no_digit(n):
    return len(str(n))


a = 1
b = 1
ct = 2
while no_digit(b) < 1000:
    ct += 1
    t = b
    b = a + b
    a = t
print(ct)
