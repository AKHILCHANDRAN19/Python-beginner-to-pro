print('Welcome to the Coffee Shop!')
type = input('What type of coffee would you like? Espresso, Latte, or Cappuccino: ').lower()
size = input('What size? S,M or L? ; ').lower()
bill = 0
if type == 'espresso' and size ==  's':
  bill += 3
elif type == 'espresso' and size == 'm':
  bill += 4
elif type == 'espresso' and size ==  'l':
  bill += 5

if type == 'latte' and size == 's':
  bill += 4
elif type == 'latte' and size == 'm':
  bill += 5
elif type == 'latte' and size == 'l':
  bill += 6

if type == 'cappuccino' and size == 's':
  bill += 4.5
elif type == 'cappuccino' and size == 'm':
  bill += 5.5
elif type == 'cappuccino' and size == 'l':
  bill += 6.5

whipping_cream = input('Do you want Whipped Cream? Y or N: ').lower()
if whipping_cream == 'y':
  bill += .5
elif whipping_cream == 'n':
  bill += 0
print(f'You should pay ${bill}')
