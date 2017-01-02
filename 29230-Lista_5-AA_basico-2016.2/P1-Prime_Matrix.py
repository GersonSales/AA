def crivo(limit):
    primes = [True] * limit
    primes[0] = False
    primes[1] = False

    for i in xrange(2, limit):
        for j in xrange(i*i, limit, i):
            primes[j] = False

    return primes
primes = crivo(10**6)
n, m = map(int, raw_input().split())

matrix = []
matrixTouse = []
transpMatrxToUse = []
transpMatrx = []
for i in xrange(n):
    newLine = map(int, raw_input().split())
    matrix.append(newLine)
    matrixTouse.append(matrix[i])

    if (len(transpMatrx) == 0):
        for j in xrange(len(newLine)):
            transpMatrx.append([newLine[j]])
    else:
        for j in xrange(len(newLine)):
            transpMatrx[j].append(newLine[j])
    transpMatrxToUse.append(transpMatrx[i])

attempts = []
for  i in xrange(len(matrixTouse)):
    count = 0
    for j in xrange(len(matrixTouse[i])):
        while (not primes[matrixTouse[i][j]]):
                matrixTouse[i][j] += 1
                count += 1
    attempts.append(count)
    matrixTouse[i] = matrix[i]

for  i in xrange(len(transpMatrxToUse)):
    count = 0
    for j in xrange(len(transpMatrxToUse[i])):
        while (not primes[transpMatrxToUse[i][j]]):
            transpMatrxToUse[i][j] += 1
            count += 1

    attempts.append(count)
    transpMatrxToUse[i] = transpMatrx[i]

print min(attempts)
