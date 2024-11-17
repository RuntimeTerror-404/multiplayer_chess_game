# Board Setup: An 8x8 chessboard with initial piece placements.

# app/game_logic/chess.py

from app.game_logic.pieces import King, Queen, Rook, Bishop, Knight, Pawn

class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_turn = "white"
        self.game_over = False

    def initialize_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Place pawns
        for i in range(8):
            board[1][i] = Pawn("white")
            board[6][i] = Pawn("black")
        
        # Place rooks
        board[0][0] = Rook("white")
        board[0][7] = Rook("white")
        board[7][0] = Rook("black")
        board[7][7] = Rook("black")

        # Place knights
        board[0][1] = Knight("white")
        board[0][6] = Knight("white")
        board[7][1] = Knight("black")
        board[7][6] = Knight("black")

        # Place bishops
        board[0][2] = Bishop("white")
        board[0][5] = Bishop("white")
        board[7][2] = Bishop("black")
        board[7][5] = Bishop("black")

        # Place queens
        board[0][3] = Queen("white")
        board[7][3] = Queen("black")

        # Place kings
        board[0][4] = King("white")
        board[7][4] = King("black")

        return board

    def display_board(self):
        for row in self.board:
            print(" ".join(piece.symbol if piece else "." for piece in row))

    def is_valid_move(self, start, end):
        piece = self.board[start[0]][start[1]]
        if piece and piece.color == self.current_turn:
            return piece.is_valid_move(start, end, self.board)
        return False

    def move_piece(self, start, end):
        piece = self.board[start[0]][start[1]]
        print(f"Attempting move from {start} to {end}")
        print(f"Piece at start position: {piece.symbol if piece else 'None'}")
    
        if piece:
            print(f"Piece color: {piece.color}, Current turn: {self.current_turn}")
    
        if self.is_valid_move(start, end):
            print("Move is valid")
            self.board[end[0]][end[1]] = piece
            self.board[start[0]][start[1]] = None
            self.current_turn = "black" if self.current_turn == "white" else "white"
            return True
    
        print("Move is invalid")
        return False
