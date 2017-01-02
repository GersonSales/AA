n = int(raw_input())

for i in xrange(n):
    word = raw_input()
    middle = len(word) / 2
    result = ""
    for x in xrange(middle -1, -1, -1):
        result += word[x]

    for x in xrange(len(word) - 1, middle - 1, -1):
        result += word[x]

    print result
