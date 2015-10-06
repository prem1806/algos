a =[1,21,34,4,-5,6,7,8]
k=[],k1=[]
for i in range(len(a)):
	if a[i]>0:
		k.append(a[i])
	else:
		p=i
		break
for p in range(p+1,len(a)):
		k1.append(a[p])
if sum(k) >sum(k1):
	print "k is greater than k1"
else:
	print "bad"