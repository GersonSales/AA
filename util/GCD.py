def GCD(a, b):
    if (b == 0):
        return a
    return GCD(b, a % b)

a, b = map(int, raw_input().split())

print "GCD: %d" %(GCD(a, b))
