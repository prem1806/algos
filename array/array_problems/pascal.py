def fact(n):
	if n == 1:
		return  n
	else:
		return  n * fact(n-1) 

n,r = 10,3
print fact(n)
p = fact(n) /fact(n-r) * fact(r)
print p
