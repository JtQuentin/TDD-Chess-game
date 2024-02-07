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
    
    def CreateTeam():
        board = chessGame.CreateBoard()

        whiteTeam = []
        whiteTeam.append([chessGame.Type.WTOWER.value,chessGame.Type.WRIDER.value,chessGame.Type.WCRAZY.value,chessGame.Type.WQUEEN.value,chessGame.Type.WKING.value,chessGame.Type.WCRAZY.value,chessGame.Type.WRIDER.value,chessGame.Type.WTOWER.value])
        whiteTeam.append([chessGame.Type.WPAWN.value]*8)
        
        board[0] = whiteTeam[0]
        board[1] = whiteTeam[1]

        blackTeam = []
        blackTeam.append([chessGame.Type.BTOWER.value,chessGame.Type.BRIDER.value,chessGame.Type.BCRAZY.value,chessGame.Type.BQUEEN.value,chessGame.Type.BKING.value,chessGame.Type.BCRAZY.value,chessGame.Type.BRIDER.value,chessGame.Type.BTOWER.value])
        blackTeam.append([chessGame.Type.BPAWN.value]*8)

        board[6] = blackTeam[1]
        board[7] = blackTeam[0]

        return board
    
    def ValidMove():
        

        
# print(chessGame.CreateBoard())
print(chessGame.CreateTeam())


