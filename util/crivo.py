def crivo(limit):
    limit = limit
    primes = [True] * limit
    primes[0] = False
    primes[1] = False


    for i in xrange(2, limit):

        for j in xrange(i*i, limit, i):
            primes[j] = False
    return  primes
