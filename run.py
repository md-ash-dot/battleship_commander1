from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    The Board class, sets the board size, the number of ships,
    player's name, board type (player board or computer)
    Has methods for adding ships and guesses and printing the board.
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

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x,y))
            if self.type == "player":
                self.board[x][y] = "@"


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)

        


