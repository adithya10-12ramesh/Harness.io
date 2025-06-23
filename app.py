from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Game state
game_state = {
    'board': ['', '', '', '', '', '', '', '', ''],
    'current_player': 'X',
    'winner': None,
    'game_over': False
}

def check_winner(board):
    # Winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
            return board[combo[0]]
    
    if '' not in board:
        return 'Draw'
    
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/game_state')
def get_game_state():
    return jsonify(game_state)

@app.route('/api/make_move', methods=['POST'])
def make_move():
    global game_state
    
    data = request.json
    position = data.get('position')
    
    if game_state['game_over'] or game_state['board'][position] != '':
        return jsonify({'error': 'Invalid move'}), 400
    
    # Make the move
    game_state['board'][position] = game_state['current_player']
    
    # Check for winner
    winner = check_winner(game_state['board'])
    if winner:
        game_state['winner'] = winner
        game_state['game_over'] = True
    else:
        # Switch player
        game_state['current_player'] = 'O' if game_state['current_player'] == 'X' else 'X'
    
    return jsonify(game_state)

@app.route('/api/reset', methods=['POST'])
def reset_game():
    global game_state
    game_state = {
        'board': ['', '', '', '', '', '', '', '', ''],
        'current_player': 'X',
        'winner': None,
        'game_over': False
    }
    return jsonify(game_state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)