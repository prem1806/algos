l = [2,6,8,14,19,18,24,30]
print len(l)
for i in range(len(l)-1):
	if l[i+1] < l[i]:
		print l[i]
		break