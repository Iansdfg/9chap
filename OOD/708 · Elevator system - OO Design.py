"""
Workflow:
   level request ----> elevator system ----> elevator 

Objects
    request 
        in 
        ex
    elevator 
    elevator system 


case:

    internal request 
    external request 

"""


from turtle import up
from urllib import request
from prometheus_client import Enum


class ElevatorSystem:
    def __init__(self):
        self.elevators = []
        e1 = Elevator()
        self.elevators.append(e1)
    

    def choose_elev(self):
        for elevator in self.elevators:
            if True:#condition
                return elevator

    def ExternalRequest(self, lv, dirc):
        elevator = self.choose_elev()
        elevator.ExternalRequest(lv, dirc)

    def InternalRequest(self, lv):
        elevator = self.choose_elev()
        elevator.InternalRequest(lv)
    

class Elevator:
    def __init__(self):
        self.curr_level = 0 
        self.curr_status = 'idel'
        self.up_list = []
        self.down_list = []

    def ExternalRequest(self, lv, dirc):
        ex_request = ExternalRequest(lv, dirc)
        ex_request.excute(self)
        self.print_status()

    def InternalRequest(self, lv):
        in_request = InternalRequest(lv)
        in_request.excute(self)
        self.print_status()

    def openGate(self):
        if not self.down_list and not self.up_list:
            self.curr_status = 'idel'

        elif not self.up_list:
            curr_lv = self.down_list.pop()
            self.curr_level = curr_lv
        
        elif not self.down_list:
            curr_lv = self.up_list.pop()
            self.curr_level = curr_lv
        else:
            if self.up_list and self.curr_status == 'up':
                curr_lv = self.up_list.pop()
                self.curr_level = curr_lv
            elif self.down_list and self.curr_status == 'down':
                curr_lv = self.down_list.pop()
                self.curr_level = curr_lv

        self.print_status()

    def closeGate(self):
        if not self.up_list:
            self.curr_status = 'down'
        elif not self.down_list:
            self.curr_status = 'up'
        else:
            self.curr_status = 'idle'


    def update_level(self):
        pass 

    def add_up(self):
        pass

    def add_down(self):
        pass

    def change_up(self):
        pass

    def change_down(self):
        pass


    def print_status(self):
        print('Currently elevator status is : ', self.curr_status)
        print('Current level is at: ', self.curr_level)
        print('up stop list looks like: ', self.up_list)
        print('down stop list looks like: ', self.down_list)
        print('##############################')


class ExternalRequest:
    def __init__(self, lv, dirc):
        self.level = lv 
        self.direction = dirc

    def excute(self, elevator):
        if self.level > elevator.curr_level:
            elevator.curr_status = 'up'
        elif self.level < elevator.curr_level:
            elevator.curr_status = 'down'

        if self.direction == 'Down':
            elevator.down_list.append(self.level)
            elevator.down_list.sort()
        else:
            elevator.up_list.append(self.level)
            elevator.up_list.sort()


class InternalRequest:
    def __init__(self, lv):
        self.level = lv  

    def excute(self, elevator):
        if self.level > elevator.curr_level:
            elevator.down_list.append(self.level)
            elevator.down_list.sort()
        elif self.level < elevator.curr_level:
            elevator.up_list.append(self.level)
            elevator.up_list.sort()

# es = ElevatorSystem()
e1 = Elevator()
e1.ExternalRequest(3, "Down")
e1.ExternalRequest(2, "Up")
e1.openGate()
e1.closeGate()
e1.InternalRequest(1)
e1.openGate()
e1.closeGate()
e1.openGate()
e1.closeGate()
e1.openGate()
e1.closeGate()
