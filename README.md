# Games
basic games made with Pygame

# Connect Four Game

![Connect Four](connect4bg.png)

**Connect Four** is a classic two-player connection game in which the players choose a color (either red or yellow) and take turns dropping colored discs from the top into a vertically suspended grid. The objective of the game is to connect four of one's own discs in a row, either horizontally, vertically, or diagonally, before your opponent does.

This Python code implements a graphical version of the Connect Four game using the Pygame library. Players can take turns to play and the game tracks their moves, detects wins, and displays the final result.

## Getting Started

Before running the code, ensure you have Python and Pygame installed on your system. If not, you can install Pygame using pip:

```bash
pip install pygame
```

Clone the repository and run the script to start the game:

```bash
python connect_four.py
```

## Gameplay

- The game window displays a Connect Four board with 7 columns and 6 rows.
- Players can select their preferred color (either red or yellow) at the beginning of the game.
- The game alternates between the two players, prompting them to make a move by clicking on the column where they want to drop their disc.
- The game continues until a player wins by connecting four discs vertically, horizontally, or diagonally or until there are no more empty spaces.
- When the game ends, it will display a message indicating the winner or declare a tie.

## Controls

- Click with the mouse to select a column to drop a disc.

## Features

- Interactive graphical interface for a two-player Connect Four game.
- Color selection for players at the start of the game.
- Gravity mechanism that ensures discs fall to the lowest available position in a column.
- Win condition detection for both horizontal and diagonal connections.
- Endgame display showing the result and allowing players to quit the game.

## Customization

You can easily customize this game by replacing the board and background images (`connect4board.png` and `connect4bg.png`) with your own images to give the game a unique look and feel.

## Code Structure

The code is structured into functions for better readability and maintainability. Key functions include:

- `main()`: Initializes the game, sets up the window, and starts the game loop.
- `playGame()`: Manages the game logic and player turns.
- `drawBoard()`: Renders the game board.
- `getSpaceClicked()`: Converts mouse coordinates to board coordinates.
- `printInfo()`: Displays whose turn it is.
- `isOnBoard()`: Checks if a coordinate is within the board.
- `chooseColor()`: Allows players to choose their color.
- `Move()`: Places a disc on the board.
- `finishingMove()`: Checks for a winning move.
- `newBoard()`: Creates a new game board.

## Enjoy the Game!

This Connect Four game offers a fun and challenging gaming experience. Feel free to explore and modify the code to add your own features or improvements. Have a great time playing!
