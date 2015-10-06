list=[[1,2,3],[2,3,4]]

def search(d):
	for i in range(0,len(list)):
		for j in range(0,len(list[i])):
			if list[i][j] == d:
				return True
	return False


d = raw_input()
d = int(d)
print search(d)

