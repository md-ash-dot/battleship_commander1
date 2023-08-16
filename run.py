from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    The Board class, sets the board size, the number of ships,
    player's name, board type (player board or computer)
    Has methods for adding ships and guesses and printing the board.
    """
    
    def __init__(self, size, num_ships, name, board_type):
        self.size = size
        self.board = [["." for _ in range(size)] for _ in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.board_type = board_type 
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




def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)

def populate_board(board):
    """
    The game board is populated.
    """

    

        
def new_game():
    """
    Starts a new game, sets the board size and number of ships, 
    resets the scores and initialises the board.
    """

    size = 5
    num_ships=2
    print("Welcome to Battleship Commander!")
    print("You are the Commander in charge, sink all enemy ships.")
    print("Awaiting your command to strike at coordinates specified by you.")
    player_name = input("Please enter your name Commander: ")
    print(f"Welcome aboard Commander {player_name}")
    print(f"Number of ships: {num_ships}, Board size: {size}")

    computer_board = Board(size,num_ships, "Computer", board_type="computer")
    player_board = Board(size,num_ships, player_name, board_type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    

new_game()

