import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("WELCOME TO THE PASSWORD GENERATOR!")
ip_letters = int(input("How many letters would you like in your password?\n"))
ip_symbols = int(input("How many symbols would you like in your password?\n"))
ip_numbers = int(input("How many numbers would you like in your password?\n"))
op_letters = random.choices(letters, k = ip_letters)
op_symbols = random.choices(symbols, k = ip_symbols)
op_numbers = random.choices(numbers, k = ip_numbers)
#converting the integers list to string list
str_numbers = list(map(str, op_numbers))
op_result = op_letters + str_numbers + op_symbols
#changing the place of each item in a list by using random module and shuffle function
random.shuffle(op_result)
#converting a list item to combined item look a like combination of letters numbers and string eg: a1#2fgh@90jk
result = ''.join(op_result)
print(f"Your Generated password is : {result}")
