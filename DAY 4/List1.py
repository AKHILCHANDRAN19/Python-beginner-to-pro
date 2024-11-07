#Indian states and calling data from a particular position

states_of_india = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Karnataka", "Uttar Pradesh"]
print(states_of_india[0])
print(states_of_india[-1])
print(states_of_india[1])
print(states_of_india[-2])

#replacing a listed item by changing it's spelling

states_of_india = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Karnataka", "Uttar Pradesh"]
states_of_india[0] = "Anthra Pradesh"
print(states_of_india)

#adding a data at the end of the list Append function

states_of_india = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Karnataka", "Uttar Pradesh"]
states_of_india.append("kerala")
print(states_of_india)

#adding a new list to the existing list using extend function

states_of_india = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Karnataka", "Uttar Pradesh"]
states_of_india.extend(["kerala", "Tamil Nadu"])
print(states_of_india)

#more functions is here 👇👇
#docs.python.org/3/tutorial/datastructures.html
