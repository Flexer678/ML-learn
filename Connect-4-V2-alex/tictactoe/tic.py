import numpy as np

class Connect4:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((rows, columns), dtype=int)
        self.current_player = 1

    def display_board(self):
        print(self.board)

    def is_valid_move(self, column):
        return self.board[0][column] == 0

    def make_move(self, column):
        for row in range(self.rows-1, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                break

    def check_win(self):
        # Check rows
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3] != 0:
                    return True

        # Check columns
        for row in range(self.rows - 3):
            for col in range(self.columns):
                if self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col] != 0:
                    return True

        # Check diagonals (positive slope)
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3] != 0:
                    return True

        # Check diagonals (negative slope)
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == self.board[row - 3][col + 3] != 0:
                    return True

        return False

    def is_full(self):
        return np.all(self.board != 0)

    def get_possible_moves(self):
        return [col for col in range(self.columns) if self.is_valid_move(col)]

    def evaluate_board(self):
        # Evaluate the board for the current player
        player = self.current_player

        # Check rows for potential wins
        for row in range(self.rows):
            for col in range(self.columns - 3):
                window = self.board[row][col:col + 4]
                if np.array_equal(window, [player, player, player, player]):
                    return float('inf')

        # Check columns for potential wins
        for col in range(self.columns):
            for row in range(self.rows - 3):
                window = self.board[row:row + 4, col]
                if np.array_equal(window, [player, player, player, player]):
                    return float('inf')

        # Check diagonals (positive slope) for potential wins
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                window = [self.board[row + i][col + i] for i in range(4)]
                if np.array_equal(window, [player, player, player, player]):
                    return float('inf')

        # Check diagonals (negative slope) for potential wins
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                window = [self.board[row - i][col + i] for i in range(4)]
                if np.array_equal(window, [player, player, player, player]):
                    return float('inf')

        # No potential wins for the current player
        return 0

    def minimax(self, depth, maximizing_player):
        if depth == 0 or self.check_win() or self.is_full():
            return self.evaluate_board()

        if maximizing_player:
            max_eval = float('-inf')
            possible_moves = self.get_possible_moves()
            for move in possible_moves:
                self.make_move(move)
                eval = self.minimax(depth - 1, False)
                self.board[np.where(self.board[:, move] != 0)[0][0] - 1][move] = 0
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            possible_moves = self.get_possible_moves()
            for move in possible_moves:
                self.make_move(move)
                eval = self.minimax(depth - 1, True)
                self.board[np.where(self.board[:, move] != 0)[0][0] - 1][move] = 0
                min_eval = min(min_eval, eval)
            return min_eval

    def get_best_move(self):
        max_eval = float('-inf')
        best_move = None
        possible_moves = self.get_possible_moves()
        for move in possible_moves:
            self.make_move(move)
            eval = self.minimax(5, False)  # Adjust the depth as needed
            self.board[np.where(self.board[:, move] != 0)[0][0] - 1][move] = 0
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return best_move

    def play_game(self):
        while True:
            self.display_board()

            if self.current_player == 1:
                column = int(input(
                    f"{self.current_player}'s turn. Enter the column number (0-{self.columns - 1}): "))
                if self.is_valid_move(column):
                    self.make_move(column)
                else:
                    print("Invalid move. Please try again.")
                    continue
            else:
                column = self.get_best_move()
                self.make_move(column)
                print(f"AI chooses column {column}")

            if self.check_win():
                self.display_board()
                if self.current_player == 1:
                    print("Player 1 wins!")
                else:
                    print("AI wins!")
                break

            if self.is_full():
                self.display_board()
                print("It's a tie!")
                break

            self.current_player = 2 if self.current_player == 1 else 1
            
game = Connect4()
game.play_game()