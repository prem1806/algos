import random
def avg(l):
	l1 = 0
	for i in range(len(l)):
		l1+=i
	return l1/2

l = []
for i in range(1000):
	l.append(random.randint(1,1000))
print avg(l)
