#permitaion....
def permutate(seq):
    if not seq:
        return [seq]  
    else:
        temp = []
        for k in range(len(seq)):
            part = seq[:k] + seq[k+1:]
            print k, part  # test
            for m in permutate(part):
                temp.append(seq[k:k+1] + m)
                print "the temp var"
                print m, seq[k:k+1]  # test
        #print temp
        return temp





permutate('pre')