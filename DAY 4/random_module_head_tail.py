import random
integer = random.randint(1,2)
if integer == 1:
  print('head')
elif integer == 2:
  print('tail')


# OR

import random
integer = str(random.randint(1,2))
if integer == '1':
  print('head')
elif integer == '2':
  print('tail')


#OR

import random
result = random.randint(1,10000)
new_result = result % 2
if new_result == 0:
  print(f'your random number is {result} so your option is head')
else:
  print(f'your random number is {result} so your option is tail')
