# Taking input from the user and converting it to an integer
year = int(input('Enter your year '))

# Checking if the year is divisible by 4 (primary condition for leap year)
if year % 4 == 0:
    
    # If divisible by 4, check if it's divisible by 100 (century year)
    if year % 100 == 0:
        
        # If divisible by 100, check if it's divisible by 400 (special case for century years)
        if year % 400 == 0:
            # If divisible by 400, it's a leap year
            print('Its a leap year')
        else:
            # If divisible by 100 but not 400, it's not a leap year
            print('Its not a leap year')
    
    else:
        # If divisible by 4 but not 100, it's a leap year
        print('Its a leap year')

else:
    # If not divisible by 4, it's not a leap year
    print('Its not a leap year')
