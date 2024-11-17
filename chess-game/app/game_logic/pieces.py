# Piece Definitions: Classes for King, Queen, Rook, Bishop, Knight, and Pawn.

class Piece:
    def __init__(self, color):
        self.color = color
        self.symbol = ""

    def is_valid_move(self, start, end, board):
        raise NotImplementedError("This method should be overridden in subclasses")

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "K" if color == "white" else "k"

    def is_valid_move(self, start, end, board):
        dx = abs(start[0] - end[0])
        dy = abs(start[1] - end[1])
        return max(dx, dy) == 1

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "Q" if color == "white" else "q"

    def is_valid_move(self, start, end, board):
        return Rook(self.color).is_valid_move(start, end, board) or Bishop(self.color).is_valid_move(start, end, board)

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "R" if color == "white" else "r"

    def is_valid_move(self, start, end, board):
        return start[0] == end[0] or start[1] == end[1]

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "B" if color == "white" else "b"

    def is_valid_move(self, start, end, board):
        return abs(start[0] - end[0]) == abs(start[1] - end[1])

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "N" if color == "white" else "n"

    def is_valid_move(self, start, end, board):
        dx = abs(start[0] - end[0])
        dy = abs(start[1] - end[1])
        return (dx, dy) in [(1, 2), (2, 1)]

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "P" if color == "white" else "p"

    def is_valid_move(self, start, end, board):
        direction = 1 if self.color == "white" else -1
        dx = end[0] - start[0]
        dy = end[1] - start[1]

        # Standard single forward move
        if dx == direction and dy == 0 and board[end[0]][end[1]] is None:
            return True
        
        # Double move on first turn
        if start[0] == 1 and self.color == "white" and dx == 2 * direction and dy == 0 and board[end[0]][end[1]] is None:
            return True
        if start[0] == 6 and self.color == "black" and dx == 2 * direction and dy == 0 and board[end[0]][end[1]] is None:
            return True

        # Capture move (diagonal)
        if dx == direction and abs(dy) == 1 and board[end[0]][end[1]] is not None:
            return True

        return False
