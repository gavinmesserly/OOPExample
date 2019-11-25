from Card import Card
from Minion import Minion

def main():
    #create town crier card
    #cost = 1 and name = town crier
    #instantiate an object called townCrier, creating and instance of the class
    townCrier = Minion(1, 'Town Crier', 1, 2)
    
    #create an instance of the class called redbandWasp
    #attributes where the cost is = 2 and name is = Redband Wasp
    redbandWasp = Minion(2, 'Redband Wasp', 1, 3)
    warPath = Card(2, 'Warpath')

    townCrier.printCardInfo()
    townCrier.printMinionInfo()

    redbandWasp.printCardInfo()
    warPath.printCardInfo()
    
    #show the player the details of the card
    
    
    
if __name__ == '__main__':
    main()