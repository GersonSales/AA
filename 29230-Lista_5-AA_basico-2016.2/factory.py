import random
import string

nFavourites = random.ranrange(27)
favourites = ""

for i in xrange(1, nFavourites):
    letter = random.choice(string.ascii_lowercase)
    if (not letter in favourites):
        favourites += letter
nameSize = 10**5
operations = 10**5
print "%d %d %d" %(nFavourites, nameSize, operations)
print favourites

name = ""

for i in xrange(nameSize):
    name += random.choice(string.ascii_lowercase)
print name

for i in xrange(operations):
    stLetter = random.choice(string.ascii_lowercase)
    ndLetter = random.choice(string.ascii_lowercase)
    print "%s %s" %(stLetter, ndLetter)

