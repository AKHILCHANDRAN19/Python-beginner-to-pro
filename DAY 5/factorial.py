#My version

number = int(input("Enter a number : "))
input = number
for i in range(1, number):
  number = number * i
print(f"The factorial of the number {input} is {number}")


#correct version

number = int(input("Enter a number : "))
factorial = 1

# Loop to multiply numbers from 1 to number
for i in range(1, number + 1):
    factorial *= i  # Same as: factorial = factorial * i

print(f"The factorial of the number {number} is {factorial}")
