n = raw_input()
n = int(n)
c =0
p = 0
while n > 0:
	n1 = n % 10
	p += n1
	n /= 10
	c+=1

print p