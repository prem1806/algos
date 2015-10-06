def check_empty(lst):
    for i in range(0, len(lst)):
        for j in range(0, len(lst[i])):
            if lst[i][j] == -1:
                return False
    return True


def check_for_unique(lst):
    hash_dict = [False for i in range(1, 11)]
    for l in lst:
        hash_dict[l] = True
    for i in range(1, 10):
        if hash_dict[i] == False:
            return False
    return True


def row_check(lst):
    for i in range(0, len(lst)):
        value = check_for_unique(lst[i])
        if value == False:
            return False
    return True

                
def col_check(lst):
    for j in range(0, len(lst)):
        temp_lst = []
        for i in range(0, len(lst[j])):
            temp_lst.append(lst[i][j])
        value = check_for_unique(temp_lst)
        if value == False:
            return False
    return True


def square_check(lst):
    for i in range(0, len(lst), 3):
        for j in range(0, len(lst[i]), 3):
            sx,ex = i, i+3
            sy,ey = j, j+3
            temp_lst = [lst[k][l] for k in range(sx, ex) for l in range(sy, ey)]
            value = check_for_unique(temp_lst)
            if value == False:
                return False
    return True


r,c = raw_input().split()
r,c = int(r), int(c)

lst = [[] for i in range(r)]

for i in range(0, r):
	for j in range(0, c):
		value = int(raw_input())
		lst[i].append(value)

print lst

if not check_empty(lst):

    print "Invalid sudoku 1"
elif not row_check(lst):
    print "invalid sudoku 2"
elif not col_check(lst):
    print "invalid sudoku 3"
elif not square_check(lst):
    print "invalid sudoku 4"
else:
    print "yayy!!!this is valid sudoku"

		


