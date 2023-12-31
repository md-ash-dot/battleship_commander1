from random import randint

scores = {"computer": 0, "player": 0}

# Some of the code taken from studying the portfolio project 3 intro video by Code Institute 
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
        self.guesses.append((x, y))

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            self.board[x][y] = "X"
            return "Miss"

    def add_ship(self, x, y):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.board_type == "player":
                self.board[x][y] = "@"

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()


def valid_coordinates(x, y, board):
    """
    The coordinates are checked to see if it is  valid.
    """
    return 0 <= x < board.size and 0 <= y < board.size


def populate_board(board):
    """
    The game board is populated.
    """
    for _ in range(board.num_ships):
        while True:
            x = random_point(board.size)
            y = random_point(board.size)
            if valid_coordinates(x, y, board) and (x, y) not in board.ships:
                board.add_ship(x, y)
                break


def random_point(size):
    """
    Helper function to return a random integer between 0 and size.
    """
    return randint(0, size - 1)


def make_guess(board):
    """
    Take player's guess.
    """
    while True:
        try:
            x = int(input("Enter row:"))
            y = int(input("Enter column:"))
            if valid_coordinates(x, y, board) and (x, y) not in board.guesses:
                return x, y
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, enter numbers.")


def play_game(computer_board, player_board):
    """
    Plays the game.
    """
    while len(computer_board.ships) > 0 and len(player_board.ships) > 0:
        print("Player's board:")
        player_board.print_board()
        print("Computer's board:")
        computer_board.print_board()

        print("Player's turn:")
        x, y = make_guess(computer_board)
        result = computer_board.guess(x, y)
        print(result)
        current_computer_ships = len(computer_board.ships)
        if result == "Hit":
            scores["player"] += 1
            computer_board.ships.remove((x, y))

        if current_computer_ships == 0:
            print("Congratualtions! All enemy ships destroyed!")
            break

        print("Computer's turn:")
        x, y = random_point(player_board.size), random_point(player_board.size)
        result = player_board.guess(x, y)
        print(result)
        current_player_ships = len(player_board.ships)
        if result == "Hit":
            scores["computer"] += 1
            player_board.ships.remove((x, y))

        if current_player_ships == 0:
            print("Computer has won! You have lost the battle!")
            break

        print("-" * 50)
        print(f"Scores - Player: {scores['player']}")
        print(f"Computer: {scores['computer']}")
        print("-" * 50)

    print("GAME OVER")


def new_game():
    """
    Starts a new game, sets the board size and number of ships,
    resets the scores and initialises the board.
    """

    size = 5
    num_ships = 4
    print("Welcome to Battleship Commander!\n")
    print("You are the Commander in charge, sink all enemy ships.")
    print("Awaiting your command to strike at coordinates specified by you.\n")
    player_name = input("Please enter your name Commander: ")
    print("-" * 50)
    print(f"Welcome aboard Commander {player_name}")
    print(f"Number of ships: {num_ships}, Board size: {size}")
    print(f"LEGEND: @ ---> {player_name}'s ship, * ---> Destroyed ship")
    print("The top left coordinate is row-0 column-0")
    print("The bottom right coordinate is row-4 column-4")
    print("Rows and columns go from 0 to 4")
    print("You cannot guess the same coordinate more than once.")
    print("-" * 50)

    computer_board = Board(size, num_ships, "Computer", board_type="computer")
    player_board = Board(size, num_ships, player_name, board_type="player")

    populate_board(player_board)
    populate_board(computer_board)

    play_game(computer_board, player_board)
    print("Final Scores")
    print(f"Player: {scores['player']}, Computer: {scores['computer']}")


new_game()
