# Description: A Gess Game simulation with a Gess_Game class that stores the information of a game with methods to
# create the board, check for valid input, make moves, establish location of pieces, and resign games.  It also
# communicates with a Valid_Moves class that determines valid moves.

from Valid_Moves import *

class GessGame:
    """A class that stores the information of a Gess Game."""
    def __init__(self):
        """Creates a GessGame object with a board, game state, board columns, and board rows."""
        self._myboard = self.create_board()
        self._game_state = 'UNFINISHED'
        self._columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                         'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't']
        self._rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                      '12', '13', '14', '15', '16', '17', '18', '19', '20']
        self._player_turn = 'BLACK'
        self._b_value = 'b'
        self._w_value = 'w'

    def create_board(self):
        """
        Initializes a board for the game with starting
        positions of all pieces.
        :return: self._myboard with starting positions of 'w' and 'b'.
        """
        self._myboard = [['_' for row in range(20)] for column in range(20)]

        b_index_pieces = [[1, 2], [1, 4], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10],
                          [1, 11], [1, 12], [1, 13], [1, 15], [1, 17], [2, 1], [2, 2],
                          [2, 3], [2, 5], [2, 7], [2, 8], [2, 9], [2, 10], [2, 12],
                          [2, 14], [2, 16], [2, 17], [2, 18], [3, 2], [3, 4], [3, 6],
                          [3, 7], [3, 8], [3, 9], [3, 10], [3, 11],[3, 12], [3, 13],
                          [3, 15], [3, 17], [6, 2], [6, 5], [6, 8], [6, 11], [6, 14], [6, 17]]

        w_index_pieces = [[18, 2], [18, 4], [18, 6], [18, 7], [18, 8], [18, 9], [18, 10],
                          [18, 11], [18, 12], [18, 13], [18, 15],[18, 17], [17, 1], [17, 2],
                          [17, 3], [17, 5], [17, 7], [17, 8], [17, 9], [17, 10], [17, 12],
                          [17, 14],[17, 16], [17, 17], [17, 18], [16, 2], [16, 4], [16, 6],
                          [16, 7], [16, 8], [16, 9], [16, 10], [16, 11],[16, 12], [16, 13],
                          [16, 15], [16, 17], [13, 2], [13, 5], [13, 8], [13, 11], [13, 14],
                          [13, 17]]

        # Iterate through both lists to place initial pieces.
        for b_val in b_index_pieces:
            self._myboard[b_val[0]][b_val[1]] = 'b'
        for w_val in w_index_pieces:
            self._myboard[w_val[0]][w_val[1]] = 'w'
        return self._myboard

    def get_my_board(self):
        return self._myboard

    def get_game_state(self):
        return self._game_state

    def set_game_state(self, state):
        """Sets the current state of the game."""
        if state == "UNFINISHED" or state == "BLACK_WON" or state == "WHITE_WON":
            self._game_state = state

    def get_player_turn(self):
        return self._player_turn

    def set_player_turn(self):
        """Sets the player turn to opposing player."""
        if self.get_player_turn() == 'BLACK':
            self._player_turn = 'WHITE'
        else:
            self._player_turn = 'BLACK'

    def get_player_val(self):
        """Returns the value of current player."""
        if self.get_player_turn() == 'BLACK':
            return self._b_value
        else:
            return self._w_value

    def print_board(self):
        """Prints the GessGame board with column and row labels."""
        # Iterate through self._columns and add spacing.
        for c in self._columns:
            if c == "a":
                print(("   ") + str(c), end="")
            else:
                print("  " + str(c), end="")
        print()
        # Iterate through self._rows and add spacing
        for r in range(len(self._myboard) - 11):
            print(" " + str(self._rows[r]), end="")

            for i in self._myboard[r]:
                print(" " + str(i), end=" ")
            print()
        # Less spacing for double digit rows.
        for r in range(9, len(self._myboard)):
            print(str(self._rows[r]), end="")

            for i in self._myboard[r]:
                print(" " + str(i), end=" ")
            print()

    def translate(self, val):
        """
        Translates user input of a piece to its corresponding
        index value for row or column from values stored in self._columns or
        self._rows.
        :return: Index value of corresponding row or column.
        """
        # Get column index.
        for col_val in self._columns:
            if col_val == val:
                col = self._columns.index(col_val)
                return col
        # Get row index.
        for row_val in self._rows:
            if row_val == val:
                row = self._rows.index(row_val)
                return row

    def foot_values(self, row, col):
        """
        Stores the values associated with the coordinates of the
        starting footprint.
        :return: List of values in the starting footprint.
        """
        board = self._myboard
        # Establish list of footprint around starting row and column.
        footprint = [board[row][col], board[row + 1][col],
                     board[row + 1][col + 1], board[row + 1][col - 1],
                     board[row - 1][col], board[row - 1][col + 1],
                     board[row - 1][col - 1], board[row][col + 1],
                     board[row][col - 1]]
        return footprint

    def get_footprint(self, row, col):
        """
        Creates the location of the footprint of each
        piece by adding or subtracting to the starting center of a piece.
        :return: List of locations of the footprint.
        """
        # Check that footprint is within range on board.
        if row < 1 or row > 18 or col < 1 or col > 18:
            return False

        # Establish list of footprint around row and column.
        footprint = [[row, col], [row + 1, col], [row + 1, col + 1],
                     [row + 1, col - 1], [row - 1, col],
                     [row - 1, col + 1], [row - 1, col - 1],
                     [row, col + 1], [row, col - 1]]
        return footprint

    def move_footprint(self, start_row, start_col, end_row, end_col, temp_board):
        """
        Moves the footprint of the starting piece to the
        footprint of the ending piece if valid move established.
        """
        board = self._myboard
        # Calculate distance between start and end coordinates.
        slope_row = end_row - start_row
        slope_col = end_col - start_col

        # Copy value at footprint from temp_board to end footprint.
        for val in self.get_footprint(start_row, start_col):
            value = temp_board[val[0]][val[1]]
            self._myboard[val[0] + slope_row][val[1] + slope_col] = value

        # Clear values of outer columns and rows.
        for val in range(0, 20):
            board[0][val] = "_"
            board[19][val] = "_"
            board[val][0] = "_"
            board[val][19] = "_"

        # Clear area of starting footprint not in ending footprint.
        for val in self.get_footprint(start_row, start_col):
            if val not in self.get_footprint(end_row, end_col):
                board[val[0]][val[1]] = "_"

    def make_move(self, start, end):
        """
        A driver method that validates user input, calls to translate to translate
        input, communicates with Piece class to get valid moves,
        calls to opposing pieces check, calls to move_footprint to move
        the piece,calls to ring_check to ensure the current player cannot
        make a move where they lose a ring and to check for a win, updates
        player turn, and prints the game board.
        :return: False if move is not legal or if game won, else True.
        """
        # Check if game over.
        if self.get_game_state() != 'UNFINISHED':
            return "GAME OVER"
        # Check that user input is valid.
        if start[0].lower() not in self._columns or\
                end[0].lower() not in self._columns:
            return "Invalid Coordinate - Try Again"
        if start[1:].lower() not in self._rows or \
                end[1:].lower() not in self._rows:
            return "Invalid Coordinate - Try Again"

        # Translate user input to row and column coordinates.
        start_col = self.translate(start[0])
        start_row = self.translate(start[1:])
        end_col = self.translate(end[0])
        end_row = self.translate(end[1:])

        # Establish communication with Piece class and create temp board.
        piece = Valid_Moves(start_row, start_col, end_row, end_col)
        temp_board = []
        for i in self._myboard:
            temp_board.append(list(i))
        valid_moves = piece.valid_moves(self.get_player_val(), temp_board)

        if not self.opposing_pieces_check(start_row, start_col):
            return "Invalid - Opposing Pieces in Footprint"

        # Check end coordinates valid.
        if [end_row, end_col] not in valid_moves:
            return "Invalid Move - Try again"
        self.move_footprint(start_row, start_col, end_row, end_col, temp_board)

        # If current player loses a ring, move is not valid.
        # If opposing player loses a ring, game won by current player.
        if self.get_player_turn() == 'BLACK':
            if self.ring_check('w') == []:
                self.set_game_state('BLACK_WON')
            else:
                if self.ring_check('b') == []:
                    return "Invalid Move - Ring Lost - Try Again"
        else:
            if self.ring_check('b') == []:
                self.set_game_state('WHITE_WON')
            else:
                if self.ring_check("w") == []:
                    return "Invalid Move - Ring Lost - Try Again"
        self.set_player_turn()
        self.print_board()
        return "Valid Move"

    def opposing_pieces_check(self, row, col):
        """
        Checks for opposing player pieces in the
        footprint of the current player's piece.
        :return: False if opposing player value found in current player
                piece footprint, else True.
        """
        # Check for 'w' in 'BLACK' footprint.
        if self.get_player_turn() == "BLACK":
            for val in self.foot_values(row, col):
                if val == "w":
                    return False
            return True
        # Check for 'b' in 'WHITE' footprint.
        if self.get_player_turn() == "WHITE":
            for val in self.foot_values(row, col):
                if val == "b":
                    return False
            return True

    def ring_check(self, player):
        """
        Checks for the presence of a ring for both players'
        pieces by scanning the board and treating each coordinate as a
        center of a piece.
        :return: Return a list of coordinates for where a ring is present
                on the board for a designated player.
        """
        board = self._myboard
        ring_list = []

        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                # Check each empty space for ring of player values surrounding it.
                if col == "_" and col_index < 19 and col_index > 1 and \
                    row_index < 19 and row_index > 1:
                    # If a ring is found, add the coordinates to ring_list.
                    if board[row_index + 1][col_index] == \
                        board[row_index + 1][col_index + 1] == \
                        board[row_index + 1][col_index - 1] == \
                        board[row_index - 1][col_index] == \
                        board[row_index - 1][col_index + 1] == \
                        board[row_index - 1][col_index - 1] == \
                        board[row_index][col_index + 1] == \
                        board[row_index][col_index - 1] == player:
                        ring_list.append([row_index, col_index])
        return ring_list

    def resign_game(self):
        """
        Resigns the game for a player by referring
        to the current player turn and sets game state to
        opposing player winning.
        :return: Game state after player resigns.
        """
        # Check for player turn and assign opposing player as winner.
        if self._player_turn == "BLACK":
            self.set_game_state("WHITE_WON")
        else:
            self.set_game_state("BLACK_WON")
        return self.get_game_state()

def main():
    gess_game = GessGame()
    gess_game.print_board()
    while gess_game.get_game_state() == "UNFINISHED":
        print("Current Turn: " + gess_game.get_player_turn())
        start = input("Enter starting coordinate: ")
        end = input("Enter ending coordinate: ")
        print(gess_game.make_move(start, end))

if __name__ == '__main__':
    main()


