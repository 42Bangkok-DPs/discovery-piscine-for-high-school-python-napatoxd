class Piece:
    def __init__(self, color):
        self.color = color

class King(Piece):
    def __str__(self):
        return '♚' if self.color == 'white' else '♔'

    def is_in_check(self, board):
        king_position = None
        for i in range(8):
            for j in range(8):
                if isinstance(board.board[i][j], King) and board.board[i][j].color == self.color:
                    king_position = (i, j)
                    break
            if king_position:
                break

        if king_position:
            opponent_color = 'black' if self.color == 'white' else 'white'
            for i in range(8):
                for j in range(8):
                    piece = board.board[i][j]
                    if piece and piece.color == opponent_color:
                        if board.is_valid_move((i, j), king_position, piece):
                            return True
        return False

class Queen(Piece):
    def __str__(self):
        return '♛' if self.color == 'white' else '♕'

class Rook(Piece):
    def __str__(self):
        return '♜' if self.color == 'white' else '♖'

class Bishop(Piece):
    def __str__(self):
        return '♝' if self.color == 'white' else '♗'

class Knight(Piece):
    def __str__(self):
        return '♞' if self.color == 'white' else '♘'

class Pawn(Piece):
    def __str__(self):
        return '♟' if self.color == 'white' else '♙'

class Team:
    def __init__(self, color):
        self.color = color
        self.pieces = []

class Board:
    def __init__(self):
        self.board = self.create_board()
        self.white_team = Team('white')
        self.black_team = Team('black')
        self.setup_teams()  
        self.captures = []
        self.turn = 'white'  # กำหนดสีเริ่มต้นที่ขาว


    def create_board(self):
        return [[None for _ in range(8)] for _ in range(8)]

    def setup_teams(self):
        for i in range(8):
            self.board[6][i] = Pawn('white')
            self.white_team.pieces.append(self.board[6][i])
            self.board[1][i] = Pawn('black')
            self.black_team.pieces.append(self.board[1][i])

        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, PieceClass in enumerate(pieces):
            self.board[7][i] = PieceClass('white')
            self.white_team.pieces.append(self.board[7][i])
            self.board[0][i] = PieceClass('black')
            self.black_team.pieces.append(self.board[0][i])

    def display(self):
        print("  a b c d e f g h")
        for i, row in enumerate(self.board):
            print(8 - i, end=" ")
            print(' '.join(str(piece) if piece else '.' for piece in row))
        print("  a b c d e f g h")

        # แสดงข้อความการจับหมาก
        if self.captures:
            print("\nCaptures:")
            for message in self.captures:
                print(message)
            # ลบข้อความ
            self.captures.clear()


    def is_in_check(self, color):
        for i in range(8):
            for j in range(8):
                if isinstance(self.board[i][j], King) and self.board[i][j].color == color:
                    return self.board[i][j].is_in_check(self)
        return False

    def is_checkmate(self, color):
        if self.is_in_check(color):
            for i in range(8):
                for j in range(8):
                    piece = self.board[i][j]
                    if piece and piece.color == color:
                        for x in range(8):
                            for y in range(8):
                                if self.is_valid_move((i, j), (x, y), piece):
                                    original_piece = self.board[x][y]
                                    self.board[x][y] = piece
                                    self.board[i][j] = None
                                    if not self.is_in_check(color):
                                        self.board[i][j] = piece
                                        self.board[x][y] = original_piece
                                        return False
                                    self.board[i][j] = piece
                                    self.board[x][y] = original_piece
            return True
        return False

    def is_check(self, color):
        if self.is_in_check(color):
            print(f"{color.capitalize()} is in check!")

    def is_valid_move(self, start, end, piece):
        x1, y1 = start
        x2, y2 = end

        if not isinstance(piece, Knight):
            if not self.is_clear_path(start, end):
                return False

        if isinstance(piece, King):
            return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
        elif isinstance(piece, Queen):
            return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)
        elif isinstance(piece, Rook):
            return x1 == x2 or y1 == y2
        elif isinstance(piece, Bishop):
            return abs(x1 - x2) == abs(y1 - y2)
        elif isinstance(piece, Knight):
            return (abs(x1 - x2), abs(y1 - y2)) in [(2, 1), (1, 2)]
        elif isinstance(piece, Pawn):
            direction = -1 if piece.color == 'white' else 1
            start_row = 6 if piece.color == 'white' else 1

            if y1 == y2:
                if x1 + direction == x2 and not self.board[x2][y2]:
                    return True
                if x1 == start_row and x1 + 2 * direction == x2 and not self.board[x2][y2] and not self.board[x1 + direction][y1]:
                    return True
            elif abs(y1 - y2) == 1 and x1 + direction == x2:
                return self.board[x2][y2] and self.board[x2][y2].color != piece.color

        return False
    def is_clear_path(self, start, end):
        x1, y1 = start
        x2, y2 = end

        dx = x2 - x1
        dy = y2 - y1

        step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
        step_y = 0 if dy == 0 else (1 if dy > 0 else -1)

        x, y = x1 + step_x, y1 + step_y

        # ตรวจสอบขอบเขตของกระดาน
        while 0 <= x < 8 and 0 <= y < 8 and (x, y) != (x2, y2):
            if self.board[x][y]:
                return False
            x += step_x
            y += step_y

        return True


    def move(self, start, end):
        piece = self.board[start[0]][start[1]]
        destination_piece = self.board[end[0]][end[1]]

        # ตรวจสอบสีหมากให้ตรง
        if piece is None or piece.color != self.turn:
            print(f"Invalid move. It's {self.turn}'s pieces.")
            return False

        if piece and self.is_valid_move(start, end, piece):
            if destination_piece and destination_piece.color == piece.color:
                print("You cannot capture your own piece!")
                return False

            self.captures.clear()

            # Move piece
            original_piece = self.board[end[0]][end[1]]
            self.board[end[0]][end[1]] = piece
            self.board[start[0]][start[1]] = None

            # result in check
            if self.is_in_check(piece.color):
                self.board[start[0]][start[1]] = piece
                self.board[end[0]][end[1]] = original_piece
                print("Can't move! You are still in check.")
                return False

            # Check for capture
            if destination_piece:
                if isinstance(destination_piece, King):
                    print(f"{'White' if destination_piece.color == 'white' else 'Black'} King was captured!!!")
                    print(f"{'Black' if piece.color == 'black' else 'White'} Wins!!!!")
                    exit()

                capture_message = f"{'White' if piece.color == 'white' else 'Black'} {piece.__class__.__name__} captures {'White' if destination_piece.color == 'white' else 'Black'} {destination_piece.__class__.__name__} at {end[0] + 1},{chr(ord('a') + end[1])}!"
                self.captures.append(capture_message)

            return True
        else:
            print("Invalid move!")
            return False


def main():
    board = Board()
    board.display()

    while True:
        if board.is_checkmate(board.turn):
            print(f"{'Black' if board.turn == 'white' else 'White'} wins!")
            return

        board.is_check(board.turn)

        while True:
            try:
                start = input(f"{board.turn.capitalize()}'s turn - Where do you want to move (e.g., e2): ").strip()
                start = (8 - int(start[1]), ord(start[0]) - ord('a'))
                if start[0] < 0 or start[0] >= 8 or start[1] < 0 or start[1] >= 8:
                    raise ValueError("Coordinates out of bounds.")
            except (ValueError, IndexError):
                print("Invalid input. Please use the format 'e2'.")
                continue

            piece = board.board[start[0]][start[1]]

            # ตรวจสอบหมากตามสี
            if not piece or piece.color != board.turn:
                print(f"Invalid move. It's {board.turn}'s turn.")
                continue

            end = input("Where do you want to move to? (e.g., e4): ").strip()
            end = (8 - int(end[1]), ord(end[0]) - ord('a'))
            if end[0] < 0 or end[0] >= 8 or end[1] < 0 or end[1] >= 8:
                raise ValueError("Coordinates out of bounds.")

            if board.move(start, end):
                board.display()
                break

        # เปลี่ยนเทิร์น
        board.turn = 'black' if board.turn == 'white' else 'white'

main()
