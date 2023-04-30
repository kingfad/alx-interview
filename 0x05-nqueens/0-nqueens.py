import sys

def solve_n_queens(row, board, N):
    if row == N:
        return [board]
    
    solutions = []
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solutions += solve_n_queens(row+1, board, N)
            board[row] = -1
    
    return solutions

def is_valid(board, row, col):
    for r, c in enumerate(board):
        if c == col or r-c == row-col or r+c == row+col:
            return False
    return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [-1] * N
    solutions = solve_n_queens(0, board, N)
    
    for sol in solutions:
        print(" ".join(str(col) for col in sol))
