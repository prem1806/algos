class Reservation:
   def __init__(self,passenger_id,passenger_fname,passenger_lname):
      self.passenger_id = passenger_id
      self.passenger_fname = passenger_fname
      self.passenger_lname = passenger_lname
      self.cost = 0
      self.reservation_id = []
      self.passenger_record = {'p_name'  : self.passenger_fname + self.passenger_lname,
                             'p_id'    : self.passenger_id,
                             'p_wallet': self.cost,
                             'p_reservation_id': self.reservation_id,
                            }
      self.hotel_room = {'Penthouse'             : 10,
                       'King Deluxe Bedroom'    : 20,
                       'Queen Deluxe Bedroom'   : 20,
                       'Kind Standard Bedroom' : 30,
                       'Queen Standard Bedroom': 50 }
      self.hotel_price = {'Penthouse'            : 1000,
                        'King Deluxe Bedroom'    : 700,
                        'Queen Deluxe Bedroom'   : 600,
                        'Kind Standard Bedroom' : 450,
                        'Queen Standard Bedroom': 350 }


class Hotel(Reservation):
    def __init__(self,passenger_id,passenger_fname,passenger_lname,hotel_room_selection,
             hotel_check_in_date,hotel_check_out_date):
        Reservation.__init__(self,passenger_id,passenger_fname,passenger_lname)
        self.hotel_room_selection = hotel_room_selection
        self.hotel_check_in_date = hotel_check_in_date
        self.hotel_check_out_date = hotel_check_out_date

    def CheckAvailability(self):
        if (self.hotel_room.get(self.hotel_room_selection) != 0):
            self.hotel_room[self.hotel_room_selection] -= 1
            self.passenger_record['p_wallet'] += self.hotel_price[self.hotel_room_selection]
            print "\n\nReserved Hotel Room\n\n"

"""A1 = Airline("1","Arun","Raman","Business Class","07-07-2014")
A1.CheckAvailability()
A1.currentStatus("Airline")"""
H1 = Hotel("1","Arun","Raman","Penthouse","07-07-2014","07-10-2014")
H1.CheckAvailability()
H1.currentStatus("Hotel")