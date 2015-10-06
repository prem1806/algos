'''
Finding LCM of two numbers
@Author: Rohith
'''

def lcm(a, b):
	cnt = 2
	while True:
		if cnt % a == 0 and cnt % b == 0:
			break
		cnt = cnt + 1
	return cnt


def hcf(a, b):
	# lcm(a, b) * hcf(a, b) = a*b
	prod = lcm(a, b)
	return (a*b) / prod


if __name__ == "__main__":
	a,b = raw_input().split()
	a,b = int(a), int(b)
	print lcm(a, b)
	print hcf(a, b)
