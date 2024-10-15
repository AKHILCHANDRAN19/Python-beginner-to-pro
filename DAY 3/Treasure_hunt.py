print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

# Start the adventure
choice = input("Do you want to start your adventure? (yes/no): ").lower()

if choice == 'yes':
    # Choose a path
    print("\nYou are at a crossroad. You can go left or right.")
    path = input("Which path will you take? (left/right): ").lower()

    if path == 'left':
        # Encounter a river
        print("\nYou arrived at a river. It's deep and wide.")
        print("Do you want to swim across or wait for a boat?")
        river_choice = input("Type 'swim' to swim or 'wait' for the boat: ").lower()

        if river_choice == 'swim':
            print("You swam across but were attacked by a crocodile. Game over!")
        elif river_choice == 'wait':
            print("You waited and found a boat. You safely crossed the river!")
            # Find treasure
            print("\nCongratulations! You've reached the treasure area!")
            print("You see a treasure chest. Do you want to open it?")
            treasure_choice = input("Type 'open' to open the chest or 'leave' to leave it: ").lower()

            if treasure_choice == 'open':
                print("You opened the chest and found gold and jewels! You win!")
            elif treasure_choice == 'leave':
                print("You left the treasure behind. Game over!")
            else:
                print("Invalid choice. Please choose 'open' or 'leave'.")
        else:
            print("Invalid choice. Please choose 'swim' or 'wait'.")

    elif path == 'right':
        # Encounter a cave
        print("\nYou entered a dark cave.")
        print("You can search the cave or exit.")
        cave_choice = input("Type 'search' to look for treasure or 'exit' to leave: ").lower()

        if cave_choice == 'search':
            print("You found a hidden treasure chest! You win!")
        elif cave_choice == 'exit':
            print("You exited the cave safely but without treasure. Game over!")
        else:
            print("Invalid choice. Please choose 'search' or 'exit'.")
    else:
        print("Invalid choice. Please choose left or right.")
else:
    print("Thank you for visiting. Goodbye!")
