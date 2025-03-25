# X_O_Game
🎮 X & O Game is a simple console-based Tic-Tac-Toe game built in Python. The game supports two players taking turns to place their symbols on a 3x3 board. The goal is to align three symbols in a row, column, or diagonal to win the game.

## Overview:   
X & O Game (Tic-Tac-Toe) is a console-based two-player game developed in Python. It follows the principles of clean code and object-oriented programming, ensuring maintainability and scalability. The game provides a simple yet interactive way to play Tic-Tac-Toe, where two players take turns marking spaces on a 3x3 grid until one of them wins or the game ends in a draw.
   
## Objectives:
The primary goal of this project is to:
- Provide an interactive command-line Tic-Tac-Toe experiencee.    
- Apply OOP principles to structure the game efficiently.  
- Ensure code readability and maintainability using clean code practices.  
- Implement a user-friendly interface with input validation.  

## Features:   
- **Two-player mode:** Players enter their names and choose unique symbols.   
- **Turn-based gameplay:** Players take turns selecting positions on the board.  
- **Win and draw detection:** The game checks for a winner or a tie after each move.  
- **Menu system:** Players can start, restart, or quit the game.   
- **Board validation:** Prevents players from selecting an already occupied cell.    
- **Clean UI in the console:** The game board updates dynamically.    

## Project Structure:
The project consists of the following main components:  
- **Player Class:** Handles player details (name and symbol).  
- **Menu Class:** Manages the game menus (start, restart, quit).  
- **Board Class:** Maintains the game board and updates it based on player moves.  
- **Game Class:** Controls the overall game logic, including turns, win/draw conditions, and game flow.  

## How It Works:
1. Players enter their names and choose symbols.  
2. The game board is displayed, and Player 1 starts.  
3. Players take turns choosing a cell (1-9) to place their symbol.  
4. The game checks for a winner or a draw after each move.  
5. If there's a winner, the game announces it; otherwise, it continues until a draw.  
6. Players can choose to restart or quit after a game ends.  

## Future Enhancements:
- Implement an AI opponent for single-player mode.  
- Add a GUI version using Tkinter or PyQt.  
- Store player statistics for tracking wins and losses.  
- Introduce different difficulty levels for AI-based gameplay.  

## Requirements:
- Python 3.x      
- Compatible with Windows, macOS, and Linux  

## How to Run the Game:
1. Clone the repository:  
   ```bash
   git clone https://github.com/mohamedelawakey/X_O_Game.git
2. Navigate to the project directory:  
   ```bash
   cd XO-Game
3. Navigate to the project directory:  
   ```bash
   python game.py

# Contribution Guidelines
- Fork the repository and create a new branch. 
- Commit changes with clear messages.
- Submit a pull request with a description of your improvements.
