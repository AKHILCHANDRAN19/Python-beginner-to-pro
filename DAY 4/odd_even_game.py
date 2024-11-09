import random

computer_number = random.randint(1,100)
input_number = int(input("Enter your number : "))
input_guess = input("Enter your guess odd/even : ").lower()
total_sum = computer_number + input_number
if (total_sum % 2 == 0 and input_guess == "even") or (total_sum % 2 == 1 and input_guess == "odd"):
  print("You guessed it right")
elif (total_sum % 2 == 0 and input_guess == "odd") or (total_sum % 2 == 1 and input_guess == "even"):
  print("You guessed it wrong")
else:
  print("something wrong with your input!")
  exit()
print(f"computer choosed : {computer_number}")
print(f"You choosed : {input_number}")
print(f"The total sum is : {total_sum}")
