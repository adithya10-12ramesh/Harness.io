# Flask-based version of the 2-player Tic Tac Toe game
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Board positions indexed 1-9
board = [' '] * 10

# Track player moves
player_one_moves = []
player_two_moves = []
current_player = 'X'

def check_winner(moves):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # cols
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]
    for combo in winning_combinations:
        if all(pos in moves for pos in combo):
            return True
    return False

@app.route('/')
def index():
    global board, player_one_moves, player_two_moves, current_player
    winner = None
    draw = False

    if check_winner(player_one_moves):
        winner = 'Player 1 (X)'
    elif check_winner(player_two_moves):
        winner = 'Player 2 (O)'
    elif len(player_one_moves) + len(player_two_moves) == 9:
        draw = True

    return render_template_string(TEMPLATE, board=board, winner=winner, draw=draw, current_player=current_player)

@app.route('/move/<int:pos>')
def move(pos):
    global board, player_one_moves, player_two_moves, current_player

    if board[pos] != ' ':
        return redirect(url_for('index'))  # position already taken

    board[pos] = current_player
    if current_player == 'X':
        player_one_moves.append(pos)
        current_player = 'O'
    else:
        player_two_moves.append(pos)
        current_player = 'X'

    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    global board, player_one_moves, player_two_moves, current_player
    board = [' '] * 10
    player_one_moves = []
    player_two_moves = []
    current_player = 'X'
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
