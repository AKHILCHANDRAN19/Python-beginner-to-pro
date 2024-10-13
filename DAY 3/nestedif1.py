age = 18
has_permission = True

if age >= 18:  # Outer if
    print("You are an adult.")
    
    if has_permission:  # Inner if (nested inside the outer if)
        print("You can enter the club.")
    else:
        print("You need permission to enter.")
else:
    print("You are not old enough to enter.")
