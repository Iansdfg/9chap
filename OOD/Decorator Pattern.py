"""
Work Flow:
    CoffeePack--- CoffeeMaker --- Coffee

Objects:
    CoffeePack
    CoffeeMaker
    Coffee

Use Case:
    Brew
    Add decor

"""
class CoffeePack:
    def __init__(self, milk_value, sugar_value):
        self.milk_value = milk_value
        self.sugar_value = sugar_value


class CoffeeMaker:
    def __init__(self):
        pass  

    def make_coffee(self, cofee_pack):
        coffee = Coffee(cofee_pack)
        milk_value = cofee_pack.milk_value
        sugar_value = cofee_pack.sugar_value
        for i in range(milk_value):
            coffee = Milk(coffee)
        for i in range(sugar_value):
            coffee = Sugar(coffee)
        return coffee


class Coffee:
    def __init__(self, cofee_pack):
        self.ingredients = ['plain coffee']
        self.cost = 2

    def get_ingredience(self):
        print('Ingredients for this coffee is', ', '.join(self.ingredients))
        return self.ingredients

    def get_cost(self):
        return self.get_cost


class Decore(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
    
    
class Milk(Decore):
    def __init__(self, coffee):
        self.ingredients = coffee.ingredients + ['milk']
        self.cost = coffee.cost + 0.5

    def get_ingredience(self):
        print('Ingredients for this coffee is', ', '.join(self.ingredients))
        return self.ingredients

    def get_cost(self):
        return self.cost


class Sugar(Decore):
    def __init__(self, coffee):
        self.ingredients = coffee.ingredients + ['sugar']
        self.cost = coffee.cost + 0.5

    def get_ingredience(self):
        print('Ingredients for this coffee is', ', '.join(self.ingredients))
        return self.ingredients

    def get_cost(self):
        return self.cost

    

pack = CoffeePack(2,3)
cf = CoffeeMaker()
coffee = cf.make_coffee(pack)
coffee.get_ingredience()
cost = coffee.get_cost()
print(cost)


