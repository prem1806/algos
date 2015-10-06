"""d = {}
d["prem"] = 344
del d["prem"]
print d"""

"""def printdict():
	d = {}
	d[1] = 1
	d[2] = 2**2
	d[3] = 3**3
	print d
	print d[1]
printdict()"""


"""l = [i for i in raw_input().split()]
l.sort()
print l"""


"""" values insert and one perticulor value acessing """ 

"""d = {}
for i in range(1,21):
	d[i] = i**2

print d
print d.items()[8] """

""" only valuse or keys """
'''d = {}
for i in range(1,21):
	d[i] = i**2
print d
for (k,v) in d.items():
	print k,
	print v,'''

d = { i for i in raw_input().split()}
print d
