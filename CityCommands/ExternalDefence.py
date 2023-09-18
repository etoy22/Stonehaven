import Spells.GlyphOfWarning as GOF
from Defence import Defence
from Spells.MirrorImage import MirrorImage
from Spells.CloudImage import CloudImage


class ExternalDefence (Defence):
    def __init__(self):
        self.mirror = [MirrorImage(ex=False,number=1),MirrorImage(ex=False,number=2),MirrorImage(ex=False,number=3)]
        self.cloud = CloudImage(False)
        super().__init__()

    def mirrorImageOn(self):
        distance = []
        try:
            for i in range (3):
                getX = input("Get X value for " + i +" Illusion: ")
                getY = input("Get Y value for " + i +" Illusion: ")
                distance.append([getX,getY])
        except Exception as error:
            print('Caught this error: ' + repr(error))
        for i in range (len(self.mirror)):
            self.mirror[i].setDistance(distance[i])
            self.mirror[i].setExists(True)

    def mirrorHit(self):
        toHit = []
        for i in range(3):
            if(self.mirror[i].getExists()):
                print("Mirror Image " + (i+1) + " can be hit")
                toHit.append(i+1)
        result = input("Which mirror was hit")
        try:
            if(int(result) in toHit):
                self.mirror[int(result)-1].hit()
        except Exception as error:
            print('Caught this error: ' + repr(error))

    def mirrorDesc(self):
        # Create an illusion that only is visible one way
        print(self.mirror[0])

    def cloudDesc(self):
        print(self.cloud)

    def exActivation(self):
        illInter = True
        while (illInter):
            print("____________________________________________________________________")
            print("Working with the Active Defence Interface")
            print("1. Activate Mirror Image")
            # Ooc to show that a Mirror Image was hit
            print("2. Mirror Image Hit")
            print("3. Description of Mirror Image")
            print("4. Description of Vision Blocking Image")
            print("5. Earthbind rune")
            print("10. Exit Defence Interface")
            print("____________________________________________________________________")
            result = input("Give me the number: ")

            try:
                result = int(result)
            except Exception as error:
                print('Caught this error: ' + repr(error))

            match result:
                case 1:
                    self.mirrorImageOn()
                case 2:
                    self.mirrorHit()
                case 3:
                    self.mirrorDesc()
                case 4:
                    self.cloudDesc()
                case 5:
                    self.earthbind()
                case 10:
                    illInter = False
                case _:
                    print("Invalid response")

    def warning(self,dist = 5300):
        '''
        Their is a magic mouth in the city letting people know that the malachi are within range of weapons of the city these would be both at the city gates and the city walls
        '''
        if (dist <= 2000):
            super().warning()
            print("Magic Mouth: Alert the enemy is coming even closer the gates will start to close")
            self.lockTheGates()
            self.setFlip(True)
        elif (dist <= 2500):
            super().warning()
            print("Magic Mouth: Alert the enemy is coming even closer should they come closer the gates will start to close")
        elif (dist <= 3600):
            super().warning()
            print("Magic Mouth: Alert the enemy is coming closer everyone should start making there way into the city")
        elif(dist <= 5280):
            super().warning()
            print("Magic Mouth: Alert there is an enemy on the within 1 mile of the city")

    def ongoingOuter(self):
        if(not(self.startingAttack)):
            # The first time attacking has started
            self.startingAttack = True
            self.cloud.setExists(True)

        print("Ongoing Attack Spells")


    def turnOffDefences(self):
        self.cloud.setExists(False)


    def earthbind(self):
        GOF.casting("Earth Bind",2)