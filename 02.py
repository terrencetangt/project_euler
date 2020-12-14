a = 1
b = 2
f = b
c = 0
while True:
    c = a + b
    if c > 4000000:
        break
    if c % 2 == 0:
        f = f + c
    a = b
    b = c
print(f)
