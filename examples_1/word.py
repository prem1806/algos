def a():
	a = "abcd"
	b= raw_input()
	for c in b:
		if a.find(c)==-1:
			return False
		else:
			a = a.replace(c,"")
	return True

print a()