
class HotelReservation():

	def __init__(self):
		r,c = 1, 30
		self.ac_rooms = [[None for j in range(c)] for i in range(r)]
		self.non_ac_rooms = [[None for j in range(c)] for i in range(r)]
		self.ac_room_price = 1000
		self.non_ac_room_price = 750

	
	def check_for_vacancy(self, room_type, sdate, edate):
		if room_type == 'AC':
			for i in range(len(self.ac_rooms)):
				flag = 0
				num_of_days = edate - sdate
				for j in range(sdate, edate):
					if self.ac_rooms[i][j] == None:
						flag = flag + 1
				if flag == num_of_days:
					return (i, True)
			return (0, False)
		else:
			for i in range(len(self.non_ac_rooms)):
				flag = 0
				num_of_days = edate - sdate
				for j in range(sdate, edate):
					if self.non_ac_rooms[i][j] == None:
						flag = flag + 1
					if flag == num_of_days:
						return (i, True)
			return (0, False)
	

	def check_in(self, name, room_type, sdate, edate):
		index, isvacant = self.check_for_vacancy(room_type, sdate, edate)
		if isvacant == True:
			if room_type == 'AC':
				for j in range(sdate, edate):
					self.ac_rooms[index][j] = name
			else:
				for j in range(sdate, edate):
					self.non_ac_rooms[index][j] = name
		else:
			print "Sorry No rooms are available"


	def check_out(self, room_type, name):
		if room_type == 'AC':
			total_days = 0
			for i in range(0, len(self.ac_rooms)):
				for j in range(0, len(self.ac_rooms[i])):
					if self.ac_rooms[i][j] == name:
						total_days = total_days + 1
						self.ac_rooms[i][j] = None
			cost = total_days * self.ac_room_price
			print "cost for your stay: %d" % cost
		else:
			total_days = 0
			for i in range(0, len(self.non_ac_rooms)):
				for j in range(0, len(self.non_ac_rooms[i])):
					if self.non_ac_rooms[i][j] == name:
						total_days = total_days + 1
						self.non_ac_rooms[i][j] = None
			cost = total_days * self.non_ac_room_price
			print "cost for your stay: %d" % cost


if __name__ == "__main__":
	hotel_object = HotelReservation()
	while True:
		hotel_object.check_in('rohith', 'AC', 1, 4)
#		hotel_object.check_out('AC', 'rohith')
		hotel_object.check_in('rahul', 'NONAC', 2, 6)
#		hotel_object.check_out('NONAC', 'rahul')
		hotel_object.check_in('prem', 'AC', 2, 6)
		hotel_object.check_in('shammi', 'NONAC', 7, 10)
		print hotel_object.non_ac_rooms
		hotel_object.check_out('NONAC', 'shammi')
		break









