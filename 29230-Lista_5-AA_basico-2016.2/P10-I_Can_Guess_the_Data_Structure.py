def get(priorityQueue):
    if (len(priorityQueue) > 0):
        maxIndex = [0, priorityQueue[0]]
        for i in xrange(len(priorityQueue)):
            if (priorityQueue[i] > maxIndex[1]):
                maxIndex[0] = i
                maxIndex[1] = priorityQueue[i]
        return priorityQueue.pop(maxIndex[0])

try:
    while 1:
        stack = []
        queue = []
        priorityQueue = []

        isStack = True
        isQueue = True
        isPriorityQueue = True
        count = 3

        n = int(raw_input())
        for i in xrange(n):
            comand, number = map(int, raw_input().split())

            if (comand == 1):
                stack.append(number)
                queue.append(number)
                priorityQueue.append(number)
            else:
                if (number in stack):
                    if (number != stack.pop()):
                        if (isStack):
                            isStack = False
                            count -= 1
                else:
                    if (isStack):
                        isStack = False
                        count -= 1


                if (number in queue):
                    if (number != queue.pop(0) and isQueue):
                        isQueue = False
                        count -= 1
                else:
                    if (isQueue):
                        isQueue = False
                        count -= 1

                if (number in priorityQueue):
                    if (number != get(priorityQueue) and isPriorityQueue):
                        isPriorityQueue = False
                        count -= 1
                else:
                    if (isPriorityQueue):
                        isPriorityQueue = False
                        count -= 1


        if (count > 1):
            print "not sure"
        elif (count < 1):
            print "impossible"
        elif (isStack):
            print "stack"
        elif (isQueue):
            print "queue"
        elif (isPriorityQueue):
            print "priority queue"



except EOFError:
    pass
