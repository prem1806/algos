class Product(object):
	def __init__(self):
		self.product_details = {}

	def sell_product(self, name, quantity):
		present_quantity = self.product_details[name][1]
		if present_quantity < quantity:
			print "Insufficient quantity"
		else:
			present_quantity -= quantity
			self.product_details[name][1] = present_quantity
			print "%d units of %s medicine have been sold" %(quantity, name)

	def buy_product(self, name, quantity, price):
		if name not in self.product_details.keys():
			self.product_details[name] = []
			self.product_details[name].append(price)
			self.product_details[name].append(quantity)
		else:
			present_quantity = self.product_details[name][1]
			present_quantity = present_quantity + quantity
			self.product_details[name][0] = price
			self.product_details[name][1] = present_quantity
		print "%d units of %s medicine hav been purchased" %(quantity, name)


if __name__ == "__main__":
	prod_object = Product()
	while True:
		print "welcome to Prem medical shop"
		print"\t1)sell medicine"
		print"\t2)purchase medicine"
		print "\t3)exit"
		option = int(raw_input("What do you want to do :"))
		if option == 1:
			print "Enter Name and quantity"
			name, quantity = raw_input().split()
			quantity = int(quantity)
			prod_object.sell_product(name, quantity)

		elif option == 2:
			print "Enter Name and quantity"
			name, quantity, amount = raw_input().split()
			quantity = int(quantity)
			amount   = int(amount)
			prod_object.buy_product(name, quantity, amount)

		elif option == 3:
			print "Thank you for using your software"
			break



		