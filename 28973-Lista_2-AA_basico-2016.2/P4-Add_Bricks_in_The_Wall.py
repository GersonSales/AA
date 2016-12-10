n = int(raw_input())

for x in xrange(n):

    wall = [['' for x in range(i)] for i in xrange(1, 10)]


    for i in xrange(0, len(wall), 2):
        inputt = map(int, raw_input().split())
        x = 0;
        for j in xrange(0, len(wall[i]), 2):
            wall[i][j] = inputt[x]
            x += 1

    for i in xrange(2, len(wall), 2):
        summ = wall[i][0]
        for j in xrange(2, len(wall[i]), 2):
            summ += wall[i][j]
            wall[i][j - 1] = (wall[i - 2][j - 2] - summ) / 2
            summ = wall[i][j]


    for i in xrange(1, len(wall), 2):
        for j in xrange(0, len(wall[i]), 1):
            wall[i][j] = wall[i + 1][j] + wall[i + 1][j + 1]


    for i in xrange(len(wall)):
        for j in xrange(len(wall[i])):
            if (j + 1 < len(wall[i])):
                print  "%d" %(wall[i][j]),
            else:
                print "%d" %(wall[i][j])





