""" multiplication table"""

def num(n):
	for i in range(1,11):
		p = n * i
		print("%d * %d = %d") %(n,i,p)
		
n = int(raw_input())
num(n) 