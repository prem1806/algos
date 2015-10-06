"""n = int(raw_input())
n2 = n
s = 0
i = 0
while n>0:
	n1 = n%10
	s= s *10 + n1
	n = n/10
	i+=1
if s==n2:
	print "it is palindrome"
else:
	print "is is not a palindrome"   """
# reverse a number

n = int(raw_input())
s = 0
i = 0
while n>0:
	n1 = n%10
	s = s*10+n1
	n = n/10
	i+=1
print s