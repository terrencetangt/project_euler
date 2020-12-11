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


ans = 0
c = 6
d = 1
i = 1
while d < c:
    d = 1
    for j in range(2,c+1):
        if ispermutate(str(i), str(i*j)) == False:
            break
        else:
            d += 1
            if d == c:
                ans = i
    i += 1
print(ans)
