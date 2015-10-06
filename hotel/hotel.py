class Hotel(object):
 	def __init__(self,hotel_name,ac_rooms,non_ac_rooms):
 		self.hotel_name = hotel_name
 		self.ac_rooms = ac_rooms
 		self.non_ac_rooms = non_ac_rooms


 	def resever(self,ac,rooms):
 		if ac:
 			if self.ac_rooms >= rooms:
 				self.ac_rooms -= rooms
 				print "you are ac rooms reserved"
 			else:
 				print "Reservation failed"
 		else:
 			if self.non_ac_rooms>=rooms:
 				self.non_ac_rooms -= rooms
 				print "you are non ac rooms are reserved"
 			else:
 				print "Reservation failed"
 	def vacate(self,ac,rooms):
 		if ac:
 			self.ac_rooms += rooms
 			print "you are vacating from ac room "
 		else:
 			self.non_ac_rooms += rooms
 			print "you are vacating from non ac rooms"


h = Hotel("prem",int(25),int(25))

while True:
	print "welcome to *** Hotel *****"
	print"\t1)reserve"
	print"\t2)vacate"
	print "\t3)exit"
	option = int(raw_input("What do you want to do :"))
	if option == 1:
		ac = input("Do you want AC?")
		rooms = input("Enter no of rooms :")
		h.resever(ac,rooms)
	elif option == 2:
		ac = input("Are you vacating AC room?")
		rooms = input("Enter no of rooms :")
		h.vacate(ac,rooms)
	elif option == 3:
		break











