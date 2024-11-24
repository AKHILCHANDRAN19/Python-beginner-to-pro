#triangle star pattern

number = int(input("Enter the number of rows: "))
star = "*"
for i in range(1, number + 1):
  print(f"{i * star}")


#pyramid star pattern

number = int(input("Enter the number of rows: "))
star = "*"
for i in range(1, number + 1):
    spaces = " " * (number - i)  # Spaces to center the stars
    stars = star * (2 * i - 1)   # Stars for the current row
    print(f"{spaces}{stars}")
