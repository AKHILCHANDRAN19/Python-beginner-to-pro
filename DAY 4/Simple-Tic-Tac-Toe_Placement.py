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



### Structure of `board` as a 2D List
#The `board` is defined as:
#```python
#board = [row1, row2, row3]
#```
#This means:
#- `board[0]` is `row1`.
#- `board[1]` is `row2`.
#- `board[2]` is `row3`.

#Each element in `board` is itself a list, so `board` is a list containing other lists. When you access an element in `board`, like `board[0][1]`, you're actually accessing an element in `row1`.

### Accessing Elements Using Indices
#When the user enters a position like "12":
#1. `horizontal = 1`, `vertical = 2`.
#2. The script calculates `board[horizontal - 1][vertical - 1]`, which translates to `board[0][1]`.

### How Python Understands This:
#- **`board[0]`** selects the first row (`row1`), which is `[' ', ' ', ' ']`.
#- **`board[0][1]`** accesses the second element in `row1`, which is the position where the `X` will be placed.

### Visual Breakdown:
#Consider the `board` as:
#```
#[[' ', ' ', ' '],  # This is row1
# [' ', ' ', ' '],  # This is row2
# [' ', ' ', ' ']]  # This is row3
#```

#- `board[0][1]` points to the second element in `row1` (first row), which is marked as `X`:
#```
#[[' ', 'X', ' '],  # Modified row1
# [' ', ' ', ' '],  # row2 remains the same
# [' ', ' ', ' ']]  # row3 remains the same
#```

### Why This Works:
#- **2D Indexing**: The 2D list structure (`board`) maintains the idea of rows and columns. Each `board[i]` is a row, and `board[i][j]` is a column within that row.
#- **Reference to Rows**: `board` holds references to `row1`, `row2`, and `row3`. Modifying `board[0][1]` is the same as modifying `row1[1]`, so the change reflects in the 2D representation.

### Final Clarification:
#Even though `board` is a "combined list" of rows, each `board[i]` is still a separate list representing a row. The 2D indexing (`board[row][column]`) allows the script to understand which specific element to update.
