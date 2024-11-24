number = int(input("Enter a number: "))

for i in range(number, 0, -1):
    print(i, end=" ")

#Or

number = int(input("Enter your input number : "))
for i in range(1, number + 1):
  num = number - i
  print(f"{num}")
