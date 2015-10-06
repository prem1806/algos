for n in range(0000,2359):
	n2 = n
	p  = 0

	while n > 0:
		n1 = n % 10
		p = p * 10 + n1
		n = n / 10

	if p == n2 and p%100 < 60:
		print ("the palindrome is %d") %(p)
