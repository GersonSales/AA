m = [map(int, raw_input().split()) for i in xrange(5)]
for i in m:
    del i[0]
    i.sort()

for x in m:
    print x
