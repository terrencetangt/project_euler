p = 1
n = 100

for i in range(1,n+1):
    p = p * i

t = str(p)
s = 0
for i in range(len(t)):
    s = s + int(t[i])

print(s)
