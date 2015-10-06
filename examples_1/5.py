class In(object):
	def __init__(self):
		self.s = ""

	def getString(self):
		self.s = raw_input()

	def stringPrint(self):
		print self.s.upper()

	def stringPrint(self):
		print self.s.lower()

prem = In()
print prem.getString()
print prem.stringPrint()
print prem.stringPrint()