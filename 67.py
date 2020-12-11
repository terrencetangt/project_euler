import urllib.request

url = "https://projecteuler.net/project/resources/p067_triangle.txt"
file = urllib.request.urlopen(url)

s = ""
for line in file:
	s = s + line.decode()

sa = s.split("\n")
for i in range(len(sa)):
    sa[i] = sa[i].split()
    for j in range(len(sa[i])):
        sa[i][j] = int(sa[i][j])

for i in range(len(sa) -1, 0,-1):
    for j in range(len(sa[i])-1):
        if sa[i][j] > sa[i][j+1]:
            sa[i-1][j] += sa[i][j]
        else:
            sa[i-1][j] += sa[i][j+1]

max = sa[0][0]
print(max)
