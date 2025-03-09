def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queen(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queen(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def n_queen(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queen(board, 0, n):
        return None
    return board

n = 8
result = n_queen(n)
if result:
    for row in result:
        print(row)
else:
    print("No solution")
