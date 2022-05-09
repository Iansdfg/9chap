"""

Workflow:
    search --> bookingSystem--> hotel

Case:
    Search 
    Select and Book 
    Cancle 

Object:
    BookingSystem
    Hotel
    Room
        Single
        Double 

Example:
    Expedia = BookingSystem() #singleton 
    Hilton = Hotel()
    Marriot = Hotel()
    Room_type_list = Expedia.search(date, size)
    Expedia.Book(room_type)
    Expedia.Canle(room_type)
"""


class BookingSystem:
    instance = None 
    @classmethod
    def getInstance(cls):
        if cls.instance:
            cls.instance = BookingSystem()
        return BookingSystem.instance

    hotels = []

    def add_hotel(self, hotel):
        self.hotels.append(hotel)

    def search(self, time, size):
        for hotel in self.hotels:
            avaliable_rooms = hotel.find_room(time, size)

        roomtype_to_roomlist = hashMap(avaliable_rooms)
        room_number = 
        return roomtype_to_roomlist.keys

    def book_rooms(room):
        pass


    def cancel_rooms(room):
        pass

    
    def print_hotel(self):
        for hotel in self.hotels:
            print(hotel.name)


class Hotel:
    def __init__(self, n):
        self.name = n
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def find_room(self, time, size):
        for room in self.rooms:
            rooms = check_condition()
        
        return rooms


class Room:
    def __init__(self, hotel_name, room_type, capacity):
        self.hotel_name = hotel_name
        self.room_type = room_type
        self.capacity = capacity
        self.avaliable = True 
        self.avalibility = [[1, 31]]

class SingleRoom(Room):
    def __init__(self, hotel_name):
        Room.__init__(hotel_name, 'single', 2)


class DoubleRoom(Room):
    def __init__(self, hotel_name):
        Room.__init__(hotel_name, 'double', 4)



Expedia = BookingSystem() #singleton 
Hilton = Hotel('Hilton')
Hilton = Hotel('Marriot')

Expedia.add_hotel(Hilton)
Expedia.print_hotel()
