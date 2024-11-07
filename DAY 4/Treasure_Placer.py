row1 = ["🥰", "🥰", "🥰"]
row2 = ["🥰", "🥰", "🥰"]
row3 = ["🥰", "🥰", "🥰"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure (e.g., 23): ")
horizontal = int(position[0])  # Column number
vertical = int(position[1])    # Row number

# Update the specific position on the map
map[vertical - 1][horizontal - 1] = "🤑"

# Print the updated map
print(f"{row1}\n{row2}\n{row3}")

