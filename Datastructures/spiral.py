def auto(A):
    m = len(A)
    n = len(A[0])
    T = 0
    B = m - 1
    L = 0
    R = n - 1
    direction = 0
    ret = []
    while T <= B and L <= R:
        if (direction == 0):
            for i in range(L,R+1):
                ret.append(A[T][i])
                T += 1
                direction = 1
        elif direction == 1:
            for i in range(T,B+1):
                ret.append(A[i][R])
                R -= 1
                direction = 2
        elif direction == 2:
            for i in range(R, L - 1, -1):
                ret.append(A[B][i])
                B -= 1
                direction = 3
        else:
            for i in range(B,T-1, -1):
                ret.append(A[i][L])
                L += 1
                direction = 0
    return ret

A = [[1,2,3,4,5],[9,5,3,6,6,9,3],[1,5,3,8,6,4,2]]
print auto(A)

            


        