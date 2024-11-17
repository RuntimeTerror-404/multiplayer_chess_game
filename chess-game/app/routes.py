# app/routes.py

from flask import Blueprint, request, jsonify
from app.game_logic.chess import ChessGame

main = Blueprint('main', __name__)
game = ChessGame()

@main.route('/move', methods=['POST'])
def make_move():
    data = request.json
    start = data.get('start')  # Example: [6, 4] (pawn e2 to e4)
    end = data.get('end')

    if game.move_piece(tuple(start), tuple(end)):
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "invalid move"}), 400

@main.route('/board', methods=['GET'])
def get_board():
    board_state = [[piece.symbol if piece else "." for piece in row] for row in game.board]
    return jsonify({"board": board_state}), 200


@main.route('/debug/board', methods=['GET'])
def debug_board():
    board_state = [
        [piece.symbol if piece else "." for piece in row]
        for row in game.board
    ]
    print("\nCurrent Board State:")
    for row in board_state:
        print(" ".join(row))
    return jsonify({"board": board_state}), 200
