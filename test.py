from chessgame import chessGame

def test_CreatePion():

    assert chessGame.CreatePion(0) == ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜", "♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"]
    assert chessGame.CreatePion(1) == ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙", "♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
    assert chessGame.CreatePion(78) == None