number = input("write down your number ")
first_digit = number[0]
second_digit = number[1]
total = int(first_digit) + int(second_digit)
print(total)


#OR

number = input("write down your number ")
first_digit = int(number[0])
second_digit = int(number[1])
total = first_digit + second_digit
print(total)


#OR

number = input("write down your number ")
first_digit = int(number[0])
second_digit = int(number[1])
total = str(first_digit + second_digit)
print("The sum total of two digit number you entered is " + total)



#OR


number = input("write down your number ")
first_digit = int(number[0])
second_digit = int(number[1])
total = str(first_digit + second_digit)
print("The sum total of two digit number  "  + number  + ' is ' + total)
