n, k = map(int, raw_input().split())

summ = 0
count = 1

matrix =[]
for i in xrange(n):
    line = []
    for j in xrange(n):
        line.append(count)
        if (j + 1 == k):
            summ += count
        count += 1
    matrix.append(line)

print summ
for row in matrix:
    for col in row:
        print col,
    print ""



