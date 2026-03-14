class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'

    def print_board(self):
        # Print the current state of the board
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.check_win():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                return True
            elif ' ' not in self.board:
                self.print_board()
                print("It's a draw!")
                return True
            else:
                self.current_player = 'X' if self.current_player == 'O' else 'O'
        else:
            print("Invalid move. Try again.")
        return False

    def check_win(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontal
                          (0, 3, 6), (1, 4, 7), (2, 5, 8), # vertical
                          (0, 4, 8), (2, 4, 6)]  # diagonal
        for condition in win_conditions:
            if self.board[condition[0]] == self.current_player and self.board[condition[1]] == self.current_player and self.board[condition[2]] == self.current_player:
                return True
        return False

    def play(self):
        while True:
            self.print_board()
            move = int(input(f"Player {self.current_player}, enter your move (0-8): "))
            if self.make_move(move):
                break

if __name__ == '__main__':
    game = TicTacToe()
    game.play()