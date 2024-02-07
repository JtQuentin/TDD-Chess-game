from chessgame import chessGame

# def test_CreatePion():
#     assert chessGame.CreatePion(0) == ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜", "♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"]
#     assert chessGame.CreatePion(1) == ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙", "♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
#     assert chessGame.CreatePion(78) == None

def test_ShowPion():
    assert chessGame.Type.BCRAZY.value == '♝'
    assert chessGame.Type.BKING.value == '♚'
    assert chessGame.Type.BPAWN.value == '♟'
    assert chessGame.Type.BQUEEN.value == '♛'
    assert chessGame.Type.BRIDER.value == '♞'
    assert chessGame.Type.BTOWER.value == '♜'
    assert chessGame.Type.WCRAZY.value == '♗'
    assert chessGame.Type.WKING.value == '♔'
    assert chessGame.Type.WPAWN.value == '♙'
    assert chessGame.Type.WQUEEN.value == '♕'
    assert chessGame.Type.WRIDER.value == '♘'
    assert chessGame.Type.WTOWER.value == '♖'