#this class needs to inherit the attributes and behaviors of the Card class
# a minion object is a Card
#child class or derived class
from Card import Card 
class Minion(Card):
    #attribute cost and name, inherits them from parent class: Card
    def __init__(self, cost, name, damage, life):
        Card.__init__(self, cost, name)
        #assign perameters to the object
        self.damage = damage
        self.life = life

    def printMinionInfo(self):
        print('The card cost: ' + str(self.cost))
        print('The card name: ' + self.name)
        print('Damage: ' + str(self.damage))
        print('Life: ' + str(self.life))