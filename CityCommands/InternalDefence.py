import Spells.GlyphOfWarning as GOF

from Defence import Defence


class InternalDefence(Defence):
    def __init__(self):
        super().__init__()


    '''
    Attacking Enemies
    '''
    def attack(self):
        # Ongoing spell effects 
        self.ongoingInner()
        # Non ongoing spell effects

    def setFlip(self, value):
        super().setFlip(value)
        if (self.flip):
            self.lockTheGates()

    '''
    Their is a magic mouth in the city letting people know that the enemies within the city
    '''
    def warning(self):
        super().warning()
        print("Everyone get to a safe place their are enemies within the city")

    def deactivate(self):
        super().deactivate()
        self.setFlip(False)
        # Maybe dispel temporary spells?

    '''
    Informs Defenders
    '''

    '''
    Spells that are always on going or at least cast once a day for the permanent effect
    '''

    def onSpells(self):
        print("Forbidance")
        print("Guards and Wards [To become immune to the effect one needs to gain a secuirty level (Recast everyday so if you lose security you no longer gain the benifit)]")
        print("Guards and Wards has 2 stinking clouds every 50 feet square")

    '''
    Here is the activation of the inner defences
    '''

    def onInner(self):
        self.flip = True

    '''
    Here is the activation of the inner defences
    '''

    def ongoingInner(self):
        if(not(self.startingAttack)):
            # The first time attacking has started
            self.startingAttack = True