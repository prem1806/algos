steve = raw_input("enter the name:")

reverse_steve = ""

for i in range(len(steve)-1,-1,-1):
	reverse_steve = reverse_steve + steve[i]

print reverse_steve 


