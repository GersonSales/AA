import string
k, m, n = map(int, raw_input().split())

favourites = raw_input()
name = raw_input()

dic = {}
for letter in name:
    if (letter in dic):
        dic[letter] += 1
    else:
        dic[letter] = 1

maxFavourites = 0
for fav in favourites:
    if (fav in dic):
        maxFavourites += dic[fav]

operations = []
indexFavourite = -1
for i in xrange(n):
    stLetter, ndLetter = raw_input().split()

    if (stLetter in dic):
        if (ndLetter in dic):
            aux = dic[stLetter]
            dic[stLetter] = dic[ndLetter]
            dic[ndLetter] = aux
        else:
            dic[ndLetter] = dic[stLetter]
            dic[stLetter] = 0
    else:
        if (ndLetter in dic):
            dic[stLetter] = dic[ndLetter]
            dic[ndLetter] = 0

    countFav = 0
    for fav in favourites:
        if(fav in dic):
            countFav += dic[fav]

    if (countFav > maxFavourites):
        maxFavourites = countFav
        indexFavourite = i


    operations.append((stLetter, ndLetter))

exists = {}
for letter in string.ascii_lowercase:
    if (not (letter in exists)):
        if (letter in name):
            exists[letter] = True
        else:
            exists[letter] = False

alphabet = {}
for letter in string.ascii_lowercase:
    alphabet[letter] = letter

def findKey(dic, value):
    for key in dic.keys():
        if (dic[key] == value):
            return key
    return None
def associate(dic, oldValue, newValue):
    for key in dic.keys():
        if (dic[key] == oldValue):
            dic[key] = newValue


def dualAssociate(dic, value, otherValue):
    for key in dic.keys():

        if (dic[key] == value):
            dic[key] = otherValue
        elif (dic[key] == otherValue):
            dic[key] = value


for op in xrange(indexFavourite + 1):
    stLetter = operations[op][0]
    ndLetter = operations[op][1]

    if (exists[stLetter] and exists[ndLetter]):
        dualAssociate(alphabet, stLetter, ndLetter)

    elif (exists[stLetter] and not exists[ndLetter]):
        associate(alphabet, stLetter, ndLetter)
        exists[stLetter] = False
        exists[ndLetter] = True

    elif (not exists[stLetter] and exists[ndLetter]):
        associate(alphabet, ndLetter, stLetter)
        exists[ndLetter] = False
        exists[stLetter] = True


newName = ""
for letter in name:
    if (letter in alphabet):
        newName += alphabet[letter]
    else:
        newName += letter
name = newName


print maxFavourites
print name
