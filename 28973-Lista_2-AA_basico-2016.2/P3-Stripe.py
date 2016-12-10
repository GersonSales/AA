n = int (raw_input())

array = map(int, raw_input().split())
count = 0
generalSumm = sum(array)
intervalSumm = 0;

for i in xrange(len(array) - 1):
    intervalSumm += array[i]
    if (intervalSumm == generalSumm - intervalSumm):
        count +=1
print count
