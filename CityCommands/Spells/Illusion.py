class Illusion():
    def __init__(self,ex=True):
        self.exists = ex
    
    def getExists(self):
        return self.exists
    
    def setExists(self,ex):
        self.exists = ex