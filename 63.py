def no_digit(n):
    return len(str(n))

ans = 0
for i in range(1,100):
    for p in range(1,100):
        if no_digit(i ** p) == p:
            ans += 1
print(ans)
