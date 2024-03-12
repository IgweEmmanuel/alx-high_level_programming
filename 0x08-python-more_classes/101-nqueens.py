#!/usr/bin/python3
"""queen chess gaem"""
import sys

def print_solution(board):
    N = len(board)
    for row in range(N):
        print("[{}, {}]".format(row, board[row]))

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N):
    if row == N:
        print_solution(board)
        print()
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N)
            board[row] = -1  # Backtrack

def nqueens(N):
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)
    
    nqueens(sys.argv[1])

