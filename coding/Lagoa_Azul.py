a, p = map(int, raw_input().split())


count = 0
for i in xrange(a):
	positions = map(int, raw_input().split())
	if (len(positions) > 1): 
		if(positions[1] > 0): 
			count += 1
	for j in xrange(1, len(positions) - 1, 1):
		if(positions[j] > positions[j + 1]):
			count = count + 1
print count

			
