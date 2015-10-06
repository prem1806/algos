"""n = int(raw_input())
for num in range(2,n+1):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print num"""


def p(n):
	if n == 1:
		return "prime number are start at 2"
	else:
		for i in range(1,n):
			if n%i==0:
				return False
			return True
n = int(raw_input())
print p(n)

