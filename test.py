import pytest
from chessgame import chessGame

class TestChess:
    def test_show_pion(self):
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

    def test_create_board(self):
        assert len(chessGame.CreateBoard()) == 8
        for row in chessGame.CreateBoard():
            assert len(row) == 8

    def test_initial_state(self):
        for row in chessGame.CreateBoard():
            for cell in row:
                assert cell == ' '
    
    def test_create_team(self):
        assert chessGame.CreateTeam()[0] == ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        assert chessGame.CreateTeam()[1] == ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙']   
        assert chessGame.CreateTeam()[6] == ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟']
        assert chessGame.CreateTeam()[7] == ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'] 


if __name__ == '__main__':
    pytest.main([__file__])