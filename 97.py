#get the process time of a function (without parameters)
def time_function(function):
    from timeit import timeit
    time = timeit(function, number = 1)
    print("The running time is {} seconds.".format(time))


def main():
    ans = 1
    no_of_digits = 10
    power = 7830457
    coefficient = 28433
    constant = 1
    for i in range(power):
        ans *= 2
        if ans > 10 ** 10:
            ans = ans % 10 ** 10
    ans = ans * coefficient + 1
    ans = ans % 10 ** 10
    print(ans)

if __name__ == "__main__":
    time_function(main)

#The running time is 1.0058154000000001 seconds.
