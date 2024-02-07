from enum import Enum

class chessGame:
    class Type(Enum):
        BKING = '♚'
        BRIDER = '♞'
        BQUEEN = '♛'
        BTOWER = '♜'
        BCRAZY = '♝'
        BPAWN = '♟'
        WKING = '♔'
        WRIDER = '♘'
        WQUEEN = '♕'
        WTOWER = '♖'
        WCRAZY = '♗'
        WPAWN = '♙'
    
    def CreateBoard():
        board = []
        for _ in range(8):
            row = [' '] *8
            board.append(row) 
        return board

    def PrintBoard():
        for row in chessGame.CreateBoard():
            print(row)

print(chessGame.PrintBoard())

