""""Bank related  """
import sys
net_amount = 0
while True:
	s = raw_input()
	if not s:
		break
	value = s.split(" ")
	operation = value[0]
	amount = int(value[1])
	if operation == "D":
		net_amount += amount
	elif operation == "w":
		net_amount -= amount
	else: 
		pass

print net_amount