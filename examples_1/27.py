def names(s1,s2):
	l1 = len(s1)
	l2 = len(s2)
	if l1 > l2:
		print l1
	elif l1 < l2:
		print l2
		print s1
		print s2 

s1,s2 = raw_input().split()
names(s1,s2)
