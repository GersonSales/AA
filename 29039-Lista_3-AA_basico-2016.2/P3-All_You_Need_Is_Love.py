def GCD(a, b):
    if (b == 0):
        return a
    return GCD(b, a % b)

n = int(raw_input())

for x in xrange(n):
    s1 = raw_input()
    s2 = raw_input()
    
    s1Int = int(s1, 2)
    s2Int = int(s2, 2)

    if (GCD(s1Int, s2Int) > 1):
        print "Pair #%d: All you need is love!" %(x + 1)
    else:
        print "Pair #%d: Love is not all you need!" %(x + 1)
