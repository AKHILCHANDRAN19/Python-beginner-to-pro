print('Welcome to the Movie Ticket Booking!')
age = int(input('How old are you?\n'))
bill = 0
if age < 12:
  bill += 5
elif age < 18:
  bill += 7
elif age > 18 and age <= 60:
  bill += 12
elif age > 60:
  bill += 8
three_d = input('Do you want to watch a 3D movie? Y or N: ').lower()
if three_d == 'y':
  bill += 3
elif three_d == 'n':
  bill += 0
else:
  print('You entered wrong option')
print(f'you should pay ${bill}')
