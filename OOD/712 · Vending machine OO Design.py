from enum import Enum
import abc
import collections

class ItemInfo(object): # A1 -> Sprite A2 -> Coke
    def __init__(self, name, price):
        self.price = price
        self.name = name # sprite, coke, cake   

class Sprite(object): # Inheritance
    def __init__(self):
        self.info = ItemInfo("Sprite", 1.99)
        self.price = 1.99
        self.name = "Sprite"
        
class Coke(object):
    def __init__(self):
        self.name = ItemInfo("Coke", 1.50)
        self.price = 1.50
        self.name = "Coke"

class Cake(object):
    def __init__(self):
        self.name = ItemInfo("Cake", 2.99)
        self.price = 2.99
        self.name = "Cake"

class Value(Enum):
    PENNY = 1
    NICKLE = 5
    DIME = 10
    QUARTER = 25
    
    def get_value(self):
        return self.value
    
    def get_name(self):
        return self.name

class Coin(object):
    def __init__(self, value): # value --- Value(Enum)
        self.value = value.get_value()
        self.name = value.get_name()
        
class State:
    def __init__(self, vendingMachine):
        self.vm = vendingMachine

class No_Selection(State):
    def __init__(self, vendingMachine):
        State.__init__(self, vendingMachine)
        
    def selectItem(self, selection): # string
        info = self.vm.itemIdentifiers[selection]
        self.vm.change_to_has_selection()
        self.vm.set_selected_item(selection)
        return info
    
    def insertCoins(self, coins):
        print("Please make a selection first")
    
    def executeTransaction(self):
        print("Please make a selection first")
    
    def cancelTransaction(self):
        print("Please make a selection first")
        return 0
        
class Has_Selection(State):
    def __init__(self, vendingMachine):
        State.__init__(self, vendingMachine)
        
    def selectItem(self, selection): # string
        self.vm.set_selected_item(selection)
        
    def insertCoins(self, coins):
        self.vm.insert_coins(coins)
        self.vm.change_to_inserted_money()
        
    def executeTransaction(self):
        print("Please insert money first")
    
    def cancelTransaction(self):
        print("Transactions cancelled")
        self.vm.set_selected_item("null")
        self.vm.change_to_no_selection()
        return 0
    
class Inserted_Money(State):
    def __init__(self, vendingMachine):
        State.__init__(self, vendingMachine)
        
    def selectItem(self, selection): # string
        print("Has incomplete transaction")
    
    def insertCoins(self, coins):
        self.vm.insert_coins(coins)
    
    def executeTransaction(self):
        inserted_value = self.vm.get_inserted_money()
        price = self.vm.currentSelection.price
        diff = abs(inserted_value - price)
        if inserted_value < price:
            print("{} more money needed to pay", price - inserted_value)
        else:
            print("Executing transaction, will return you $" + str(diff) + " and " + self.vm.currentSelection.name + " item.")
            self.vm.set_selected_item("null")
            self.vm.coins.extend(self.vm.currentCoins)
            self.vm.change_to_no_selection()
            self.vm.empty_inserted_coins()
    
    def cancelTransaction(self):
        self.vm.set_selected_item("null")
        self.vm.change_to_no_selection()
        inserted_money = self.vm.get_inserted_money()
        self.vm.empty_inserted_coins()
        return inserted_money
        
class VendingMachine(object):
    def __init__(self):
        self.coins = [] # List<Coin> 
        self.items = [] # List<Items>
        self.itemIdentifiers = {} # Map<String, ItemInfo>
        self.currentSelection = None # ItemInfo
        self.currentCoins = []
        self.stock = collections.defaultdict(list) # Map<identifier, List<Item>>
        self.No_Selection = No_Selection(self)
        self.Has_Selection = Has_Selection(self)
        self.Inserted_Money = Inserted_Money(self)
        self.state = self.No_Selection
        
    def set_itemIdentifiers(self):
        self.itemIdentifiers["A1"] = Sprite()
        self.itemIdentifiers["B1"] = Coke()
        self.itemIdentifiers["C1"] = Cake()
        self.itemIdentifiers["null"] = None
    
    def set_state(self, state):
        self.state = state
    
    def set_selected_item(self, string):
        self.currentSelection = self.itemIdentifiers[string]
    
    def insert_coins(self, coins): # List<Coins>
        self.currentCoins.extend(coins)
    
    def get_inserted_money(self):
        return sum([x.value for x in self.currentCoins])
    
    def empty_inserted_coins(self):
        self.currentCoins = []
    
    def get_current_sale_price(self):
        if not currentSelection:
            print("Please make a selection first")
            return 0
        else:
            return self.currentSelection.price
    
    def refill_items(self, id_, num):
        if id_ == "A1": # Sprite
            for _ in range(num):
                self.stock["A1"].append(Sprite())
        elif id_ == "B1": # Coke  
            for _ in range(num):
                self.stock["B1"].append(Coke())
        elif id_ == "C1": # Cake:
            for _ in range(num):
                self.stock["C1"].append(Cake())
        return
    
    def change_to_no_selection(self):
        self.state = self.No_Selection
        
    def change_to_has_selection(self):
        self.state = self.Has_Selection
    
    def change_to_inserted_money(self):
        self.state = self.Inserted_Money
    
    def selectItem(self, selection): # string
        self.state.selectItem(selection)
    
    def insertCoins(self, coins):
        self.state.insertCoins(coins)
    
    def executeTransaction(self):
        self.state.executeTransaction()
    
    def cancelTransaction(self):
        self.state.cancelTransaction()
    
    
vm = VendingMachine()
vm.refill_items("A1", 6)
vm.set_itemIdentifiers()
vm.selectItem("A1")
vm.insertCoins([Coin(Value.PENNY), Coin(Value.PENNY)])
vm.executeTransaction()
