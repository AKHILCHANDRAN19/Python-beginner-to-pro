student_height = input("Enter the students height separated by space : ").split()
sum_height = 0
for height in student_height:
  sum_height = sum_height + float(height)
#print(sum_height)
number_of_items = 0
for items in student_height:
  number_of_items = number_of_items + 1
#print(number_of_items)
average_height = sum_height / number_of_items
rounded_value = round(average_height, 2)
print(f"The average height of {number_of_items} student is : {rounded_value}")
