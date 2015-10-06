def insertion(a):
	for i in range(1,len(a)):
		p = a[i]
		q = i
		while (q > 0 and a[q-1] > p):
			a[q] = a[q-1]
			q = q-1
		a[q] = p

a = [1,2,3,6,7,8,34,5,23,9]
insertion(a)
print a