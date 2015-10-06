menu_list = {"idly": 23, "dosa": 34, "puri": 25}

print "\tMenu\n"
for key in menu_list:
	print key,menu_list[key]


print "Enter items one by one in line"

total_cost = 0

while True:
	inp = raw_input()
	if inp == 'END':
		break
	else:
		name, quantity = inp.split()
		quantity = int(quantity)
		total_cost = total_cost +  (menu_list[name] * quantity)

print "Thanks for the order. Your total cost is: ", total_cost


