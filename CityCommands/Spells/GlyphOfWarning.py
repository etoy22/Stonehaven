'''
Recieve name and level of spell that is being cast because its being cast from Glyph of Warning minimum level is always 3
'''
def casting(name,level):
    print("Casting the spell " + name + " at level " + min(3,level))