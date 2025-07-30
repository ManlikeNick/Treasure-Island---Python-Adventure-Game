print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input("You are lost in the Amazon forest You have reached a crossroad\n"
               "Which path will you take....Left or Right")
if choice == "left".lower():
    Swim_wait = input("You reach a river will you 'Swim or Wait'")
    if Swim_wait == "wait".lower():
        print("As you wait and look around you find out that there is a house \n"
              "Nearby and it has 3 doors Blue Red or Yellow\n"
              "Which door will open?")
        door = input("Blue or Red or Yellow ")
        if door == "blue".lower():
            print("Oh Oh You are eaten by beasts that eat human flesh...Game over")
        elif door == "Red".lower():
            print("Oh oh A flame of fire has engulfed you to ashes...Game Over")
        elif door == "yellow".lower():
            print("You win you have found the Treasure Island...You Win")
        else:
            print("Sorry wrong choice.....Game Over")
    else:
        print("You are attacked by Piranhas....Game over")
        exit()


else:
    print("You have fallen into a a ditch with spikes in them to welcome you \n"
          ".....Game Over")
    exit()
