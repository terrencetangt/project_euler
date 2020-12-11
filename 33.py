def cancel(a, b):
    list = [0,0]
    for i in str(a):
        for j in str(b):
            if i == j:
                if str(a)[0] != str(a)[1]:
                    list[0] = int(str(a).replace(i,""))
                if str(b)[0] != str(b)[1]:
                    list[1] = int(str(b).replace(j,""))
    return list

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

list = []
d = [1,1]
ans = 0
for i in range (11, 100):
    for j in range(11, 100):
        if i / j < 1:
            if i % 10 != 0 and j % 10 != 0:
                list = cancel(i,j)
                if list[1] > 0:
                    if list[0]/list[1] == i/j:
                        d[0] *= i
                        d[1] *= j

ans = int(d[1] /gcd(d[0], d[1]))
print(ans)
