l = [200,35,76,90,200,35,35,90,90,90,76]
# a = {}
# for b in l:
# 	a[b] += 1

# for c in a:
# 	if a[c] %2 ==0:
# 		print c
# 		break


l.sort()
print l
a="prem"
count = 1
for b in l:
	if a==b:
		count +=1
	else:
		if count%2==0:
			print a
			break
		count = 0
		a=b


# s = 0
# for a in l:
# 	s =s^a
# print s




