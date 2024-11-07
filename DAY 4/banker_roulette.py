import random
#importing the random module
name_of_persons = input("Give me everybody's name separated by a comma. ")
#taking input from the user separated by coma
list_of_pepoles = name_of_persons.split(", ")
#converting the input into list
number_of_items = len(list_of_pepoles)
#calculating number of entries in the list
random_choice = random.randint(0, number_of_items - 1)
#taking a random number according to the number of inputs
desired_person = list_of_pepoles[random_choice]
#placing the randomily generated number and calling the corresponding entry in the list
print(f"{desired_person} is going to pay the bill")
