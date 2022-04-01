def is_solved(board):
    condition = {"is_empty": 0, "X": 1, "O": 2}
    for line in board:
        if line[0] == line[1] == line[2] != condition["is_empty"]:
            return line[0]
    if board[0][0] == board[1][1] == board[2][2] != condition["is_empty"]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != condition["is_empty"]:
        return board[0][2]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != condition["is_empty"]:
            return board[0][i]
    for i in range(3):
        for j in range(3):
            if board[i][j] == condition["is_empty"]:
                return -1

    return 0
