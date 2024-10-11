print('WELCOME TO THE TIP 💵💵 CALCULATOR.')
total_bill = float(input('What was the total bill? \n💲'))
tip = float(input('What percentage of tip would you like to give?\n💯'))
people = int(input('How many people to split the bill?\n👬'))
tip_amount = float(total_bill * (tip / 100))
Amount_per_person = (total_bill + tip_amount) / people
money = round(Amount_per_person , 2)
print(f'Each person should pay:\n{money}')
