
def hcf(a, b):
	while b:
		p = b
		print p
		b = a % b
		print b
		a = p
		print a
	return a
	

a = int(raw_input())
b = int(raw_input())	
print hcf(a,b)