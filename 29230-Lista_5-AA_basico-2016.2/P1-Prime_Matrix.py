def crivo(limit):
    primes = [True] * limit
    primes[0] = False
    primes[1] = False

    for i in xrange(2, limit):
        if (primes[i]):
            for j in xrange(i * 2, limit, i):
                primes[j] = False
    return primes

primes = crivo(10**5 + 100)
n, m = map(int, raw_input().split())

matrix = []
for i in xrange(n):
    matrix.append(map(int, raw_input().split()))

attempts = []

dic = {}

for i in xrange(n):
    moves = 0
    for j in xrange(m):
        elem = matrix[i][j]
        bckp = matrix[i][j]
        count = 0
        if (bckp in dic):
            count = dic[bckp]
        else:
            while (not primes[elem]):
                    elem += 1
                    count += 1
            dic[bckp] = count
        moves += count
    attempts.append(moves)


for i in xrange(m):
    moves = 0
    for j in xrange(n):
        elem = matrix[j][i]
        bckp = matrix[j][i]
        count = 0
        if (bckp in dic):
            count = dic[bckp]
        else:
            while (not primes[elem]):
                elem += 1
                count += 1
            dic[bckp] = count
        moves += count
    attempts.append(moves)
print min(attempts)
