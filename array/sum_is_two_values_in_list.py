l = [2, 4, 3, 5, 7, 5, 6, 8]
for i in range(len(l)):
	for j in range ((i + 1),len(l)):
		if l[i]  +  l[j] == 6:
			print l[i],l[j]