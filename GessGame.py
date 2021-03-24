# Description: A GessGame simulation with a GessGame class that stores the information of a game with methods to
# create the board, check for valid input, make moves, establish location of pieces, and resign games.  It also
# communicates with a Piece class that determines valid moves.

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
        A method that initializes a board for the game with starting
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
        """Returns current state of the GessGame board."""
        return self._myboard

    def get_game_state(self):
        """Returns the current state of the game."""
        return self._game_state

    def set_game_state(self, state):
        """Sets the current state of the game to 'UNFINISHED', 'BLACK_WON', or 'WHITE_WON'."""
        if state == "UNFINISHED" or state == "BLACK_WON" or state == "WHITE_WON":
            self._game_state = state
        return

    def get_player_turn(self):
        """A method that returns the current player turn."""
        return self._player_turn

    def set_player_turn(self):
        """A method that sets the player turn to opposing player."""
        if self.get_player_turn() == 'BLACK':
            self._player_turn = 'WHITE'
        else:
            self._player_turn = 'BLACK'

    def get_player_val(self):
        """A method that returns the value of current player."""
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
        A method that translates user input of a piece to its corresponding
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
        A method that stores the values associated with the coordinates of the
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
        A method that creates the location of the footprint of each
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
        A method that moves the footprint of the starting piece to the
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
        A method that validates user input, calls to translate to translate
        input, communicates with Piece class to get valid moves,
        calls to opposing pieces check, calls to move_footprint to move
        the piece,calls to ring_check to ensure the current player cannot
        make a move where they lose a ring and to check for a win, updates
        player turn, and prints the game board.
        :return: False if move is not legal or if game won, else True.
        """
        # Check if game over.
        if self.get_game_state() != 'UNFINISHED':
            return False
        # Check that user input is valid.
        if start[0].lower() not in self._columns or\
                end[0].lower() not in self._columns:
            return False
        if start[1:].lower() not in self._rows or \
                end[1:].lower() not in self._rows:
            return False

        # Translate user input to row and column coordinates.
        start_col = self.translate(start[0])
        start_row = self.translate(start[1:])
        end_col = self.translate(end[0])
        end_row = self.translate(end[1:])

        # Establish communication with Piece class and create temp board.
        piece = Piece(start_row, start_col, end_row, end_col)
        temp_board = []
        for i in self._myboard:
            temp_board.append(list(i))
        valid_moves = piece.valid_moves(self.get_player_val(), temp_board)

        if not self.opposing_pieces_check(start_row, start_col):
            return False

        # Check end coordinates valid.
        if [end_row, end_col] in valid_moves:
            self.move_footprint(start_row, start_col, end_row, end_col, temp_board)
        else:
            return False

        # If current player loses a ring, move is not valid.
        # If opposing player loses a ring, game won by current player.
        if self.get_player_turn() == 'BLACK':
            if self.ring_check('w') == []:
                self.set_game_state('BLACK_WON')
            else:
                if self.ring_check('b') == []:
                    return False
        else:
            if self.ring_check('b') == []:
                self.set_game_state('WHITE_WON')
            else:
                if self.ring_check("w") == []:
                    return False
        self.set_player_turn()
        self.print_board()
        return True

    def opposing_pieces_check(self, row, col):
        """
        A method that checks for opposing player pieces in the
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
        A method that checks for the presence of a ring for both players'
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
        A method that resigns the game for a player by referring
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


class Piece:
    """A class that stores the valid moves of a Piece declared by a player."""
    def __init__(self, start_row, start_col, end_row, end_col):
        """Creates a Piece object with a start row, start column, end row end column, and
           list of valid moves."""
        self._start_row = start_row
        self._start_col = start_col
        self._end_row = end_row
        self._end_col = end_col

    def valid_moves(self, player, current):
        """
        A method that uses the location of the footprint of the starting
        piece to call to other methods to determine valid moves on the board.
        Calls move_length to edit list according to allowed move length.
        :return: List of valid moves.
        """
        row = self._start_row
        col = self._start_col
        valid = []

        # Bottom center.
        if current[row + 1][col] == player:
            self.valid_down_center(row, col, current, valid)
        # Lower right diagonal.
        if current[row + 1][col + 1] == player:
            self.valid_down_right_diag(row, col, current, valid)
        # Lower left diagonal.
        if current[row + 1][col - 1] == player:
            self.valid_down_left_diag(row, col, current, valid)
        # Upper center.
        if current[row - 1][col] == player:
            self.valid_up_center(row, col, current, valid)
        # Upper right diagonal.
        if current[row - 1][col + 1] == player:
            self.valid_up_right_diag(row, col, current, valid)
        # Upper left diagonal.
        if current[row - 1][col - 1] == player:
            self.valid_up_left_diag(row, col, current, valid)
        # Right center.
        if current[row][col + 1] == player:
            self.valid_right(row, col, current, valid)
        # Left center.
        if current[row][col - 1] == player:
            self.valid_left(row, col, current, valid)
        return self.move_length(player, valid, temp_board)

    def valid_down_center(self, row, col, current, valid):
        """
        A method that appends all valid down moves
        to list of valid moves.
        """
        valid.append([row + 1, col])
        inc = 1

        # Loop to in move down direction to find open spaces.
        while current[(row + 1) + inc][col] == \
                current[(row + 1) + inc][col + 1] == \
                current[(row + 1) + inc][col - 1] == "_" \
                and ((row + 1) + inc) < 19:
            # Add open space coordinates to valid list and increment for next loop.
            valid.append([(row + 1) + inc, col])
            inc += 1
        return

    def valid_down_right_diag(self, row, col, current, valid):
        """
        A method that appends all valid lower right hand diagonal
        moves to list of valid moves.
        """
        valid.append([row + 1, col + 1])
        inc = 1

        # Loop to in diagonal down and right direction to find open spaces.
        while current[(row + 1) + inc][(col + 1) + inc] == \
                current[(row + 1) + inc][col + inc] == \
                current[row + inc][(col + 1) + inc] == \
                current[(row + 1) + inc][col] == \
                current[row][(col + 1) + inc] == "_" \
                and ((row + 1) + inc) < 19 and ((col + 1) + inc) < 19:
            # Add open space coordinates to valid list and increment for next loop.
            valid.append([(row + 1) + inc, (col + 1) + inc])
            inc += 1
        return

    def valid_down_left_diag(self, row, col, current, valid):
        """
        A method that appends all valid lower left hand diagonal
        moves to list of valid moves.
        """
        valid.append([row + 1, col - 1])
        inc = 1

        # Loop to in diagonal down and left direction to find open spaces.
        while current[(row + 1) + inc][(col - 1) - inc] == \
                current[(row + 1) + inc][col - inc] == \
                current[row + inc][(col - 1) - inc] == \
                current[row][(col - 1) - inc] == \
                current[(row + 1) + inc][col] == "_" \
                and ((row + 1) + inc) < 19 and ((col - 1) - inc) > 0:
            # Add open space coordinates to valid list and increment for next loop.
            valid.append([(row + 1) + inc, (col - 1) - inc])
            inc += 1
        return

    def valid_up_center(self, row, col, current, valid):
        """
        A method that appends all valid up moves
        to list of valid moves.
        """
        valid.append([row - 1, col])
        inc = 1

        # Loop to in move up direction to find open spaces.
        while current[(row - 1) - inc][col] == \
                current[(row - 1) - inc][col + 1] == \
                current[(row - 1) - inc][col - 1] == "_" \
                and ((row - 1) - inc) > 0:
            # Add open space coordinates to valid list and increment for next loop.
            valid.append([(row - 1) - inc, col])
            inc += 1
        return

    def valid_up_right_diag(self, row, col, current, valid):
        """
        A method that appends all valid upper right hand diagonal
        moves to list of valid moves.
        """
        valid.append([row - 1, col + 1])
        inc = 1

        # Loop to in diagonal up and right direction to find open spaces.
        while current[(row - 1) - inc][(col + 1) + inc] == \
                current[row - inc][(col + 1) + inc] == \
                current[(row - 1) - inc][col + inc] == \
                current[(row - 1) - inc][col] == \
                current[row][(col + 1) + inc] == "_" \
                and ((row - 1) - inc) > 0 and ((col + 1) + inc) < 19:
            # Add open space coordinates to valid list and increment for next loop.
            valid.append([(row - 1) - inc, (col + 1) + inc])
            inc += 1
        return

    def valid_up_left_diag(self, row, col, current, valid):
        """
        A method that appends all valid upper left hand diagonal
        moves to list of valid moves.
        """
        valid.append([row - 1, col - 1])
        inc = 1

        # Loop to in diagonal up and left direction to find open spaces.
        while current[(row - 1) - inc][(col - 1) - inc] == \
                current[row - inc][(col - 1) - inc] == \
                current[(row - 1) - inc][col - inc] == \
                current[(row - 1) - inc][col] == \
                current[row][(col - 1) - inc] == "_" \
                and ((row - 1) - inc) > 0 and ((col - 1) - inc) > 0:
            # Add open space coordinates to valid list and increment for next loop.
            valid.append([(row - 1) - inc, (col - 1) - inc])
            inc += 1
        return

    def valid_right(self, row, col, current, valid):
        """
        A method that appends all valid right moves
        to list of valid moves.
        """
        valid.append([row, col + 1])
        inc = 1

        # Loop to in move right direction to find open spaces.
        while current[row][(col + 1) + inc] == \
                current[row + 1][(col + 1) + inc] == \
                current[row - 1][(col + 1) + inc] == "_" \
                and ((col + 1) + inc) < 19:
            # Add open space coordinates to valid list and increment for next loop.
            valid.append([row, (col + 1) + inc])
            inc += 1
        return

    def valid_left(self, row, col, current, valid):
        """
        A method that appends all valid left moves
        to list of valid moves.
        """
        valid.append([row, col - 1])
        inc = 1

        # Loop to in move left direction to find open spaces.
        while current[row][(col - 1) - inc] == \
                current[row + 1][(col - 1) - inc] == \
                current[row - 1][(col - 1) - inc] == "_" \
                and ((col - 1) - inc) > 0:
            # Add open space coordinates to valid list and increment for next loop.
            valid.append([row, (col - 1) - inc])
            inc += 1
        return

    def move_length(self, player, valid_list, current):
        """
        A method that determines the valid length of a move by a player.
        :return: List of valid moves within allowed move length.
        """
        valid_copy = []
        valid_index = []

        # Check for player value not in center of footprint.
        if current[self._start_row][self._start_col] != player:
            # Add moves within range of 3 to valid_copy.
            for value in valid_list:
                if abs(self._start_row - value[0]) <= 3 and abs(value[1] - self._start_col) <= 3:
                    valid_copy.append(value)
        else:
            # Add each move to valid_copy.
            for value in valid_list:
                valid_copy.append(value)

        # Check for moves within legal range of board and add to valid_index.
        for value in valid_copy:
            if value[0] > 0 and value[0] < 19 and value[1] > 0 and value[1] < 19:
                valid_index.append(value)
        return valid_index


def main():
    gess_game = GessGame()
    gess_game.print_board()
    gess_game.get_game_state()

    print(gess_game.make_move('e3', 'e6'))
    print(gess_game.get_player_turn())
    print(gess_game.make_move('r18', 's18'))
    print(gess_game.make_move('e6', 'e9'))
    print(gess_game.make_move('f15', 'f12'))
    print(gess_game.get_player_turn())
    print(gess_game.make_move('c3', 'c5'))
    print(gess_game.make_move('o18', 'q16'))
    print(gess_game.make_move('h3', 'e6'))
    print(gess_game.get_game_state())

if __name__ == '__main__':
    main()


