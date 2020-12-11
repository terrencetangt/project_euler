import urllib.request

url = "https://projecteuler.net/project/resources/p022_names.txt"
file = urllib.request.urlopen(url)

s = ""
for line in file:
	s = s + line.decode()

sa = s.split(",")
for i in range(len(sa)):
    sa[i] = sa[i].strip('"')

sa.sort()
sum = 0
for i in range(len(sa)):
    s = 0
    for j in sa[i]:
        s = s + ord(j) - 64
    sum = sum + s * (i+1)

print(sum)
