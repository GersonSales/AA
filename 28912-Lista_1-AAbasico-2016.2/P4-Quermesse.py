count = 0
while 1:


	n = int(raw_input())

	if (n == 0): break
	count += 1
	print "Teste %d"%(count)
	elem = map(int, raw_input().split())

	for x in xrange(n):
		if (x + 1 == elem[x]):
			print elem[x]
			print ""
	
			break
	
