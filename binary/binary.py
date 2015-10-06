def binarySearch(l, item):
	low = 0
	high = len(l)-1
	found = False
	while low<=high and not found:
	    midpoint = (low + high)//2
	    if l[midpoint] == item:
	    	found = True
	    else:
	        if item < l[midpoint]:
	        	high = midpoint-1
	        	print high
	        else:
	            low = midpoint+1
	            print low,
	return found
	    
	
l = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(l, 42))
