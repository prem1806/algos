class Hotel(object):
 	def __init__(self,hotel_name,type_room,total_rooms):
 		self.hotel_name = hotel_name
 		self.type_room = type_room
 		self.total_rooms = total_rooms

h = Hotel('prem','a/c',8)
print h.hotel_name
