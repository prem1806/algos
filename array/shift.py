def shift(s, n):
    shifted = []
    for i in range(len(s)):
    	print i,n,len(s)
        shifted.append(s[(i+n) % len(s)])
        print shifted
    return shifted

print shift([1, 2, 3, 4, 5], 2)