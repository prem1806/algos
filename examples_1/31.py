""" tuples """
def num(n):
	l = []
	for i in range(n):
		i = i**2
		l.append(i)
	x = tuple(l)
	t1 = x[5:]
	print t1

n = int(raw_input())
num(n)

"""t = (1,2,3,4,5,6,7,8,9)
t1 = t[5:]
print t1"""	

