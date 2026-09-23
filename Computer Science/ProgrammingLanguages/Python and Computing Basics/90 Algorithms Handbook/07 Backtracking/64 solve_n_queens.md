# solve_n_queens

solve_n_queens(board_size) FUNCTION
Return every way to place board_size queens so none attack each other.
REMEMBER Place one queen per row; for each column check it isn't in a used column or diagonal (row-col and row+col
identify the two diagonals); recurse to the next row; undo on the way back.
WHEN TO USE Constraint-satisfaction puzzles (Sudoku, map colouring).
AVOID WHEN Large boards for ALL solutions (exponential growth).
REQUIRES board_size ≥ 1. Each solution lists the column of the queen in each row.
TIME Exponential (pruning makes it far below nn
). SPACE O(n).
USED FOR Classic backtracking demo; template for Sudoku solvers.
def solve_n_queens(board_size):
all_solutions = []
column_of_queen_in_row = []
used_columns = set()
used_row_minus_column = set()
used_row_plus_column = set()
def place_queen_in_row(row):
if row == board_size:
all_solutions.append(list(column_of_queen_in_row))
return
for column in range(board_size):
if (column in used_columns or (row - column) in used_row_minus_column
or (row + column) in used_row_plus_column):
continue # prune
used_columns.add(column)
used_row_minus_column.add(row - column)
used_row_plus_column.add(row + column)
column_of_queen_in_row.append(column)
place_queen_in_row(row + 1)
column_of_queen_in_row.pop() # undo
used_row_plus_column.remove(row + column)
used_row_minus_column.remove(row - column)
used_columns.remove(column)
place_queen_in_row(0)
return all_solutions
INPUT solve_n_queens(4) # each list: column of the queen in each row
OUTPUT [[1, 3, 0, 2], [2, 0, 3, 1]]
IN PRODUCTION No standard routine. Real puzzle and scheduling work uses a constraint solver such as OR-Tools CP-SAT.
CS Algorithms Toolkit Backtracking
64
