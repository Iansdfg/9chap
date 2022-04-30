"""
Objects:
    Coin
    VendingMachine,
    Item
        Coke
        Sprite
        MountDew
    State:
        Not Select
        Insert money

Work Flow
    Select Items ---Insert money --- Finish transaction
                                   L-- Cancel transaction

Case: 
    Select Items
    Insert money
        Finish transaction
    Cancel transaction




"""
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Coke(Item):
    def __init__(self):
        Item.__init__(self, 'Coke', 300)

class Sprite(Item):
    def __init__(self):
        Item.__init__('Sprite', 300)

class MountDew(Item):
    def __init__(self):
        Item.__init__('MountDew', 300)



class VendingMachine:
    """
    @return: nothing
    """
    def __init__(self):
        self.state = No_Selection(self)
        self.value = 0
        self.curr_item = None
        self.id_item = dict()

        self.No_Selection = No_Selection(self)
        self.Has_Selection = Has_Selection(self)
        self.Inserted_Money = Inserted_Money(self)

    def refill(self, id, item):
        if id not in self.id_item:
            self.id_item[id] = []
        self.id_item[id].append(item)

    def setSelectedItem(self, id):
        self.curr_item = self.id_item[id].pop(0)

    def selectItem(self, id):
        self.state.selectItem(id)
 
    def insertCoins(self, value):
        self.state.insertCoins(value)

    def executeTransaction(self):
        return self.state.executeTransaction()

    def cancelTransaction(self):
        self.state.cancelTransaction()

    def change_to_No_State(self):
        self.state = self.No_Selection
    def change_to_Has_Selection(self):
        self.state = self.Has_Selection
    def change_to_Inserted_Money(self):
        self.state = self.Inserted_Money


class State:
    def __init__(self, VM):
        self.vm = VM

class No_Selection(State):
    def __init__(self, VM):
        State.__init__(self, VM)

    def selectItem(self, id):
        self.vm.change_to_Has_Selection()
        self.vm.setSelectedItem(id)
        
    def insertCoins(self, value):
        print("Please make a selection first") 
    
    def executeTransaction(self):
        print("Please make a selection first")

    def cancelTransaction():
        print("Please make a selection first") 

class Has_Selection(State):
    def __init__(self, VM):
        State.__init__(self, VM)

    def selectItem(self, id):
        self.vm.setSelectedItem(id)

    def insertCoins(self, value):
        self.vm.value = value
        self.vm.change_to_Inserted_Money()

    def executeTransaction(self):
        print("Please pay first")

    def cancelTransaction(self):
        self.vm.value = 0
        self.vm.change_to_no_state()
 

class Inserted_Money(State):
    def __init__(self, VM):
        State.__init__(self, VM)

    def selectItem(self, id):
        print("Has incomplete transaction")

    def insertCoins(self, value):
        # self.vm.value += value
        print('paid')

    def executeTransaction(self):
        if self.vm.value < self.vm.curr_item.price:
            print("Insufficent amont")
            return 
        else:
            return self.vm.curr_item
        
    def cancelTransaction(self):
        self.vm.value = 0
        self.vm.change_to_no_state()


c1 = Coke()
vm = VendingMachine()
vm.refill('A1', c1)
vm.selectItem("A1")
vm.insertCoins(300)
item = vm.executeTransaction()
print(item.name)
