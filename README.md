# BATTLESHIP COMMANDER

Battleship Commander is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Users can plat against the computer in finding all the computer's battleships before the computer finds theirs. Each battleship occupies specific points on the board. You can see your battleships but not the computer's battleships.

The live link can be found here - [BATTLESHIP COMMANDER](https://battleships-commander-7b51cdde1b3a.herokuapp.com/)
![Responsive mockup](/images/am-i-responsive.JPG)

## How to play

Battleship Commander is based on the classic pen and paper game. You can read about it here [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)). In this version, you start in a grid-based game board where ships are placed. The game prompts the player to input coordinates for their guesses. These guesses are compared with the positions of the opponent's ships on the board. If a guessed coordinate matches a ship's location, it's marked as a hit; otherwise, it's marked as a miss. The game continues until all of the opponent's ships are successfully hit, at which point a victory message is displayed. After each guess, the updated game board is shown, allowing the player to strategize and visualize their progress in sinking the opponent's fleet.

## Features

### Existing Features
 - Random board generation: Ships are randomly placed on the computer and player board, adding an element of surprise and strategy to each game session.
 - Grid Board with Visualization: The game is played on a grid-based board, visually representing the ocean with coordinates. This layout immerses players in the classic naval battle experience.
 ![Player board](/images/player%20board.JPG)

 - Instructions and Game Rules: A concise set of instructions guides players through the gameplay mechanics, rules, and objectives, ensuring a clear understanding of how to engage in the battle.
 ![Instructions](/images/instructions.JPG)

 -Immersive Welcome Message: The game begins with a personalized welcome message that creates a sense of involvement and prepares players for the upcoming strategic challenge.
 ![Welcome message](/images/welcome%20message.JPG)

 -Player Identification: Players are prompted to enter their name at the start, which is then incorporated into messages, enhancing the feeling of commanding a fleet.
 ![Request name](/images/request%20name.JPG)

 -Scores Tracking: After each round, the game displays updated scores for both the player and the computer, fostering a competitive spirit and tracking progress.
 ![Scores](/images/scores.JPG)

 -Invalid Input Handling: The game actively addresses invalid inputs by notifying players about their mistakes and prompting them to retry, maintaining a smooth and user-friendly experience.
 ![Invalid input](/images/invalid%20input.JPG)

 -Valid Coordinates Enforcement: When players provide coordinates, the game ensures that they are within the bounds of the game board and not previously guessed, maintaining fairness and accuracy.
 ![Invalid coordinates](/images/invalid%20input%202.JPG)
 
 -Hit and Miss Visual Feedback: The game visually indicates whether a guess was a hit or a miss on the grid, allowing players to assess their progress and refine their strategy accordingly.

### Future Features
 - Set board size with user input.
 - Set number of ships with user input.
 - Allow users to position the ships by themselves.
 - Allow players to use bigger ships.
 - Allow players to choose if they want to play a two player game with a friend or computer.

## Data Model

The data model in this code revolves around simulating a simplified version of the classic Battleship game. It employs object-oriented programming principles by defining a Board class to represent the game board and its associated properties and behaviors. The class encapsulates attributes like board size, ship locations, player names, and board types. The game's logic is facilitated through methods such as add_ship, guess, print_board, and make_guess, which manage ship placement, guessing, and printing of the game state. Additionally, the code maintains a scores dictionary to track the scores of both the player and the computer opponent. Overall, this data model structures the game's components in a modular and organized manner, facilitating the interactive play of Battleship between the player and the computer.

## Testing

I have manually tested this project by doing the following:
 - Passed the code through a PEP8 linter and confirmed there are no problems.
 - Given invalid inputs: strings when numbers are expected, out of game board bounds input, same input twice.
 - Tested in my local terminal and the Code Institute Heroku terminal.
![PEP8 validator](/images/PEP8%20validator.JPG)

### Bugs
- Value of player name was not getting printed, instead the variable (player_name) was printed.
-->The variable was called within quotes, making it a string. Removed quotes to solve it.
- Error showing board class does not take any arguments.
-->The code did not have the right indentation inside the board class.The right indentations were used to correct the error.
- TypeError showing while running code.
-->The input was taken in as string so the input was converted to a string.
- The code kept running in an infinite loop.
--> The indentation used was wrong and the while loop made it run continuosly. Correct indentation were used to correct the error.
- Syntax error. f string unmatched.
-->The quotes used inside the f string caused the error. The opposite quotes were used inside the f string to correct it.
- Kept getting Error: you cannot add any more ships!, while starting game.
-->The populate_board was being called multiple times. The code was changed to call it only once, to corecct it.
- The game did not end even after all ships on a player's board were destroyed.
-->The function did not check the current number of ships. The play game function was used to check and end game if all ships on a board were destroyed.

## Remaining Bugs
- No bugs remaining

## Validator Testing
- PEP8 : All errors were corrected by identifying it with the validator. They were mostly whitespaces, missing last line, line character length and spaces.

### Deployment

This project was deployed using CodeInstitute's mock terminal for Heroku.

Steps for deployment:
- Fork or clone this repository.
- Create a new Heroku app.
- Set the buildbacks to Python and NodeJS in that order.
- Link the Heroku app to the repository.
- Click on Deploy.

### Credits

- Code Institute for the deployment terminal.
- Code Institute tutors and mentor.
- Wikipedia for the details of the Battleships game.
- Love Sandwiches project by Code Institute.
- The portfolio 3 overview video by Code Institute.
- Youtube channel Clever Programming Python Tutorials.
