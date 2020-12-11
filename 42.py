import math as m
def tri(n):
    n = 2 * n
    p = m.sqrt(n)
    if n == int(p) * (int(p) + 1):
        return True
    else:
        return False

import urllib.request

url = "https://projecteuler.net/project/resources/p042_words.txt"
file = urllib.request.urlopen(url)

s = ""
for line in file:
	s = s + line.decode()

ans = 0
sa = s.split(",")
for i in range(len(sa)):
    sa[i] = sa[i].strip('"')
    y = 0
    for j in sa[i]:
        y = y + ord(j) - 64
    if tri(y) == True:
        ans += 1
print(ans)
