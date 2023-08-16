scores = {"computer": 0, "player": 0}

class Board:
    """
    The Board class, sets the board size, the number of ships,
    player's name, board type.
    """
    
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type 
        self.guesses = []
        self.ships = []

    def guess(self, x, y):
        self.guesses.append((x,y))
        self.board[x][y] = "X"

        