#print the process time of a function (without parameters)
def time_function(function):
    from timeit import timeit
    msg = "The running time is "
    second = timeit(function, number = 1)
    if second < 60:
        print(msg + "{} seconds.".format(second))
    elif second > 60:
        minute = int((second % 60 ** 2) // 60)
        second = second % 60
        print(msg + "{} minutes and {} seconds".format(minute, second))
    elif second > 60 ** 2:
        hour = int(second // (60 ** 2))
        second = second % 60
        print(msg + "{} hours {} minutes and {} seconds".format(hour, minute, second))

#determine if it is a prime
def isprime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#Sieve of Eratosthenes of generating primes
def SieveOfEratosthenes(n):
    primes = []
    primeb = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (primeb[p] == True):
            for i in range(p * 2, n + 1, p):
                primeb[i] = False
        p += 1
    primeb[0]= False
    primeb[1]= False
    for p in range(n + 1):
        if primeb[p]:
            primes.append(p)
    return primes

#return all prime factors list of a number
def distinct_prime_factors(n):
    factor = []
    i = 2
    while n > 1:
        while n % i == 0:
            if i not in factor:
                factor.append(i)
            n = n / i
        i += 1
    return factor

#Euler's totient function
def euler_totient(n):
    factor = distinct_prime_factors(n)
    p = n
    for i in range(len(factor)):
        p = int(p * (1 - 1/factor[i]))
    return p

def main():
    ans = [1, 1]
    max = 1000000
    prime_list = SieveOfEratosthenes(max)
    for n in range(1, max):
        if n in prime_list:
            continue
        np = n / euler_totient(n)
        if np > ans[1]:
            ans[0] = n
            ans[1] = np
    print(ans[0])

if __name__ == "__main__":
    time_function(main)

#The running time is 2 minutes and 59.95091880000018 seconds
