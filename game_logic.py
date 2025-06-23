# save as game_logic.py
def check_winner(list_one, list_two):
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
    ]
    for cond in win_conditions:
        if all(c in list_one for c in cond):
            return "Player 1"
        elif all(c + 10 in list_two for c in cond):  # since player 2 uses 11-19
            return "Player 2"
    if len(list_one) + len(list_two) == 9:
        return "Draw"
    return None
