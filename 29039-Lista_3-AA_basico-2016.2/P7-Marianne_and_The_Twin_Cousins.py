def crivo(limit):
    limit = limit + 100
    primes = [True] * limit
    primes[0] = False
    primes[1] = False


    for i in xrange(2, limit):

        for j in xrange(i*i, limit, i):
            primes[j] = False
    return  primes

def twinCousins(primes):
    twinCousins = [0] * len(primes)
    for i in xrange(1, len(primes) - 2):
        if (primes[i]):
            if (primes[i + 2] and abs (i - (i + 2)) == 2):
                twinCousins[i] = twinCousins[i - 1] + 1

            elif (primes[i - 2] and abs(i - (i - 2)) == 2):
                twinCousins[i] = twinCousins[i - 1] + 1

            else :
                twinCousins[i] = twinCousins[i - 1]
        else:
            twinCousins[i] = twinCousins[i - 1]

    return twinCousins

primes = crivo(10**6 + 1000)

twinCousins = twinCousins(primes)
n = int(raw_input())

for i in xrange(n):
    x, y = map(int, raw_input().split())

    if (y < x) :
        x, y = y, x


    print twinCousins[y] - twinCousins[x - 1]



