def bubbleSort(lst):
    for p in range(len(lst)-1,0,-1):
        for i in range(p):
            if lst[i]>lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp

lst = [12,6,3,1,7,23,10,17,11]
bubbleSort(lst)
print(lst)