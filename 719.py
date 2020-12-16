#get the process time of a function (without parameters)
def time_function(function):
    from timeit import timeit
    msg = "The running time is "
    second = timeit(function, number = 1)
    if second < 60:
        print(s + "{} seconds.".format(second))
    elif second > 60:
        minute = second // 60
        second = second % 60
        print(s + "{} minutes and {} seconds".format(minute, second))
    elif second > 60 ** 2:
        hour = second // (60 ** 2)
        minute = (second % 60 ** 2) // 60
        second = second % 60
        print(s + "{} hours {} minutes and {} seconds".format(hour, minute, second))
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

def main():
    ans = 0
    max = 10 ** 12
    i = 2
    x = i ** 2
    while x < max:
        x = i ** 2
        if number_split(x, i) == True:
            ans += x
        i += 1
    print(ans)

if __name__ == "__main__":
    time_function(main)

#The running time is 2443.1583608 seconds.
