l = [2, 4, 3, 5, 7, 6, 8]
l.sort()
print l
c = 0
i=0
j=len(l)-1

while i<j:
	c+=1
	if l[i]+l[j]<12:
		i+=1
	elif l[i]+l[j]>12:
		j-=1
	else:
		print l[i],l[j]
		i+=1
		j-=1
print c
