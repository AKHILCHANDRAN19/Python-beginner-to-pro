row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
board = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Enter the position to place an 'X' (e.g., 12): ")
horizontal = int(position[0])
vertical = int(position[1])
board[horizontal - 1][vertical - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")
