"""def squareSum(A):
	ans = []
	a = 0
	while a * a < A:
		b = 0
		while b * b < A:
			if a * a + b * b == A:
				newEntry = a, b
				ans.append(newEntry)
			b += 1
		a += 1
	return ans
	print ans
A = int(raw_input())
print squareSum(A)"""



a = int(raw_input())
d = []
b = 0
while b**2<a:
	c = 0
	while c**2<a:
		if b**2+c**2 ==a:
			e =b,c
			d.append(e)
		c+=1
	b+=1
print d