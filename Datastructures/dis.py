import math
def c_dis(p1,p2):
	distance = math.sqrt(((p2[0]-p1[0]) ** 2) + ((p2[1]-p1[1]) ** 2))
	return distance

p1 = (1,2)
p2 = (2,1)
print c_dis(p1,p2)