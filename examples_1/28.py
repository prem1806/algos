def num(n):
	if n % 2 == 0:
		print "it is a even number "
	elif n % 2 != 0:
		print "it is a odd number "
	else: 
		print "nope"

n= int(raw_input())
num(n)