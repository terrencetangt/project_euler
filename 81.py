import urllib.request

url = "https://projecteuler.net/project/resources/p081_matrix.txt"
file = urllib.request.urlopen(url)

matrix = []
for line in file:
    row = line.decode().rstrip().split(',')
    matrix.append(row)

matrix = [list(map(int,s)) for s in matrix]

def moving_right_and_down(matrix):
    l = len(matrix)
    for i in range(l):
        for j in range(l):
            if i == 0 and j == 0:
                pass
            elif i > 0 and j == 0:
                matrix[i][j] += matrix[i-1][j]
            elif i == 0 and j > 0:
                matrix[i][j] += matrix[i][j-1]
            else:
                if matrix[i-1][j] < matrix[i][j-1]:
                    matrix[i][j] += matrix[i-1][j]
                else:
                    matrix[i][j] += matrix[i][j-1]
    return matrix[l-1][l-1]

print(moving_right_and_down(matrix))
