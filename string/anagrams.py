a = raw_input()
d = raw_input()

b = sorted(a)
print b
c = ''.join(b)
print c
e = sorted(d)
print e
f = ''.join(e)
print f
if c == f:
	print "it is a anagram"
else:
	print "it is not anagram"