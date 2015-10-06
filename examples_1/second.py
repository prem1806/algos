def fact(n):
	if n == 1:
		return n
	else:
		return n * fact(n-1)

n = raw_input()
n = int(n)
fact(n)
print "the out put should be: %d " %(fact(n))