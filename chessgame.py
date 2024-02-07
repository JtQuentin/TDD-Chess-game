class chessGame:
    def CreatePion(value):
        pion = []
        if(value == 0):
            pion = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜", "♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"]
        elif(value == 1):
            pion = ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙", "♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
        else:
            return None
        return pion