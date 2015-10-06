""" lists """

"""def num(n):
	l = []
	for i in range(n):
		i = i**2
		l.append(i)
	print l

n = int(raw_input())
num(n)"""
"""values accessing 1st 5"""

def num(n):
	l = []
	for i in range(n):
		i = i**2
		l.append(i)
	print l
	print l[:5],l[-5:],l[5:]

n = int(raw_input())
num(n)

