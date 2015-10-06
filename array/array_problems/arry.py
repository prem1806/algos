"""l =[]
	l.append([1,2,3])
	l.append([])
"""
#INPUT
r,c = raw_input().split()
r,c = int(r), int(c)

lst = [[] for i in range(r)]

for i in range(0, r):
	for j in range(0, c):
		value = int(raw_input())
		lst[i].append(value)
#END OF INPUT 

print lst

for i in range(0,len(lst)):
	for j in range(0,len(lst[i])):
		lst[i][j] = (lst[i][j]*2)
		
print lst


    