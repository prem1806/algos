def l(p):
    for x in range(0,len(p) - 1):
        if p[x+1] - p[x] != 1:
            print p[x] + 1

l(p = [1,2,3,4,5,6,8,9,10])
