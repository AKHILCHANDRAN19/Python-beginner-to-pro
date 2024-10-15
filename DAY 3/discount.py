#Discount Calculator
#Question: Write a Python program that calculates the total amount a customer has to pay after applying a discount based on their membership level and purchase amount. The rules are as follows:

#If the membership level is "Gold":
#If the purchase amount is greater than or equal to 1000, apply a 20% discount.
#If the purchase amount is between 500 and 1000, apply a 15% discount.
#If the purchase amount is less than 500, apply a 10% discount.
#If the membership level is "Silver":
#If the purchase amount is greater than or equal to 1000, apply a 15% discount.
#If the purchase amount is between 500 and 1000, apply a 10% discount.
#If the purchase amount is less than 500, apply a 5% discount.
#If the membership level is "Bronze":
#If the purchase amount is greater than or equal to 1000, apply a 10% discount.
#If the purchase amount is between 500 and 1000, apply a 5% discount.
#If the purchase amount is less than 500, no discount is applied.

membership = input('Enter membership level (Gold/Silver/Bronze): ').lower()
amount = int(input("Enter purchase amount: "))
pay = 0
if membership == 'gold':
  if amount >= 1000:
    pay = amount * (20 / 100)
  elif 500 <= amount <= 1000:
    pay = amount * (15 / 100)
  elif amount < 500:
    pay = amount * (10 / 100)
elif membership == 'silver':
   if amount >= 1000:
     pay = amount * (15 / 100)
   elif 500 <= amount <= 1000:
     pay = amount * (10 / 100)
   elif amount < 500:
     pay = amount * (5 / 100)
elif membership == 'bronze':
  if amount >= 1000:
    pay = amount * (10 / 100)
  elif 500 <= amount <= 1000:
    pay = amount * (5 / 100)
  else:
    pay = 0
else:
  print('something not correct with your input')
discounted_amount = amount - pay
print(f'Total amount to pay:{discounted_amount}')
   
