import math

print "welcome to python "
number = int(raw_input())
minimum = 10e9
point = []

def c_dis(p1,p2):
	distance = math.sqrt(((p2[0]-p1[0]) ** 2) + ((p2[1]-p1[1]) ** 2))
	return distance

for i in range(0,number):
	x, y = raw_input().split()
	x = int(x)
	y = int(y)
	point.append((x,y))

for i in range(0, len(point)):
	for j in range(i+1,len(point)):
		p1 = point[i]
		p2 = point[j]
		distance = c_dis(p1, p2)
		minimum  = min(distance, minimum)


print "minimum_distance = %d" % minimum