import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # keep track of the winner!

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('|'.join(row))

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        self.board[square] = letter
        if self.winner(square, letter):
            self.current_winner = letter

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
        if square % 2 == 0:
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def minimax(self, board, depth, is_maximizing, difficulty):
        if self.current_winner == 'X':  # AI is X
            return 1
        elif self.current_winner == 'O':  # Human is O
            return -1
        elif ' ' not in board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in self.available_moves():
                board[i] = 'X'
                score = self.minimax(board, depth + 1, False, difficulty)
                board[i] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in self.available_moves():
                board[i] = 'O'
                score = self.minimax(board, depth + 1, True, difficulty)
                board[i] = ' '
                best_score = min(score, best_score)
            return best_score

    def best_move(self, difficulty):
        if difficulty == 'easy':
            return random.choice(self.available_moves())
        elif difficulty == 'medium':
            return min(self.available_moves(), key=lambda x: self.minimax(self.board, 0, True, 'medium'))
        elif difficulty == 'hard':
            return max(self.available_moves(), key=lambda x: self.minimax(self.board, 0, True, 'hard'))

    def play_game(self):
        difficulty = input('Choose difficulty (easy/medium/hard): ')
        while True:
            print('Current Board:')
            self.print_board()
            if self.current_winner:
                print(f'The winner is {self.current_winner}!')
                break
            if ' ' not in self.board:
                print('It\'s a tie!')
                break
            if self.current_turn == 'O':
                square = int(input('Choose your move (0-8): '))
                if square in self.available_moves():
                    self.make_move(square, 'O')
                    self.current_turn = 'X'
            else:
                print('AI is thinking...')
                square = self.best_move(difficulty)
                self.make_move(square, 'X')
                self.current_turn = 'O'
            replay = input('Play again? (yes/no): ')
            if replay.lower() != 'yes':
                break

if __name__ == '__main__':
    t = TicTacToe()
    t.play_game()