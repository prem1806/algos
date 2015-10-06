"""l = raw_input('enter the name:')
print l
b = l[::-1]
print b"""

"""l = raw_input('enter a string:')
s = ''
for i in range(len(l)-1,-1,-1):
	s += l[i]

print s"""
n = raw_input()
n = int(n)
n2 = n
p = 0
while n > 0:
	n1 = n % 10
	p = p * 10 + n1
	n = n / 10

print p
if p == n2:
	print "it is a palindrom"
else:
	print "it is not a palindrom"