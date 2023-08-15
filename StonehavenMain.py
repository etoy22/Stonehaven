from City import City

def main():
    # Start Up Sequence
    Stonehaven = City()
    start = True
    '''
    Starting the actual commands

    TO DO:
    Add functionality to updateSecurity (Make a scan for betrayers (add them to person enemies, remove them from secuirty))
    Do Internal Defences class
    Do External Defences class
    '''
    while(start):
        print("____________________________________________________________________")
        print("What do you want to do put the number of the command you want to do")
        print("With every command you will always be scanning")
        print("0. Update Details") # This option is one that will always occur regardless of the option chosen
        print("0. Change Security Level") # This option is one that will always occur regardless of the option chosen
        print("0. Internal Defences") # Attacking enemies in the city
        print("0. External Defences") # Attacking enemies outside the city
        print("1. Add new Enemy Type") # Adds new enemy type
        print("2. Remove Enemy Type") # Removes an enemy type
        print("3. Add new Enemy (Person)") # Adds new enemy type
        print("4. Remove Enemy (Person)") # Removes an enemy type
        print("5. Defences Interface") # Will bring you to the interface for the internal defences
        print("6. Movement") 
        print("7. Pair interface to Sending Stone") # Pair to a Sending Stone who has the magic enchantment
        print("8. Pair interface to Soulforged") # Pair to a Soulforged who has the magic enchantment
        print("10. Exit Program") # Exit as a ooc character. This option doesn't exist in game
        print("____________________________________________________________________")
        result = input("Give me the number: ")

        try:
            result = int(result)
        except Exception as error:
            print('Caught this error: ' + repr(error))


        '''
        Update Details
        '''
        if(result != 10):
            Stonehaven.alwaysOccuring()

        '''
        Option Given
        '''
        match result:
            case 1:
                Stonehaven.addTypes()
            case 2:
                Stonehaven.removeTypes()
            case 3:
                Stonehaven.addPerson()
            case 4:
                Stonehaven.removePerson()
            case 5:
                Stonehaven.defInter()
            case 6:
                Stonehaven.move()
            case 7:
                print("Paired to Sending Stone")
            case 8:
                print("Paired to Soulforged")
            case 10:
                start = False
            case _:
                print("Not a valid command")

if __name__ == '__main__':
    main() 