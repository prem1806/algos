
def dtob(n):
	s=0
	i=0
	while n!=0:
		s=s+(n%2)*(10**i)
		n=n/2
		i=i+1
	return s

s = input()
print dtob(s)
while True:

	k=input()
	if k==-1:
		break
	d = 2**(k-1)
	print dtob((s&d)/d) ,