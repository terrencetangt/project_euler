#get the process time of a function (without parameters)
def time_function(function):
    from timeit import timeit
    time = timeit(function, number = 1)
    print("The running time is {} seconds.".format(time))

#adding the square of the digits in a number to form a new number
def sum_digit(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i) ** 2
    return sum

def main():
    max = 10000000
    list = [0 for i in range(max)]
    a = 0
    for j in range(1, max):
        x = j
        xlist = [x]
        while x != 1 and x != 89 and list[x] == 0:
            x = sum_digit(x)
            xlist.append(x)
            if list[x] != 0:
                a = list[x]
                break
            if x == 1 or x == 89:
                a = x
                break
        for y in xlist:
            if list[y] == 0:
                list[y] = a
    count = 0
    for j in range(1, max):
        if list[j] == 89:
            count += 1
    print(count)

if __name__ == "__main__":
    time_function(main)

#The running time is 23.8782895 seconds.
