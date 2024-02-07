from enum import Enum

class chessGame:
    board = ""
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
    
    def CreateBoard(self):
        self._board = []
        for _ in range(8):
            row = [' '] *8
            self._board.append(row) 
        return self._board

    def PrintBoard(self):
        for row in self._board:
            print(row)
    
    def CreateTeam(self):
        self._board = chessGame.CreateBoard()

        whiteTeam = []
        whiteTeam.append([chessGame.Type.WTOWER.value,chessGame.Type.WRIDER.value,chessGame.Type.WCRAZY.value,chessGame.Type.WQUEEN.value,chessGame.Type.WKING.value,chessGame.Type.WCRAZY.value,chessGame.Type.WRIDER.value,chessGame.Type.WTOWER.value])
        whiteTeam.append([chessGame.Type.WPAWN.value]*8)
        
        self._board[0] = whiteTeam[0]
        self._board[1] = whiteTeam[1]

        blackTeam = []
        blackTeam.append([chessGame.Type.BTOWER.value,chessGame.Type.BRIDER.value,chessGame.Type.BCRAZY.value,chessGame.Type.BQUEEN.value,chessGame.Type.BKING.value,chessGame.Type.BCRAZY.value,chessGame.Type.BRIDER.value,chessGame.Type.BTOWER.value])
        blackTeam.append([chessGame.Type.BPAWN.value]*8)

        self._board[6] = blackTeam[1]
        self._board[7] = blackTeam[0]

        return self._board
        
chessgame = chessGame 
print(chessgame.CreateBoard(chessgame))
print(chessGame.CreateTeam(chessgame))


