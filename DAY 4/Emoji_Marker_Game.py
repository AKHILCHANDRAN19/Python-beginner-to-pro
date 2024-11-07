# Create an empty 3x3 grid
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
grid = [row1, row2, row3]

# Print the initial grid
print(f"{row1}\n{row2}\n{row3}")

# Get the position input from the user
position = input("Enter the position to place the emoji (e.g., 13): ")
emoji = input("Enter the emoji to place: ")

column = int(position[0]) - 1  # Convert to 0-based index
row = int(position[1]) - 1     # Convert to 0-based index

# Place the emoji on the grid
grid[row][column] = emoji

# Print the updated grid
print(f"{row1}\n{row2}\n{row3}")
