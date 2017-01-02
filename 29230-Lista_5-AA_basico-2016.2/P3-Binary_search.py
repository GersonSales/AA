def binarySearch(element, elements = []):
    left = 0
    right = len(elements) - 1
    middle = (right + left) / 2

    while left <= right:
        if (elements[middle] == element):
            return middle
        else:
            if (elements[middle] < element):
                left = middle + 1
                middle = (right + left) / 2
            else:
                right = middle - 1
                middle = (right + left) / 2
    return -1


n, q = map(int, raw_input().split())

elements = map(int, raw_input().split())

for query in xrange(q):
    print binarySearch(int(raw_input()), elements)
