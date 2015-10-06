"""import math
a = int(raw_input())
b = math.sqrt(a)
print a,b
"""
def sr(n):
	root = n/2
	for i in range(12):
		root = (1/2) * (root + (n/root))
	return root
print sr(9)
