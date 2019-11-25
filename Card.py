#card class is a blueprint of the card object
#parent class or base class
class Card:
    #initializer to create the attributes of every class object (constructor)
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name
        #attributes- describes the object- argument or parameter
        #give the card a cost attribute
        #give the card a name attribute

    def printCardInfo(self):
        print('The card cost: ' + str(self.cost))
        print('The card name: ' + self.name)
        




#behaviors(methods or functions)