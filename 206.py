#get the process time of a function (without parameters)
def time_function(function):
    from timeit import timeit
    time = timeit(function, number = 1)
    print("The running time is {} seconds.".format(time))

def conceal(n):
    s = str(n)
    if len(s) != 19:
        return False
    p = 0
    for i in range(1, 10):
        if int(s[p]) != i:
            return False
        p += 2
    if int(s[-1]) != 0:
        return False
    return True

def main():
    ans = 1000000000
    square = ans ** 2
    b = False
    while b == False:
        ans += 10
        square = ans ** 2
        b = conceal(square)
    print(ans)

if __name__ == "__main__":
    time_function(main)

#The running time is 37.9745646 seconds.
