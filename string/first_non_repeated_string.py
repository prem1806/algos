l = raw_input()

flag = 0
for i in range(len(l)):
	for j in range(i+1,len(l)):
		if l[i] != l[j]:
			continue
		else:
			flag = 1
			break
	if flag == 1:
		continue
	else:
		print "Yayy!!! i found first non repeated charcater"
		print l[i]
		break

