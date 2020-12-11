#Use Brute Force and then find the pattern of the euler_coins
euler_coin = [1504170715041707, 8912517754604]
t = 1
n = 8912517754604
while n > 1:
    n = euler_coin[t] - euler_coin[t-1] % euler_coin[t]
    euler_coin.append(n)
    t+=1
ans = sum(euler_coin)
print(ans)
