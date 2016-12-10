n = int(raw_input())
array = map(int, raw_input().split())

def isSorted(array = []):
    for i in xrange(len(array) - 1):
        if (array[i] > array[i + 1]):
            return False, i
    return True, 0

def getGreater(array = [], index = 0):
    for i in xrange(index + 1, len(array), 1):
        if (array[index] < array[i]):
            return i - 1
    return len(array) - 1

def revert(array = [], i = 0, j = 0):
    while(i < j):
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

isSortedv, index = isSorted(array)
greater = getGreater(array, index)

if(not isSortedv):
    revert(array, index, greater)

    if(not isSorted(array)[0]):
        print "no"
    else:
        print "yes"
        print "%d %d" %(index + 1, greater + 1)

else:
    print "yes"
    print "%d %d" %(index + 1, greater + 1)

