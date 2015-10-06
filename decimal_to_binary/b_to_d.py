n=input()
i=0
s=0
while n!=0:
	s=s+(n%10)*(2**i)
	i=i+1
	n=n/10
print s
