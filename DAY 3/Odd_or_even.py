#programe for find out the odd or even number by a given input
number = int(input('Enter your number\n'))
result = number % 2
if result == 1:
	print('The number is an odd number')
else:
	print('The number is an even number')
