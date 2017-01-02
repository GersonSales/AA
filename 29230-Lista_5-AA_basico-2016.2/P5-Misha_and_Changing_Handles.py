n = int(raw_input())

dic = {}

for i in xrange(n):
    old, new = raw_input().split()
    hasChanged = False
    for value in dic.values():
        if (old == value):
            for key in dic.keys():
                if (dic[key] == value):
                    dic[key] = new
                    hasChanged = True
    if (not hasChanged):
        dic[old] = new
print len(dic)

for key in dic.keys():
    print key, dic[key]
