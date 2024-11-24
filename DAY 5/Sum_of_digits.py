number = int(input("Enter your number: "))
sum_digits = 0

# Convert the number to a string to loop through each digit
for i in str(number):
    sum_digits += int(i)  # Convert each character back to an integer and add it to sum_digits

print(f"The sum of the digits is: {sum_digits}")
