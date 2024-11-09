import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
selected_option = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors."))
if selected_option == 0:
    print(f"you choose : {rock}")
elif selected_option == 1:
    print(f"you choose : {paper}")
elif selected_option == 2:
    print(f"you choose : {Scissors}")
else:
    print("you choose a wrong option")
    exit()
#converting them into list
options =[rock, paper, Scissors]
list_items = len(options)
random_choice = random.randint(0, list_items - 1)
computer_choice = options[random_choice]
print(f"computer choice : {computer_choice}")
#result logic implementetion
if selected_option == 0 and random_choice == 0:
    print("game draw")
elif selected_option == 0 and random_choice == 1:
    print("You lose")
elif selected_option == 0 and random_choice == 2:
    print("You win")
if selected_option == 2 and random_choice == 2:
    print("Game draw")
elif selected_option == 2 and random_choice == 0:
    print("You lose")
elif selected_option == 2 and random_choice == 1:
    print("You lose")
if selected_option == 1 and random_choice == 1:
    print("Game draw")
elif selected_option == 1 and random_choice == 0:
    print("You lose")
elif selected_option == 1 and random_choice == 2:
    print("You win")
