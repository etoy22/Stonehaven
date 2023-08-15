import GlyphOfWarning as GOF
class Scan():
    

    '''
    Init the class
    '''
    def __init__(self):
        self.people = [""]
        self.types = ["Malachi"]
        self.internalActivation = False
        self.externalActivation = False
        self.innerActive = False
        self.outActive = False
        self.security = {"Juliet":5,"Mayor":4,"Chief":4,"Civilian":0} #Example of how it would be


    '''
    This exists because i think its funny
    '''
    def notHigh(self):
        print("Security Level not High Enough")


    '''
    Add and Remove Types of Creatures with the proper security level
    '''
    def addTypes(self,newType,securityLevel):
        if(securityLevel >= 4):
            if(newType == "Soulforged" and securityLevel == 4):
                print("Security Compromised Activating Security Sequence")
                GOF.casting("Fireball", 3)
            else:
                self.types.add(newType)
                print("Successfully added: " + newType)

        else:
            self.notHigh()

    def addPerson(self,person,securityLevel):
        if(securityLevel >= 3):
            if(self.security[person] < securityLevel):
                print("You don't have permission to do this action")
            else:
                self.people.add(person)
                print("Successfully added: " + person)

        else:
            self.notHigh()
        
    def removeTypes(self,removeType,securityLevel):
        if(securityLevel >= 4):
            if (removeType == "Malachi" and securityLevel == 4):
                print("Security Compromised Activating Security Sequence")
                GOF.casting("Fireball", 3)
            else:
                self.types.remove(removeType)
                print("Successfully removed: " + removeType)

        else:
             self.notHigh()

    def removePerson(self,person,securityLevel):
        if(securityLevel >= 4):
            self.people.remove(person)
            print("Successfully removed: " + person)

        else:
            self.notHigh()



    '''
    Scan commands
    '''
    def scanHelper(self,array):
        count = 0
        for creatures in array:
            if (count+1 < len(array)):
                print(creatures, end = ", ")
            else:
                print(creatures)
            count += 1

    def scanning(self):
        print("Scanning for the following creatures:")
        self.scanHelper(self.types)



        print("Scanning for the following people:")
        self.scanHelper(self.people)

        
        print("Scanning inside the city.")
        # Out of Character to determind if the scanning types were found inside the city
        foundInside = input("Tell me if the scanning types were found in the city (0 for False, 1 for True): ")

        # Find out from David max distance outside the city 
        print("Scanning outside the city to a max distance of 1 Mile.")
        # Out of Character to determind if the scanning types were found outside the city
        foundOutside = input("Tell me if the scanning types were found outside the city (0 for False, 1 for True): ")


        '''
        Basically only turns on the defences if they haven't already been turned on
        '''
        try:
            if(int (foundInside) and not(self.internalActivation)):
                print("Activating Internal Defences")
                self.internalActivation = True
                self.innerActive = True
            elif (not(int(foundInside))): #This says if they are not within the base
                print("No longer within range you may choose to deactivate defences")
                self.innerActive = False
        except Exception as error:
            print('Caught this error: ' + repr(error))

        try:
            if(int (foundOutside) and not(self.externalActivation)): # Just means that the 
                print("Activating External Defences")
                self.internalActivation = True
                self.outActive = True
            elif (not(int(foundOutside))): #This says if they are not in the 1 mile radius
                print("No longer within range you may choose to deactivate defences")
                self.outActive = False
        except Exception as error:
            print('Caught this error: ' + repr(error))

    '''
    Getters
    '''
    def getTypes(self):
        return self.types
    
    def getInternalActivation(self):
        return self.internalActivation
    
    def getExternalActivation(self):
        return self.externalActivation

    def getInnerActive(self):
        return self.innerActive
    
    def getOuterActive(self):
        return self.outActive
    
    '''
    Setter
    '''

    def setInternalActivation(self,active):
        self.internalActivation = active
    
    def setExternalActivation(self,active):
        self.internalActivation = active