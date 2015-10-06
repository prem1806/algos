r,c = raw_input().split()
r,c = int(r),int(c)

l = [[] for i in range(r)]

for i in range(0,r):
	for j in range(0,c):
		values = int(raw_input())
		l[i].append(values)

print l
