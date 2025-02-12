def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    for j in range(9):
        if board[pos[0]][j] == num and pos[1] != j:
            return False
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    start_row = (pos[0] // 3) * 3
    start_col = (pos[1] // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False

board = [
    [2, 6, 7, 0, 8, 4, 0, 0, 0],
    [0, 0, 3, 2, 5, 0, 0, 0, 0],
    [9, 0, 4, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 7, 8, 9, 6, 2],
    [0, 7, 6, 4, 0, 0, 1, 0, 5],
    [0, 0, 0, 0, 0, 1, 3, 7, 0],
    [7, 0, 5, 8, 0, 2, 4, 9, 0],
    [0, 0, 0, 0, 0, 5, 2, 0, 0],
    [4, 2, 0, 1, 0, 0, 7, 5, 3]
]

print("Original Sudoku:")
print_board(board)
print("\nSolving...\n")
if solve(board):
    print("Solved Sudoku:")
    print_board(board)
else:
    print("No solution exists for this Sudoku.")