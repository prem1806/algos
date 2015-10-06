"""a = []
n = int(raw_input())
for i in range(1,n):
	if (n%i==0):
		a.append(i)
		a.append(n%i)
print a
"""

"""a = int(raw_input())
for i in range(2,a-1):
	if (a%i):
		print "is not prime number" """

def isPrime(n):
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
        	k=n%i
        	print k
        	return False

    return True

n = int(raw_input())
print isPrime(n)
