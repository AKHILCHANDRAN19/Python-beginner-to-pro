number = float(input("Write your input number\n"))
if number < 0:
	print("The provided number is a negative number")
elif number == 0:
    print('The provided number is zero')
else:
	print("The provided number is a positive number")



#OR


num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print(f"{num} is zero.")

