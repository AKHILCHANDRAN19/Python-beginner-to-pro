import random
random_activity = input("Enter activities separated by a comma: ").split(",")
list_items =len(random_activity)
random_choice = random.randint(0, list_items - 1)
desired_activity = random_activity[random_choice]
print(f"Today's chosen activity is: {desired_activity}")
