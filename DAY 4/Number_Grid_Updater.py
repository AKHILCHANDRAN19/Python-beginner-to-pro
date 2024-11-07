# Create a 3x3 number grid
row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]
grid = [row1, row2, row3]

# Print the initial grid
print(f"{row1}\n{row2}\n{row3}")

# Get the position input from the user
position = input("Enter the position to update to 0 (e.g., 31): ")
column = int(position[0]) - 1  # Convert to 0-based index
row = int(position[1]) - 1     # Convert to 0-based index

# Update the grid
grid[row][column] = 0

# Print the updated grid
print(f"{row1}\n{row2}\n{row3}")
