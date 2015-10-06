net_amount = 0
d,w = raw_input().split()
d,w = int(d),int(w)
if d > 0:
	net_amount+=d
	print net_amount
elif w > 0:
	net_amount -= w
	print net_amount

print net_amount
