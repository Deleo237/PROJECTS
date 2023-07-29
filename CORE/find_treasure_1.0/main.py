print("WELCOME TO MY GITHUB 'find treasure 1.0' PROJECT.\n")
print("Welcome to Treasure Island BY DELEO.\n\n\nYour mission is to find the treasure.")
ch1=input('You are at a cross road. Where do you want to go? Type "left" or "right"\n')
ch1=ch1.lower()
if ch1=="left":
    print("TURNED LEFT AND WALKING")
    ch2=input(('You come to a lake.The is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'))
    ch2=ch2.lower()
    if ch2=="wait":
        print("WAITING FOR BOAT")
        print("The boat arrived. You are on the boat. The boat arrived the island and you are unharmed.")
        ch3=input("The is a house with 3 doors. One red, One green, and One black. Which colour do you choose?\n")
        ch3=ch3.lower()
        if ch3=="black":
            print("OPEN BLACK DOOR")
            print("@@@@@@@@@@@@@@@@@@CONGRATULATION@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@YOU FOUND THE TREASURE@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@YOU ARE NOW RICH@@@@@@@@@@@@@@@@@@")
        elif ch3=="red":
            print("OPEN RED DOOR")
            print(".You have been consumed by fire.")
            print("*************GAME OVER*************")
        elif ch3=="green":
            print("OPEN GREEN DOOR")
            print(".You have been devoured by vines")
            print("*************GAME OVER*************")
        else:
            print(".Wrong input.")
            print("*************GAME OVER*************")
    elif ch2=="swim":
        print("SWIMMING")
        print(".You have been swallowed by a big fish.")
        print("*************GAME OVER*************")
    else:
        print(".Wrong input.")
        print("*************GAME OVER*************")
elif ch1=="right":
    print("TURNED RIGHT AND WALKING")
    print(".You have been eaten by a lion.")
    print("*************GAME OVER*************")
else:
    print(".Wrong input.")
    print("*************GAME OVER*************")
