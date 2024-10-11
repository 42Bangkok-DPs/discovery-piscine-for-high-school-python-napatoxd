from checkmate import is_king_in_check 

def main():
    board =   """\
..
.K\
"""
    board = board.strip().splitlines()

    is_king_in_check(board)

if __name__ == "__main__":
    main()
