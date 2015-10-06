import random 
def max1(l):
	l1 = 0
	for i in range(len(l)+1):
		if i > l1:
			temp = i
			l1 = temp
	print l1

l = []
for i in range(1000):
	l.append(random.randint(1,1000))
max1(l)