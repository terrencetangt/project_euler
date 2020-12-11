def collatzct(n):
    c = 1
    while n > 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n/2
        c += 1
    return c

n = 1000000
max = {"ct": 0, "value": 0}
v = []
i = 1
while i < n:
    c = collatzct(i)
    if c > max["ct"]:
        max["ct"] = c
        max["value"] = i
    i+=1
print(max["value"], max["ct"])
