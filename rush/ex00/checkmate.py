def is_king_in_check(board):
    if not board or not all(len(row) == len(board) for row in board):
        print("Error: Invalid board input.")
        return

    size = len(board)
    king_position = None

    # Find king
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'K':
                king_position = (r, c)
                break
        if king_position:
            break

    if not king_position:
        print("Error: King not found on the board.")
        return

    king_row, king_col = king_position

    directions = [
        (1, 0),  # ล่าง
        (-1, 0), # บน
        (0, 1),  # ขวา
        (0, -1), # ซ้าย
        (1, 1),  # ล่างขวา
        (1, -1), # ล่างซ้าย
        (-1, 1), # บนขวา
        (-1, -1) # บนซ้าย
    ]

    for dr, dc in directions:
        r, c = king_row, king_col
        
        while 0 <= r < size and 0 <= c < size:
            r += dr
            c += dc
            if 0 <= r < size and 0 <= c < size:
                piece = board[r][c]
                if piece != '.':
                    if piece in 'RQ':  # Rook Queen
                        print("Success")
                        return
                    elif piece == 'B':  # Bishop 
                        if abs(dr) == abs(dc):
                            print("Success")
                            return
                    break  # 

    # คิงไม่โดนกิน
    print("Fail")
