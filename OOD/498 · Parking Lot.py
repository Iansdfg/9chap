# enum type for Vehicle
class VehicleSize:
    Motorcycle = 1
    Compact = 2
    Large = 3
    Other = 99

class Vehicle:
    # Write your code here
    def __init__(self):
        self.parkingspot = []
        self.spot_needed = 0
        self.size = None 
    
    def get_spot_needed(self, ):
        return self.spot_needed
    
    def get_size(self, ):
        return self.size
    
    def park_in_spot(self, spot):
        self.parkingspot.append(spot)


class Motorcycle(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spot_needed = 1 
        self.size = VehicleSize.Motorcycle

    def can_fit_in_spot(self, spot):
        return True 

class Car(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spot_needed = 1 
        self.size = VehicleSize.Compact

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.Compact or spot.get_size() == VehicleSize.Large

class Bus(Vehicle):
    # Write your code here
    def __init__(self):
        Vehicle.__init__(self)
        self.spot_needed = 5
        self.size = VehicleSize.Large

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.Large

class ParkingSpot:
    def __init__(self, lv, row, n, sz):
        self.level = lv
        self.row = row
        self.spot_number = n 
        self.spot_size = sz 
        self.vehicle = None 
    
    def is_available(self):
        return self.vehicle == None 

    def can_fit_vehicle(self, vehicle):
        return self.is_available() and vehicle.can_fit_in_spot(self)
    
    def park(self, v):
        if not self.can_fit_vehicle(vehicle):
            return False 
        
        self.vehicle = v 
        self.vehicle.park_in_spot(self)
        return True 
    
    def remove_vehicle(self):
        self.level.spot_freed()
        self.vehicle = None

    def get_row(self):
        return self.row = row
    
    def get_spot_number(self):
        return self.spot_number

    
class Level:
    # Write your code here

    def __init__(self):
        pass

    def park_vehicle():
        pass 

    def find_avaliable_spot():
        pass

    def park_starting_at_spot():
        pass

    def spot_freed():
        pass

    def get_available_spots():
        pass


class ParkingLot:
    # @param {int} n number of leves
    # @param {int} num_rows  each level has num_rows rows of spots
    # @param {int} spots_per_row each row has spots_per_row spots
    def __init__(self, n, num_rows, spots_per_row):
        # Write your code here


    # Park the vehicle in a spot (or multiple spots)
    # Return false if failed
    def park_vehicle(self, vehicle):
        # Write your code here


    # unPark the vehicle
    def unpark_vehicle(self, vehicle):
        



