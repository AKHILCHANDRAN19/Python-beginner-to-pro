import random

wrong_words = ["ogd", "atc", "nta", "ioln"]
random_choice = random.randint(0, 3)
list_picker = wrong_words[random_choice]
print(f"UNSCRAMBLE THE WORD : {list_picker}")
guess = input("Your guess : ").lower()
if (random_choice == 0 and guess == "dog") or (random_choice == 1 and guess == "cat") or (random_choice == 2 and guess == "ant") or (random_choice == 3 and guess == "liom"):
  print("congrats you guessed it right")
else:
  print("sorry you guessed it wrong")
