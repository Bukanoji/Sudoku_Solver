import tkinter as tk
from tkinter import messagebox

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

def update_board_from_gui():
    for i in range(9):
        for j in range(9):
            value = entries[i][j].get()
            board[i][j] = int(value) if value.isdigit() and 1 <= int(value) <= 9 else 0

def solve_and_update():
    update_board_from_gui()
    temp_board = [row[:] for row in board]
    
    if solve(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(board[i][j]) if board[i][j] != 0 else None)
    else:
        messagebox.showerror("Error", "No solution exists")
        board[:] = temp_board

root = tk.Tk()
root.title("Sudoku Solver - Editable")

def validate_input(new_value):
    return new_value == "" or (new_value.isdigit() and 1 <= int(new_value) <= 9)

vcmd = root.register(lambda P: validate_input(P))

entries = []
board = [
    [0]*9 for _ in range(9)
]

for i in range(9):
    row_entries = []
    for j in range(9):
        block_i, block_j = i // 3, j // 3
        bg_color = "#ffffff" if (block_i + block_j) % 2 == 0 else "#e0e0e0"
        
        entry = tk.Entry(
            root,
            validate='key',
            validatecommand=(vcmd, '%P'),
            font=('Courier New', 18, 'bold'),
            width=3,
            justify='center',
            bg=bg_color,
            relief='solid',
            borderwidth=1
        )
        entry.grid(row=i, column=j, sticky='nsew', padx=1, pady=1)
        row_entries.append(entry)
    entries.append(row_entries)

solve_btn = tk.Button(root, text="Solve", command=solve_and_update)
solve_btn.grid(row=9, column=0, columnspan=9, sticky='we')

for i in range(9):
    root.rowconfigure(i, weight=1, minsize=50)
    root.columnconfigure(i, weight=1, minsize=50)

root.mainloop()