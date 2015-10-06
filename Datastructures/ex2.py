def squareSum(A):
	ans = []
	a = 0
	while a * a < A:
		b = 0
		while b * b < A:
			if a * a + b * b == A:
				print a,b
				ans.append(a)
				ans.append(b)
			b += 1
		a += 1
	return ans
print squareSum(A=int(raw_input()))
