class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player_turn = 'X'
        self.game_over = False

    def print_board(self):
        print('-' * 13)
        for row in self.board:
            print('|', end=' ')
            for cell in row:
                print(cell, end=' | ')
            print('\n' + '-' * 13)

    def is_valid_cell(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3

    def is_empty_cell(self, row, col):
        return self.board[row][col] == ' '

    def make_move(self, row, col):
        if not self.is_valid_cell(row, col):
            print("Invalid cell coordinates. Try again.")
            return
        if not self.is_empty_cell(row, col):
            print("Cell is not empty. Try again.")
            return
        self.board[row][col] = self.player_turn
        self.check_winner()
        if not self.game_over:
            self.player_turn = 'X' if self.player_turn == 'O' else 'O'

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                self.game_over = True
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                self.game_over = True
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.game_over = True
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.game_over = True
            return

    def play(self):
        while not self.game_over:
            self.print_board()
            print(f"Player '{self.player_turn}', it's your turn.")
            move = input("Enter your move (row and column, e.g., 1 2): ").split()
            if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit():
                print("Invalid input format. Try again.")
                continue
            row, col = int(move[0]) - 1, int(move[1]) - 1
            self.make_move(row, col)

        self.print_board()
        if self.player_turn == 'X':
            print("Player 'O' wins!")
        else:
            print("Player 'X' wins!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
