class Status:
    UP = 'UP'
    DOWN = 'DOWN'
    IDLE = 'IDLE'

class Directions:
    UP = 'UP'
    DOWN = 'DOWN'

class ElevatorSystem:
    def __init__(self):
        self.elevators = []
    
    def handle_request(self):
        request = ExternalRequest(level, direction)

class Elevator:
    def __init__(self):
        self.buttons = []
        self.up_stops = []
        self.down_stops = []
        self.curr_level = 1
        self.gate_open = False 

    def handle_exter_request(self):
        pass  
    
    def handle_inter_request(self):
        pass

    def open_gate(self):
        pass 

    def close_gate(self):
        pass

    def _is_request_valid(self):
        pass

class Request:
    def __init__(self, level = 0):
        self.level = level 

    def get_level(self):
        return self.level

class InternalRequest(Request):
    def __init__(self, get_level = None):
        Request.__init__(self, l)

class ExternalRequest(Request):
    def __init__(self, l = None, d = None):
        Request.__init__(self, l)
        self.direction = d

    def get_direction(self):
        return self.direction

class ElevatorButton:
    def __init__(self, l = 0, e = None):
        self.level = l
        self.elevator = e
    
    def press(self, level):
        request = InternalRequest(level)

