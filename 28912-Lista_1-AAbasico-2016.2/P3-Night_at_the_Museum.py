import string 

def indexOf(letter) :
	return string.lowercase.index(letter)


usrInput = raw_input()

actualLetter = 'e'
summ = 0;

for letter in usrInput:
	maxx = max(indexOf(actualLetter))
	minn = min(indexOf(letter))
	summ = summ + (26 - (maxx - minn))

	
	
	actualLetter = letter
print summ
