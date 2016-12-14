try:
    while 1:
        n = int(raw_input())

        pairs = []
        for i in xrange(n):
            m, l = raw_input().split()
            removed = False
            for i in xrange(len(pairs)):
                if(pairs[i] != -1 and pairs[i][0] == m and pairs[i][1] != l):
                    pairs[i] = -1
                    removed = True
                    break
            if (not removed):
                pairs.append((m, l))
        
        count = 0
        for i in xrange(len(pairs)):
            if(pairs[i] != - 1):
                count += 1

        print (n - count) / 2
except EOFError:
    pass
