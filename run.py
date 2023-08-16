scores = {"computer": 0, "player": class Board:
    """
    Board class, sets the board size, the number of ships, 
    the player's name and the board type.
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = type
   

print("Test")