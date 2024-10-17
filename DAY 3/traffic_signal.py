colour = input('Enter the traffic light color (red, yellow, green): ').lower()
if colour == 'red':
  print('Action : stop')
elif colour == 'green':
  print('Action : Go')
elif colour == 'yellow':
  print('Action : wait')
else:
  print('you choose wrong input')
