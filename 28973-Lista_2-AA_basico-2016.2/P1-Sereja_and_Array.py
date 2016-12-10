n, m = map(int, raw_input().split())

array = map(int, raw_input().split())

summ = 0

for i in xrange(m):
    op = map(int, raw_input().split())

    if(op[0] == 1):
        array[op[1] - 1] = op[2] - summ

    elif(op[0] == 2):
        summ += op[1]

    elif(op[0] == 3):
        result = array[op[1] - 1]
        print summ + result
