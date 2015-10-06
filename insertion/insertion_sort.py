def insertionSort(lst):
   for i in range(1,len(lst)):
   	value = lst[i]
    p = i
	while p>0 and lst[p-1]>value:
    	lst[p]=lst[p-1]
        p = p-1

    lst[p]=value

lst = [5,2,3,1,7,21,98,13,34]
insertionSort(lst)
print(lst)
