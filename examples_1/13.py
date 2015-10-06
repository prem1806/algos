s = raw_input()
d ={ "digits" :0,"letters":0}
for c in s:
	if c.isdigit():
		d["digits"] +=1
	elif c.isalpha():
		d["letters"] +=1
	else: 
		pass

print d
print d["digits"]
print d["letters"]

