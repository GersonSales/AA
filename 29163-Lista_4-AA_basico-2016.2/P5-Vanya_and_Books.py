books = raw_input()
length = len(books)
result = length * (int(books) + 1)

for i in xrange(length):
    result -= 10**i
print result
