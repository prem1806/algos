"""def isprime(n):
	for i in range(2,n):
		if (i % 2 ==0):
			print i

n = int(raw_input())
print isprime(n)"""

for num in range(2,101):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
        return True


"""
n = int(raw_input())
for test in range(1,n):
	if is_prime(test):
		print test"""