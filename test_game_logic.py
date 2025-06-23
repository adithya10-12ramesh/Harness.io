# test_game_logic.py
import pytest
from game_logic import check_winner

def test_player1_wins_row():
    list_one = [1, 2, 3]
    list_two = []
    assert check_winner(list_one, list_two) == "Player 1"

def test_player2_wins_diag():
    list_one = []
    list_two = [11, 15, 19]  # 1, 5, 9 for player 2
    assert check_winner(list_one, list_two) == "Player 2"

def test_draw():
    list_one = [1, 2, 6, 7, 8]
    list_two = [11, 12, 13, 15]
    assert check_winner(list_one, list_two) == "Draw"

def test_no_result_yet():
    list_one = [1]
    list_two = [11]
    assert check_winner(list_one, list_two) is None
