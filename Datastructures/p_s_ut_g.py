n = int(raw_input())
m = []
for num in range(2,n+1):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       m.append(num)

print m
for i in m:
	for j in m:
		if i+j==n:
			print i,j
