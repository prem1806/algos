print "\t\tcredit card validator"
input_string = raw_input()
name = []
var = input_string[len(input_string) - 1]
input_string = input_string[0:len(input_string)-1]
var = int(var)
input_string = input_string[::-1]

for i in range(0,len(input_string)):
	name.append(int(input_string[i]))

for i in range(0,len(name)):
	if i % 2 != 0:
		name[i] = name[i] * 2

for i in range(0,len(name)):
	if name[i] >= 9:
		name[i] = name[i] - 9

result = sum(name)
result = result % 10

if var == result:
	print "card is validated"
else:
	print "card is not validated" 