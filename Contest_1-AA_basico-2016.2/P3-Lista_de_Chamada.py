n, k= map(int, raw_input().split())

classMates = []

for  i in xrange(n):
    classMates.append(raw_input())

classMates.sort()

print classMates[k - 1]

