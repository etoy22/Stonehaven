from Illusion import Illusion 
class MirrorImage(Illusion):
    def __init__(self,dist=[0,0],ex=True,number=0):
        super().__init__(ex)
        self.distance = dist
        self.illusionNumber = number

    # The varraibles exist here to interact with the magic of the world 
    def moving(self,x=0, y=0, weatherCondition="Clear"):
        print("Moves with the illusion of the city and makes it will also use the weather conditions to accurately simulate")
        print("Illusion "+self.illusionNumber+" will move with the city")

    # The varraibles exist here to interact with the magic of the world 
    def hit(self,x=0, y=0, weatherCondition="Clear"):
        print("If illusion is hit it disappears")
        self.exists = False 
    
    def setDistance(self,dist=[0,0]):
        self.distance = dist
    
    def setExists(self,ex):
        super().setExists(ex)
        if (not(self.exists)):
            self.distance = [0,0]

    def __str__(self):
        result = "Illusion "+ self.illusionNumber + " is at X and Y of " + self.distance
        if (self.exists):
            result += " and currently exists"
        else:
            result += " and does not exists"
        return result
