class Defence():
    def __init__(self):
        self.flip = False
        self.gates = False
        self.startingAttack = False

    def defence(self):
        print("Defence")

    def deactivate(self):
        print("Deactivation Commencing")

    def warning(self):
        print("Magic Mouth Condition Unlocks")

    def lockTheGates(self):
        if (not (self.gates)):
            self.warning()
            print("Magic Mouth: Gates are closing in: ")
            for i in range(30, 0, -1):
                if (i == 0):
                    print(i)
                else:
                    print(i+",", end=" ")
            print("Gates immediatly close")
            print("This occurs on every gate going")
            self.setGates(True)

    '''
    Sends a message to all the constructs within Stonehaven its time to act in defence of Stonehaven
    '''

    def sendMessageToDefenders(self):
        print("Updates current situation to Constructs")
        print("Sends message to those who are paired via Sending Stone")
        print("Sends message to all paired Soulforged")
   
    '''
    Setters
    '''

    def setFlip(self, value):
        self.flip = value

    def setGates(self, value):
        self.gates = value
