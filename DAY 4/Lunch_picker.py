import random
place_for_lunch = input("Enter the names of the restaurants separated by a comma: ").split(",")
list_items = len(place_for_lunch)
random_choice = random.randint(0, list_items - 1)
desired_place = place_for_lunch[random_choice]
print(f"The chosen place for lunch is: {desired_place}")
