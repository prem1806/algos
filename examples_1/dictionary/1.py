"""l = {}
l['a']= 20
l['b']= 32
l['c']= 45
l['d']=56
print l
for keys in l:
	print ("good ",key)"""

total = 0
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
for akey in mydict:
	print akey,mydict[akey]
   	if len(akey) > 3:
   		total = total + mydict[akey]
print(total)