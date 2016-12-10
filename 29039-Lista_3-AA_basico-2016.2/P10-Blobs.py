def nod(number):
    if (number <= 1.):
        return 0
    return 1 + nod(number / 2.)

n = int(raw_input())

for i in xrange(n):
    x = float(raw_input())
    print "%d dias"  %(nod(x))

