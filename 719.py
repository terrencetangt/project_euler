# return all splitting combination of a string
def combos(n):
    s = str(n)
    yield (n,)
    for i in range(1, len(s)):
        for c in combos(int(s[i:])):
            yield (int(s[:i]),) + c

def combos2(n, l):
    s = str(n)
    yield (n,)
    for i in range(1, len(s)):
        for c in combos(int(s[i:])):
            if len(s[:i]) < l:
                yield (int(s[:i]),) + c


def number_split(square, square_root):
    for c in combos(square):
        s = sum(c)
        if s == square_root:
            return True
    return False

for c in combos2(6724,2):
    print(c)
    print(sum(c))

import time
tStart = time.time()

# ans = 0
# max = 10 ** 4
# i = 2
# x = i ** 2
# while x < max:
#     x = i ** 2
#     if number_split(x, i) == True:
#         ans += x
#     i += 1
# print(ans)
#
# tEnd = time.time()
# print(tEnd - tStart)
