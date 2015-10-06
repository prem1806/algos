l = [1,12,3,2,34,21,11,15,19]
n = 0
for i in range(len(l)):
	for j in range(i+1,len(l)):
		m = (l[i] + l[j])/2
		if m>n:
			n = m

print n