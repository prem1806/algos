"""l = [1,2,3,4,5,63,2,45,4,5,4,3,90]
l.sort()
print l[len(l)-1] """

l = [120,29,3,4,5,63,145,90]
h = 0
for i in range(len(l)):
	if l[i] > h:
		h = l[i]
	
print h   
