
class Valid_Moves:
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
        return self.move_length(player, valid, current)

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