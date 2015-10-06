def isPrime(A):
	for i in range(2,A):
		if A % i == 0:
			return False
	return True

A =int(raw_input())
print isPrime(A)