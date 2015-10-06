n=input()
s=0
i=0
while n!=0:
	s=s+(n%2)*(10**i)
	n=n/2
	i=i+1
print s