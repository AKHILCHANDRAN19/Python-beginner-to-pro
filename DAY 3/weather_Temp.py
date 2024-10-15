#Question:
#Write a Python program that takes three inputs from the user:

#temperature (an integer representing the temperature in degrees Celsius).
#weather_condition (a string that could be "sunny", "rainy", or "snowy").
#wind_speed (an integer representing the wind speed in km/h).
#The program should classify the day based on the following conditions:

#If the temperature is above 30:
#If the weather condition is "sunny", print "Hot and sunny, stay hydrated."
#If the weather condition is "rainy", print "Hot and rainy, it's a humid day."
#If the weather condition is "snowy", print "Hot but snowy? Something is wrong!"
#If the temperature is between 15 and 30:
#If the weather condition is "sunny", print "Pleasant day with sunshine."
#If the weather condition is "rainy" and the wind speed is above 20 km/h, print "Cool and rainy with strong winds."
#If the weather condition is "rainy" and the wind speed is 20 km/h or below, print "Cool and rainy."
#If the weather condition is "snowy", print "Snowy but not too cold."
#If the temperature is below 15:
#If the weather condition is "sunny", print "Cold but sunny."
#If the weather condition is "rainy", print "Cold and rainy, better stay warm."
#If the weather condition is "snowy" and the wind speed is above 30 km/h, print "Blizzard conditions! Stay inside."
#If the weather condition is "snowy" and the wind speed is 30 km/h or below, print "Light snow, bundle up."
#solution

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
      
