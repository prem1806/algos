def ssort(lst):
   for i in range(len(lst)-1,0,-1):
       p=0
       for l in range(1,i+1):
           if lst[l]>lst[p]:
               p = l

       temp = lst[i]
       lst[i] = lst[p]
       lst[p] = temp

lst = [4,36,11,19,32,54,23,5,2]
ssort(lst)
print(lst)
       