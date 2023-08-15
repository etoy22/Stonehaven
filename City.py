from CityCommands.InternalDefence import InternalDefence
from CityCommands.ExternalDefence import ExternalDefence
from CityCommands.Scanner import Scan

'''
General Ranking of Security Level:
0 - Means that you have no security
1 - Means that you are a member of the administration
2 - Means you are a solder in the Army (Stonehaven) or the disciple in the Soulforged
3 - Means you are a Commander or higher in the Army (Stonehaven)
4 - Means you are the Leader (Stonehaven) or Head of the Army (Stonehaven) or a personal Disciple of Juliet (Soulforged)
5 - Juliet Mirlon
'''


class City():
    def __init__(self):
        self.scan = Scan()
        self.inDefence = InternalDefence()
        self.exDefence = ExternalDefence()

    '''
    Always occuring effects
    '''

    def alwaysOccuring(self):
        self.scanning()
        self.updateSecurity()
        self.attack()
        self.inDefence.onSpells()
        # Check if inDefence is in attack mode
        # Check if exDefence is in attack mode

    '''
    Update Secuirty Measures
    This code is basically making it so that when people die and they take on their new role their Authority is automatically updated
    So makes the new mayor have the right permission but also does the same in the middle of combat as long as they aren't killed by the person they are replacing
    '''

    def updateSecurity(self):
        print("Determining Chain of Command")
        print("Checking to see if anyone is dead")
        print("Updating security levels to match new structure after people have died")

    '''
    Going to Class Scanner
    '''

    def scanning(self):
        self.scan.scanning()
        if (self.scan.getInternalActivation()):
            self.inDefence.setFlip(True)
            self.inDefence.warning()
            self.inDefence.defence()
            self.exDefence.setGates(True)
        if (self.scan.getInternalActivation()):
            dist = input("Closest enemy within range given in feet: ")
            try:
                self.exDefence.warning(int(dist))
                self.exDefence.defence()
                if (int(dist) < 2000):
                    self.inDefence.setGates(True)
            except Exception as error:
                print('Caught this error: ' + repr(error))

    '''
    Command to add a new type of enemy to the list
    '''

    def addTypes(self):
        newType = input("Give me the new type of creature you want to add: ")
        securityLevel = input("Give me your security details: ")
        self.scan.addTypes(newType, securityLevel)

    def addPerson(self):
        newType = input("Who do you want to add: ")
        securityLevel = input("Give me your security details: ")
        self.scan.addPerson(newType, securityLevel)
    '''
    Command to add a remove a type of enemy to the list
    '''

    def removeTypes(self):
        newType = input(
            "Give me the new type of creature you want to remove: ")
        securityLevel = input("Give me your security details: ")
        self.scan.removeTypes(newType, securityLevel)

    def removePerson(self):
        newType = input("Who do you want to remove: ")
        securityLevel = input("Give me your security details: ")
        self.scan.removePerson(newType, securityLevel)
    '''
    Going to Defence Interface 
    '''

    def defInter(self):
        inter = True
        while (inter):
            print("____________________________________________________________________")
            print("Working with the Defence Interface")
            # Will only be allowed if there are no enemies within the  city
            print("1. Deactivate Internal Defences")
            # Will only be allowed if there are no enemies within the  city
            print("2. Deactivate Internal Defences")
            print("3. Emergency Affecting Inner Defences")
            print("4. Emergency Affecting Inner Defences")
            # Exit as a ooc character. This option doesn't exist in game
            print("10. Exit Defence Interface")
            print("____________________________________________________________________")
            result = input("Give me the number: ")

            try:
                result = int(result)
            except Exception as error:
                print('Caught this error: ' + repr(error))

            match result:
                case 1:
                    self.deactivateInternal()
                case 2:
                    self.deactivateExternal()
                case 3:
                    self.emergancy(self.inDefence)
                case 4:
                    self.emergancy(self.exDefence)
                case 10:
                    inter = False
                case _:
                    print("Invalid response")

    '''
    Both in and out defence
    '''

    def emergancy(self, defence):
        securityLevel = input("Give me your security details: ")
        try:
            if (int(securityLevel) < 5):
                print("You don't have permission to use this feature")
            else:
                result = input("You want it on or off (0 for on 1 for off)")
                defence.setFlip(bool(result))
        except Exception as error:
            print('Caught this error: ' + repr(error))

    def attack(self):
        self.attackInternal()
        self.attackExternal()

    '''
    Here is the Internal Defences
    '''

    def deactivateInternal(self):
        securityLevel = input("Give me your security details: ")
        try:
            if (int(securityLevel) >= 3):
                if (not (self.scan.getInnerActive()) and self.scan.getInternalActivation()):
                    self.scan.setInternalActivation(False)
                    self.inDefence.deactivate()

                    # Add a way to unlock the gates
            else:
                print("Security Level not High Enough")
        except Exception as error:
            print('Caught this error: ' + repr(error))

    def attackInternal(self):
        if (self.scan.getInnerActive()):
            self.inDefence.attack()

    '''
    Here is the External Defences
    '''

    def deactivateExternal(self):
        securityLevel = input("Give me your security details: ")
        try:
            if (int(securityLevel) >= 3):
                if (not (self.scan.getOuterActive()) and self.scan.getExternalActivation()):
                    self.scan.setExternalActivation(False)
                    self.exDefence.deactivate()

                    # Add a way to unlock the gates
            else:
                print("Security Level not High Enough")
        except Exception as error:
            print('Caught this error: ' + repr(error))

    def attackExternal(self):
        if (self.scan.getOuterActive()):
            self.inDefence.attack()

    '''
    Going to Secret
    '''

    def move(self):
        print("SECRET STAGE 1")
