def total(n):
	if n == 0:
		return n
	elif n == 1:
		return n
	else:
		return n + total(n - 1)

print total(20)