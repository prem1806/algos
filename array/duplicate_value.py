a = [0, 1, 2, 1, 1, 3, 4, 5,5]
for i in range(len(a)):
	for j in range ((i + 1),len(a)):
		if (a[i] == a[j]):
			print a[i]
			break