def fact(n):
	num = 1
	while n>=1:
		num*=n
		n = n-1
	return num

n = int(raw_input())
print fact(n)