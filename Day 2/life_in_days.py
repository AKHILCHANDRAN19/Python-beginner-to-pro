present_age = int(input('What is your current age?\n'))
remaining_days = 32850 - (365 * present_age)
remaining_weeks = 4680 - (52 * present_age)
remaining_months = 1080 - (12 * present_age)
print(f"you have {remaining_days} days or you have {remaining_weeks} weeks or you have {remaining_months} months")



#little advanced


present_age = int(input('What is your current age?\n'))
destination_age = int(input('what is your dream age you want to live?\n'))
remaining_days = (destination_age * 365) - (365 * present_age)
remaining_weeks = (destination_age * 52) - (52 * present_age)
remaining_months = (destination_age * 12) - (12 * present_age)
print(f"you have {remaining_days} days or you have {remaining_weeks} weeks or you have {remaining_months} months 🥰")
