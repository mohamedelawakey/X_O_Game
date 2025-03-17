import os

# Function to clear the console screen based on the operating system
def clear_screen():
    if os.name == 'nt':
        os.system('cls') # Windows
    else:
        os.system('clear') # macOS

# todo Player class
class Player:
    def __init__(self):
        self.name = ''
        self.symbol = ''

    # Function to prompt the user to enter a valid name (letters only)
    # Check if the input contains only letters
    def chose_name(self):
        while True:
            name = input('Enter your name (letters only): ')
            if name.isalpha():
                self.name = name
                break
            print("invalid name. please try again")

    # Function to allow the player to choose a single-letter symbol
    # Check if it's a single letter
    def chose_symbol(self):
        while True:
            symbol = input('Enter your symbol {} (only 1 letter)'.format(self.name))
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("invalid symbol. please chose again.")

# todo Menu class
class Menu:

    # Static method to display the main menu and get the user's choice
    @staticmethod
    def display_main_menu():
        main_menu = """Welcome to X O game:
Choose a number between 1-9 to place your symbol.
1. Start game
2. End game """
        print(main_menu)
        choice = input("Enter your choice (1 or 2): ")
        while choice not in['1','2']:
            print('Please Enter only 1 or 2.')
            choice = input("Enter your choice (1 or 2): ")
        return choice

    # Static method to display the end-game menu and get the user's choice
    @staticmethod
    def display_end_game_menu():
        end_game_menu = """Game Over.
1. Restart game
2. Quit game"""
        print(end_game_menu)
        choice = input("Enter your choice (1 or 2): ")
        while choice not in['1','2']:
            print('sorry, it\'s wrong please Enter only (1 or 2)')
            choice = input("Enter your choice (1 or 2): ")
        return choice

# todo Board class
class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1,10)] # Create a list of strings from '1' to '9'

    # Display the current state of the game board in a 3x3 grid format.
    def display_board(self):
        for i in range(0,9,3):
            print(f" {self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]} ")
            if i < 6:
                print("---+---+---")

    # Update the board by placing the player's symbol at the chosen position.
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    # Check if the chosen move is valid.
    def is_valid_move(self,choice):
        return self.board[choice-1].isdigit()

    # Reset the board to its initial state with numbers 1-9.
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

# todo game class
class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    # Start the game by displaying the main menu and handling the player's choice.
    # - If the player chooses '1', the game setup and gameplay start.
    # - If the player chooses '2', the game exits.
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == '1':
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    # Set up players by allowing them to enter their names and choose unique symbols.
    # - Each player enters their name.
    # - Players choose their symbols, ensuring they are different.
    def setup_players(self):
        for number,player in enumerate(self.players, start=1):
            print(f'player {number} Enter your details')
            player.chose_name()
            while True:
                player.chose_symbol()
                # Ensure the second player does not pick the same symbol as the first player
                if number == 2 and player.symbol == self.players[0].symbol:
                    print("Symbol already taken. Please choose a different one.")
                else:
                    break

    # Start and manage the game loop.
    # - Continuously displays the board and allows players to take turns.
    # - Checks for a win or a draw after each move.
    # - If the game ends, it prompts the player to restart or quit.
    def play_game(self):
        game_active = True
        while game_active:
            clear_screen()
            self.board.display_board()
            self.play_turn()
            # Check if there's a winner or the game ends in a draw
            if self.check_win() or self.check_draw():
                choice = self.menu.display_end_game_menu()
                if choice == '1':
                    self.restart_game()
                    return
                else:
                    self.quit_game()
                    game_active = False

    # Handle a single turn for the current player.
    # - Prompts the player to choose a cell (1-9).
    # - Validates the move and updates the board if valid.
    # - Displays a win or draw message if applicable.
    # - Switches to the next player if the game is still ongoing.
    def play_turn(self):
        player = self.players[self.current_player_index]
        print(f'{player.name}\'s turn ({player.symbol})')
        while True:
            try:
                cell_choice = int(input('Choose a cell (1-9): '))
                # Validate move and update the board
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print('Invalid move. Please try again')
            except ValueError:
                print('Please enter a number between 1 and 9.')
        # Check for a win or draw and display a message
        if self.check_win():
            clear_screen()
            self.board.display_board()
            print(f"Congratulations {player.name}! You won!")
        elif self.check_draw():
            clear_screen()
            self.board.display_board()
            print("It's a draw!")
        else:
            self.switch_player()

    # Switch to the next player by toggling the current player index.
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    # Check if there is a winning combination on the board.
    # - Defines all possible winning combinations (rows, columns, diagonals).
    # - Checks if any of these combinations contain the same symbol.
    def check_win(self):
        win_combinations = [
            [0,1,2],[3,4,5],[6,7,8], # rows
            [0,3,6],[1,4,7],[2,5,8], # columns
            [0,4,8],[2,4,6]          # diagonals
        ]
        for comp in win_combinations:
            if self.board.board[comp[0]] == self.board.board[comp[1]] == self.board.board[comp[2]]:
                return True
        return False

    # Check if the game is a draw.
    # - A draw occurs when all board cells are filled (i.e., no digits remain).
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    # Restart the game by resetting the board and setting the first player.
    # - Resets the board to its initial state.
    # - Sets the current player index back to 0.
    # - Starts a new game session.
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    # Quit the game and display a farewell message.
    def quit_game(self):
        print('Thank you for playing')

if __name__ == "__main__":
    # Create an instance of the Game class and start the game
    game = Game()
    game.start_game()
