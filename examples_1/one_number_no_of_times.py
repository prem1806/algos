"""dic = {'1':1,'2':2,'3':4}
for (key,value) in dic.items():	
	if value % 2 == 0:
		continue
	else:
		print key"""
l = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
dic={}
for i in l:
	if i not in dic:
		dic[i]=1
	else:
		dic[i] += 1
print dic		
for (key,value) in dic.items():	
	if value % 2 == 0:
		continue
	else:
		print key
"""s = 0
for i in l:
	s = s^i
print s"""
