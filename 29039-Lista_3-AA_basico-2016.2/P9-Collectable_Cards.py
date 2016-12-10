def GCD(a, b):
    if (b== 0):
        return a
    return GCD(b, a % b)

n = int(raw_input())

for i in xrange(n):
    a, b = map(int, raw_input().split())
    print (GCD(a, b))
