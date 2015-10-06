""" class """
"""class Amirica(object):
	def __init__(self,name,nationality,state):
		self.name = name
		self.nationality = nationality
		self.state = state

	def printNationality(self):
		print self.nationality

class Newyork(Amirica):
	def printNewyork(self):
		print self.state
		

demo = Newyork("prem","Amirican","Newyork")
print demo.name
print demo.printNationality()
print demo.printNewyork()"""

class Circle(object):
	def __init__(self,r,pi):
		self.r = r
		self.pi = pi

	def area_of_circle(self):
		a = self.pi * (self.r)**2
		print a

area = Circle(20,3.142)
print area.area_of_circle()
