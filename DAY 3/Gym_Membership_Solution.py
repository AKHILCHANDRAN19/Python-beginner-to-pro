print('Welcome to the Gym!')
age = int(input('How old are you?  '))
bill = 0
if age < 18:
  bill += 20
elif 18 >= age <= 40:
  bill += 30
elif age > 40:
  bill += 25
  
personal_trainer = input('Do you want a Personal Trainer? Y or N: ').lower()
if personal_trainer == 'y':
   bill += 14
elif personal_trainer == 'n':
   bill += 0
print(f'You pay ${bill} per month.')
