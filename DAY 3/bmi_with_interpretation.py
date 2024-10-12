height = float(input('enter your height in m\n 📏'))
weight = float(input('enter your weight in kg\n⚖️'))
BMI = weight / (height ** 2)
if BMI < 18.5:
	print('You are underweight📉')
elif BMI < 25:
    print('You are  normal weight 🧍‍♂')
elif BMI < 30:
	print('You are over weight🍔📈')
elif BMI < 35:
	print('You are obese🍩')
else:
	print('You are Clinically obese🛑🏥')
