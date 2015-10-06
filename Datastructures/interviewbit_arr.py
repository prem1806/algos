"""def performOps(A):
    blen = 2 * len(A)
    B = [0]*blen
    for i in xrange(len(A)):
    	print i
        B[i] = A[i]
        B[i + len(A)] = A[(len(A) - i) % len(A)]
        print B
    return B

A=[5,10,2,1]
B = performOps(A)
for i in xrange(len(B)):
    print B[i],"""


"""a =[1,2,3,4,5,6]
temp =[1]
for i in a:
	if i == 1:
		print "u"
	elif i>1:
		temp.append(i)
print temp"""

def spiral(a,m,n):
	t = 0
	b = m-1
	l = 0
	r = n-1
	dir = 0
	while (t<=b and l<=r):
		if(dir==0):
			for i in range(l,r):
				print(a[t][i])
				t+=1
				dir=1
		elif (dir==1):
			for i in range(t,b):
				print(a[i][r])
				r-=1
				dir = 2
		elif (dir==2):
			for i in range(r,l):
				print(a[b][i])
				b-=1
				dir = 3
		elif (dir==3):
			for i in range(b,t):
				print(a[i][l])
				l+=1
				dir=(dir+1)%4


a = [[1,2,3,8],
[4,9,5,6],
[3,7,8,9]]
n,m=3,3
spiral(a,m,n)