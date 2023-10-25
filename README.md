# Games
basic games made with Pygame

- [Connect Four Game](#connect Four Game)

# Connect Four Game

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



# Quoridor Game in Python

**Quoridor** is a two-player strategy board game implemented in Python using the Pygame library. The game is inspired by the classic Quoridor board game, where players compete to reach the opposite end of the board while strategically placing walls to block their opponent's progress. This implementation offers a graphical user interface and features two-player mode.

## How to Play

### Installation

1. Make sure you have Python installed on your computer.
2. Install the Pygame library if you haven't already. You can install it using pip:

   ```
   pip install pygame
   ```

3. Clone this repository or download the source code files.

### Running the Game

1. Open a terminal and navigate to the directory where the game files are located.
2. Run the game using Python:

   ```
   python quoridor.py
   ```

3. Follow the on-screen instructions to play the game.

### Gameplay

- **Objective**: The goal of the game is to reach the opponent's starting position (the opposite edge) or block their path effectively.

- **Red and Yellow Tiles**: The game starts with one player as "Red" and the other as "Yellow." Players take turns moving their respective pieces.

- **Walls**: Players have a limited number of walls they can place on the board to block their opponent's path. The game keeps track of the number of walls each player has left.

- **Hints**: You can choose to show hints (possible valid moves) during your turn to assist in your decision-making.

- **Controls**: Use the mouse to click and select your desired move, either by placing a wall or moving your piece.

- **Winning**: The game ends when one player successfully reaches the opponent's starting position or effectively blocks their path. The player who achieves this wins the game.

### Note on Wall Placement

- Walls can be placed horizontally ('h') or vertically ('v') on the board.
- Each wall placement consumes one of the player's available walls.
- Walls must be placed strategically to block your opponent effectively while allowing you to reach your goal.

## Features

- Graphical user interface for a visually pleasing gameplay experience.
- Multiplayer mode for two players to enjoy head-to-head matches.
- Interactive hints feature to aid players in making informed decisions.
- Wall placement system to strategically block your opponent's path.













# Quoridor Game in Python

This is a Python implementation of the classic board game Quoridor. The game can be played between two players, and the goal is to reach the opposite side of the board. Each player has a limited number of walls they can place to block their opponent's progress.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [How to Play](#how-to-play)
- [Game Features](#game-features)
- [Screenshots](#screenshots)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Quoridor is a strategy board game for two players. The game board consists of a 9x9 grid, and each player starts at opposite ends of the board. The objective of the game is to be the first to reach the row opposite your starting position. Players can move their pawn one space at a time or choose to place a wall on the board to block their opponent.

## Requirements

To run the Quoridor game, you will need:

- Python 3
- Pygame library

## How to Play

1. Choose your color: At the beginning of the game, you can choose to play as either the Red or Yellow pawn.

2. Game Board: The game board consists of a 9x9 grid, with Red and Yellow pawns starting at opposite ends.

3. Turns: Players take turns to make moves.

4. Pawn Movement: You can move your pawn one space in any direction - up, down, left, or right.

5. Placing Walls: You can also choose to place walls to block your opponent's path. Each player has a limited number of walls (10 for each player). To place a wall, specify whether it's horizontal (H) or vertical (V), and then enter two numbers corresponding to the wall's position.

6. Win: The first player to reach the row opposite their starting position wins the game.

## Game Features

- Interactive GUI: The game features an interactive graphical user interface built with the Pygame library.
- Player Choice: Players can choose their color at the start of the game.
- Wall Placement: Players can strategically place walls to block their opponent's path.
- Turn-Based: The game follows a turn-based system for player moves.
- Win Detection: The game checks for a win condition and displays the winner when the game is over.

## Screenshots

[Include screenshots of the game in action here]

## How to Run

1. Make sure you have Python 3 installed.

2. Install the Pygame library if you haven't already. You can do this using pip:

   ```
   pip install pygame
   ```

3. Clone this repository to your local machine.

4. Navigate to the directory where you cloned the repository.

5. Run the game using Python:

   ```
   python quoridor.py
   ```

6. Follow the on-screen instructions to play the game.

## Contributing

Contributions are welcome. If you'd like to contribute to the development of this game or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Enjoy playing Quoridor!
