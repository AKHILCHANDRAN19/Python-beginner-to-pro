temp = float(input('Enter the temperature: '))
weather = input('Enter the weather condition [sunny, rainy, snowy]: ').lower()
speed = float(input('Enter the wind speed (km/h): '))
if temp > 30:
    if weather == 'sunny':
        print('Hot and sunny, stay hydrated.')
    elif weather == 'rainy':
        print("Hot and rainy, it's a humid day.")
    elif weather == 'snowy':
        print('Hot but snowy? Something is wrong!')
    else:
        print('you choose wrong option!')
elif 15 <= temp <= 30:
    if weather == 'sunny':
        print('Pleasant day with sunshine.')
    elif weather == 'rainy' and speed > 20:
        print("Cool and rainy with strong winds.")
    elif weather == 'snowy':
        print('Snowy but not too cold.')
    else:
        print('you selected wrong option')
elif temp < 15:
    if weather == 'sunny':
        print('Cold but sunny.')
    elif weather == 'rainy':
        print('Cold and rainy, better stay warm.')
    elif weather == 'snowy' and speed > 30:
        print('Blizzard conditions! Stay inside')
    elif weather == 'snowy' and speed <= 30:
        print("Light snow, bundle up.")
    else:
        print('you choose wrong option!')
else:
    print('something is wrong with your input!')
      
