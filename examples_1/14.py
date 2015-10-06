s = raw_input()
d = {"uppercase":0,"lowercase":0 }
for p in s:
	if p.isupper():
		d["uppercase"] += 1
	elif p.islower():
		d["lowercase"] +=1
	else:
		pass

print d["uppercase"],"uppercase"
print d["lowercase"],"lowercase"
