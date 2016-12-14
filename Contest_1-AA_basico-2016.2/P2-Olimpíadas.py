n, m = map(int, raw_input().split())


count = [0] * n

for i in xrange(m):
    medals = map(int, raw_input().split())
    for medal in medals:
        count[medal - 1] += 1

result = []

