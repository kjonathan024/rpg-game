#build out character classes ******ALSO ADD AN EVASION ATTRIBUTE TO ALL PLAYER CLASSES*******
import math
import random

class Player:
    #constructor
    def __init__(self, name="Player", level=0, hp=0, speed=0):
        self.name = name
        self.level = level
        self.hp = hp
        self.speed = speed

    #getting and setting attributes
    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getLevel(self):
        return self.level

    def setLevel(self, newLevel):
        self.level = newLevel

    def getHP(self):
        return self.hp

    def setHP(self, newHP):
        self.hp = newHP

    def getSpeed(self):
        return self.speed

    def setSpeed(self, newSpeed):
        self.speed = newSpeed

    def takeDamage(self, damageTaken):
        self.setHP(self.getHP() - damageTaken)

    #miscellaneous methods
    def backstory():
        print("In a long, far away era, your people ruled the Earth with a gracious but firm hand. You fought off the orcs, but they're coming back...")
        print()

    def BroadcastDamageDealt(self, damage):    
        print(self.name + " dealt " + str(damage) + " damage!")

    #attack methods (ADD A MISS PROBABILITY)
    def singleAttack(self):
        damage = 0
        print(self.name + " attacked!")
        if random.random() > 0.7:
            damage += math.trunc(random.randrange(15,31) * 1.2)
            print("You dealt a critical hit!")
            print()
        
        else:
            damage += random.randrange(15,31)
        self.BroadcastDamageDealt(damage)
        return damage
            
    def multiAttack(self):
        damage = 0
        print(self.name + " attacked 3 times!")
        for i in range(3): 
            if random.random() > 0.8:
                damage += math.trunc(random.randrange(15,31) * 1.2)
                print("You dealt a critical hit!")
                print()
            else:
                damage += random.randrange(15,31)
        self.BroadcastDamageDealt(damage)        
        return damage            
               
class Mage(Player):
    #constructor
    def __init__(self, name = "Player", level = 5, hp = 70, speed = 30):
        super().__init__(name, level, hp, speed)

    #miscellaneous methods
    def backstory(self):
        print("In a long, far away era, the mages ruled the Earth with a gracious but firm hand.\nYou fought off the orcs, but they're coming back...")
        print()

    #attack methods
    def singleAttack(self):
        damage = 0
        print(self.name + " summoned a magic attack!")
        if random.random() > 0.75:
            damage += math.trunc(random.randrange(20,41) * 1.2)
            print("You dealt a critical hit!")
            print()

        else:
            damage += random.randrange(15,31)
        self.BroadcastDamageDealt(damage)    
        return damage
            
    def multiAttack(self):
        damage = 0
        print(self.name + " created wind sprites that attacked 3 times!")
        for i in range(3): 
            if random.random() > 0.95:
                damage += math.trunc(random.randrange(15,31) * 1.2)
                print("You dealt a critical hit!")
                print()
            else:
                damage += random.randrange(15,31)
        self.BroadcastDamageDealt(damage)        
        return damage    

class Warrior(Player):
    #constructor
    def __init__(self, name = "Player", level = 5, hp = 80, speed = 20):
        super().__init__(name, level, hp, speed)    

    #miscellaneous methods
    def backstory(self):
        print("In a long, far away era, the warriors ruled the Earth with a protective but firm hand.\nYou fought off the orcs, but they're coming back...")
        print()

    #attack methods
    def singleAttack(self):
        damage = 0
        print(self.name + " slashed their sword!")
        if random.random() > 0.75:
            damage += math.trunc(random.randrange(20,41) * 1.2)
            print("You dealt a critical hit!")
            print()
        
        else:
            damage += random.randrange(15,31)
        self.BroadcastDamageDealt(damage)    
        return damage
            
    def multiAttack(self):
        damage = 0
        print(self.name + " striked 3 times!")
        for i in range(3): 
            if random.random() > 0.95:
                damage += math.trunc(random.randrange(15,31) * 1.2)
                print("You dealt a critical hit!")
                print()
            else:
                damage += random.randrange(15,31)
        self.BroadcastDamageDealt(damage)        
        return damage

class Assassin(Player):
    #constructor
    def __init__(self, name = "Player", level = 5, hp = 60, speed = 45):
        super().__init__(name, level, hp, speed)

    #miscellaneous methods    
    def backstory(self):
        print("In a long, far away era, the assassins lurked in the shadows...\nYour people trained for the orcs to return when no one else thought they would...\nand now that they've returned, the world needs your help.")    
        print()

    #attack methods
    def singleAttack(self):
        damage = 0
        print(self.name + " slashed!")
        if random.random() > 0.75:
            damage += math.trunc(random.randrange(20,41) * 1.2)
            print("You dealt a critical hit!")
            print()
        
        else:
            damage += random.randrange(15,31)
        self.BroadcastDamageDealt(damage)    
        return damage
            
    def multiAttack(self):
        damage = 0
        print(self.name + " swiped quickly 3 times!")
        for i in range(3): 
            if random.random() > 0.5:
                damage += math.trunc(random.randrange(15,31) * 1.2)
                print("You dealt a critical hit!")
                print()
            else:
                damage += random.randrange(15,31)
        self.BroadcastDamageDealt(damage)        
        return damage

#build an NPC

#build out enemy / boss classes

class BasicOrc():
    #default constructor method
    def __init__(self, name = "Small Orc", level = 5, hp = 100, speed = 15):
        self.name = name
        self.level = level
        self.hp = hp
        self.speed = speed

    #set and get attribute methods
    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getLevel(self):
        return self.level

    def setLevel(self, newLevel):
        self.level = newLevel

    def getHP(self):
        return self.hp

    def setHP(self, newHP):
        self.hp = newHP

    def getSpeed(self):
        return self.speed

    def setSpeed(self, newSpeed):
        self.speed = newSpeed

    #miscellaneous methods
    def BroadcastDamageDealt(self, damage):    
        print(self.name + " dealt " + str(damage) + " damage!")

    def takeDamage(self, damageTaken):
        self.setHP(self.getHP() - damageTaken)

    #attack method
    def singleAttack(self):
        damage = 0
        print(self.name + " attacked!")
        if random.random() > 0.90:
            damage += math.trunc(random.randrange(10,18) * 1.2)
            print(self.name + " dealt a critical hit!")
        
        else:
            damage += random.randrange(5,18)

        self.BroadcastDamageDealt(damage)
        return damage


#add in battle elements (maybe a miss function?)
def dealDamage(damage, target):
    if target.getHP() - damage > 0:
       target.setHP(target.getHP() - damage)
    else:
        target.setHP(0)

def checkBattleStatus(player, enemy):
        if not player.getHP() > 0:
            return "loser"
            
        elif not enemy.getHP() > 0:
            return "winner"

        else:
            return

def displayHP(player, enemy):
    print(player.getName() + " has " + str(player.getHP()) + " HP.")
    print()
    print(enemy.getName() + " has " + str(enemy.getHP()) + " HP.")
    print()

def attackOrder(player, enemy):
    if player.getSpeed() > enemy.getSpeed():
        return [player, enemy]
    else:
        return [enemy, player]

#note: gotta fix battle ending early if the HP lowers mid round *check battleOutcome()*            
def battleOutcome(outcome, player, enemy):
    if outcome == "winner":
        print(player.getName() + " has defeated " + enemy.getName() + "!")
        return True
    elif outcome == "loser":
        print(enemy.getName() + " has defeated " + player.getName() + ". " + player.getName() + " blacked out...")
        return True
    else:
        return False

#clean up
def battle(player, enemy):
    print("A wild " + enemy.getName() + " appeared!")
    print()
    while player.getHP() > 0 and enemy.getHP() > 0:
        #refresh attack choice
        currentRoundAttack = ""
        currentRoundOrder = None
        #display HP levels of both
        displayHP(player, enemy)

        #determine who hits first
        currentRoundOrder = attackOrder(player, enemy)
        #print(currentRoundOrder)
        #attacks until everyone's turn is over
        try:
            while currentRoundOrder is not None:
                #checking if it's the player's turn to attacks
                if currentRoundOrder[0] == player:

                    print("It's your turn!")

                    #determine player's attack type
                    currentRoundAttack = input("Would you like to single attack (1), or multi attack (2): ")

                    if currentRoundAttack == "1":
                        x = currentRoundOrder[0].singleAttack()
                        dealDamage(x, enemy)
                        del currentRoundOrder[0]
                        displayHP(player, enemy)
                        if battleOutcome(checkBattleStatus(player, enemy), player, enemy):
                            break

                    elif currentRoundAttack == "2":
                        x = currentRoundOrder[0].multiAttack()
                        dealDamage(x, enemy)
                        del currentRoundOrder[0]
                        displayHP(player, enemy)
                        if battleOutcome(checkBattleStatus(player, enemy), player, enemy):
                            break
                    else:
                        print("It seems you didn't choose a valid option.")
                        print()
                else:
                    x = currentRoundOrder[0].singleAttack()
                    dealDamage(x, player)
                    del currentRoundOrder[0]
                    displayHP(player, enemy)
                    if battleOutcome(checkBattleStatus(player, enemy), player, enemy):
                        break
        except IndexError:
            continue

            


#add the actual game elements, rounds, turns, etc
gameState = True
AllPlayerTypes = ["mage", "warrior", "assassin"]
while gameState:
    #setting up the player object
    playerType = input("Hello there! What player type would you like to be? \nMage, Warrior, or Assassin? ")
    playerType = playerType.lower()
    while playerType not in AllPlayerTypes:
        playerType = input("It seems you didn't choose one of the three player types. What player type would you like to be? \nMage, Warrior, or Assassin? ")
        playerType = playerType.lower()
    playerName = input("And your " + playerType + "'s name? ")

    if playerType == AllPlayerTypes[0]:
        playableCharacter = Mage(playerName)
        playableCharacter.backstory()

    elif playerType == AllPlayerTypes[1]:
        playableCharacter = Warrior(playerName)
        playableCharacter.backstory()

    elif playerType == AllPlayerTypes[2]:
        playableCharacter = Assassin(playerName)
        playableCharacter.backstory()

    inTheTown = True
    while inTheTown:
        TownActions = ["shop", "explore", "leave"]
        print()
        nextAction = input("Another gorgeous day in the village! What would you like to do?\nShop, Explore, or Leave? ")
        nextAction = nextAction.lower()
        while nextAction not in TownActions:
            nextAction = input("It seems you didn't choose one of the three options. What would you like to do?\nShop, Explore, or Leave? ")
            nextAction = nextAction.lower()
            print()
        if nextAction == TownActions[0]:
            print("You decided to visit the shop...")
            print("You walk inside the shop, but when the shopkeeper sees you lack any gold, he chases you out of the store...")
            continue
        elif nextAction == TownActions[1]:
            print("You decided to explore the town...")
            print("No one seems to want to talk to you...")
            continue
        elif nextAction == TownActions[2]:
            print("You decided to leave the village...")
            print()
            startingEnemy = BasicOrc()
            inTheTown = False

    battle(playableCharacter, startingEnemy)

    break
