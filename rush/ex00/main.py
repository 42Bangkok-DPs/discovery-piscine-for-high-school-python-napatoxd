from checkmate import is_king_in_check 

def main():
    chessboard = [
        "........",
        "........",
        "...R....",  
        "........",
        "........",
        "........",
        "...K....",  
        "........"
    ]
    
    is_king_in_check(chessboard)

if __name__ == "__main__":
    main()
