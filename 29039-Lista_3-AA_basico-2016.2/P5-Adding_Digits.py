a, b, n = map(int, raw_input().split())

flag = False

for x in xrange(10):
    if ((a * 10 + x  ) % b == 0):
        a = (a * 10 + x)
        flag = True
        break
if (not flag):
    print -1
else:
    a = a * (10**(n - 1))
    print a
