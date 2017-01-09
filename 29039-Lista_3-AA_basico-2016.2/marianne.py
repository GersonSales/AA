def crivo(limit):
    primes = [True] * limit
    primes[0] = False
    primes[1] = False

    for i in xrange(2, limit):
        if (primes[i]):
            for j in xrange(i*2, limit, i):
                primes[j] = False

    return primes

limit = 10**6 + 1000
primes = crivo(limit)

twinCousins = [0] * (limit)

for i in xrange(limit - 2):
    flag = True
    if (primes[i] and primes[i + 2]):
        twinCousins[i] = twinCousins[i - 1] + 1
        flag = False

    if (primes[i] and primes[i - 2]):
        twinCousins[i] = twinCousins[i - 1] + 1
        flag = False

    if (flag):
        twinCousins[i] = twinCousins[i -1]

n = int(raw_input())

for i in xrange(n):
    x, y = map(int, raw_input().split())

    if (y > x):
        x, y = y, x

    print abs(twinCousins[y - 1] - twinCousins[x])


