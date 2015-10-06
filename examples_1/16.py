""""odd numbers in given list """

numbers = raw_input()

l = [x for x in numbers.split(" ") if int(x) % 2 !=0 ]

print ",".join(l)