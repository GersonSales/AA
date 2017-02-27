#http://codeforces.com/problemset/problem/727/A

def fillTree(a = 0, b = 0, tree = {}):
    if (a > b):
        return a

    if (not a in tree.keys()):
        tree[a] = []

    numberToAdd = fillTree(a * 2,  b, tree)
    tree[a].append(numberToAdd)

    numberToAdd = fillTree(a * 10 + 1, b, tree)
    tree[a].append(numberToAdd)


    return a
def findB(tree, a, b, listt = []):
        listt.append(a)
        if (not a in tree.keys()):
            listt.pop()
        else:

            if (a == b):
                global result
                result = " ".join(map(str, listt))

                return listt

            for value in tree[a]:
                findB(tree, value, b, listt)
            listt.pop()

        return listt
tree = {}
a, b = map(int, raw_input().split())

fillTree(a, b, tree)
print "FillTree"

result = []
findB(tree, a, b)

if (str(b) in result):
    print "YES"
    print (len(result.split()))
    print result
else:
    print "NO"

