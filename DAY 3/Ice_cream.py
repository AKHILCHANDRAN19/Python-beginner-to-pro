print('Welcome to the Ice Cream Parlor!')
ice_Cream = input('Which ice cream do you want? Vanilla, Chocolate, or Strawberry:').lower()
bill = 0
if ice_Cream == 'vanilla':
  bill += 5
elif ice_Cream == 'chocolate':
  bill += 6
elif ice_Cream == 'strawberry':
  bill += 6.5
else:
    print('Sorry, we do not have that flavor.')
    exit()
cup = input('Do you want a Cone or a Cup? ').lower()
if cup == 'cone':
  bill += 1
elif cup == 'cup':
  bill += 0.5
sprinkles = input('Do you want Sprinkles? Y or N: ').lower()
if sprinkles == 'y':
  bill += 0.5
elif sprinkles == 'n':
  bill += 0
print(f'your total bill is ${bill}')
