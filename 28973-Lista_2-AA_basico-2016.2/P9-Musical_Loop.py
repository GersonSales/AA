while 1:
    n = int(raw_input())
    if (n == 0): break

    loop = map(int, raw_input().split())
    if (len(loop) > 0):
        loop.append(loop[0])
        loop.append(loop[1])

    goingUP = False
    goingDown = False

    count = 0
    if  (loop[0] < loop[1]):
        goingUP = True
    elif (loop[0] > loop[1]):
        goingDown = True

    aux = loop[0]

    for i in xrange(1, len(loop)):
        if (goingUP and aux > loop[i]):
            count += 1
            goingUP = False
            goingDown = True

        elif (goingDown and aux < loop[i]):
            count += 1
            goingUP = True
            goingDown = False

        aux = loop[i]

    print count





