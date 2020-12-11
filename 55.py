def palindrome(n):
    s=str(n)
    l = len(s)-1
    for i in range(l):
        if s[i] != s[l-i]:
            return False
    return True

def reverse(n):
    s=str(n)
    ns = ""
    for i in s:
        ns = i + ns
    return int(ns)

def lychrel(n):
    for i in range(50):
        n = n + reverse(n)
        if palindrome(n) == True:
            return False
    return True

ans = 0
i = 1
n = 10000
while i < n:
    if lychrel(i) == True:
        ans += 1
    i += 1
print(ans)
