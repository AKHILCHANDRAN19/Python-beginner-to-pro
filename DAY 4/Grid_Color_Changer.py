# Create a 3x3 color grid
row1 = ['red', 'blue', 'green']
row2 = ['yellow', 'purple', 'orange']
row3 = ['pink', 'gray', 'white']
grid = [row1, row2, row3]

# Print the initial grid
print(f"{row1}\n{row2}\n{row3}")

# Get the position input from the user
position = input("Enter the position to change color (e.g., 11): ")
new_color = input("Enter the new color: ")

column = int(position[0]) - 1  # Convert to 0-based index
row = int(position[1]) - 1     # Convert to 0-based index

# Change the color in the grid
grid[row][column] = new_color

# Print the updated grid
print(f"{row1}\n{row2}\n{row3}")
