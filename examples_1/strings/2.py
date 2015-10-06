"""count how many words in the given list"""
def group(n):
	upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	lower = 'abcdefghijklmnopqrstuvwxyz'
	total = 0
	no_of_p = 0
	for i in n:
		if i in upper or i in lower:
			total+=1
			if i == 'p':
				no_of_p +=1
    
	print total,no_of_p
	print("the total number of characters : %d \nnumber of p in the given list : %s") %(total,no_of_p)


n = raw_input()
print group(n)
