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
        
    # def CreatePion(value):
    #     pion = []
    #     if(value == 0):
    #         pion = [Type.WKING, "♞", "♝", "♛", "♚", "♝", "♞", "♜", "♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"]
    #     elif(value == 1):
    #         pion = ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙", "♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
    #     else:
    #         return None
    #     return pion