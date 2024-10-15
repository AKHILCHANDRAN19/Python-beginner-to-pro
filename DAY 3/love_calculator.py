print("Welcome to the Love Calculator!")

# Get user input for both names
name1 = input("Enter the first name: ").lower()
name2 = input("Enter the second name: ").lower()

# Combine the names
combined_names = name1 + name2

# Calculate the number of occurrences for the word 'TRUE'
true_count = combined_names.count('t') + combined_names.count('r') + combined_names.count('u') + combined_names.count('e')

# Calculate the number of occurrences for the word 'LOVE'
love_count = combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e')

# Combine the true and love counts to create a score (e.g., 'true' count of 4 and 'love' count of 5 will give 45)
love_score = int(str(true_count) + str(love_count))

# Output the score and message based on the score
print(f"Your love score is: {love_score}")

# Use nested if statements to determine the compatibility message
if love_score > 90 or love_score < 10:
    print("Your love is like oil and water. It just doesn't mix well!")
elif 40 <= love_score <= 60:
    print("You are quite compatible! Like peanut butter and jelly.")
else:
    print("Your relationship is okay, but you may need to put in some work.")
