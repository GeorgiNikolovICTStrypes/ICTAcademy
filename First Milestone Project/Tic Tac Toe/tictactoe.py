class TicTacToe:
    def __init__(self, positions = [' ',' ',' ',' ',' ',' ',' ',' ',' ']):
        """
        Args: positions - an array of lenght 9
        Initializes a game state given a positions array.
        """
        self._positions = positions
        
    def _print_board(self):
        """
        Prints the board state.
        """
        print("   |   |   \n {} | {} | {} \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   ".format(*self._positions))

    def _check_state(self):
        """
        Check if a player has won the game or if it has ended.
        Returns: 1 if x won, 2 if o won and 0 if there is no winner.
        """
        # Check rows
        for i in range(3):
            if self._positions[i*3:i*3+3] == ['x','x','x']:
                return 1
            if self._positions[i*3:i*3+3] == ['o','o','o']:
                return 2
        # check columns
        for i in range(3):
            if self._positions[0+i] == self._positions[3+i] == self._positions[6+i] == 'x':
                return 1
            if self._positions[0+i] == self._positions[3+i] == self._positions[6+i] == 'o':
                return 2
        # Check main diag
        if self._positions[0] == self._positions[4] == self._positions[8] == 'x':
            return 1
        
        if self._positions[0] == self._positions[4] == self._positions[8] == '0':
            return 2

        # Check secondary diag
        if self._positions[2] == self._positions[4] == self._positions[6] == 'x':
            return 1
                
        if self._positions[2] == self._positions[4] == self._positions[6] == '0':
            return 2
        # if there is no winner on rows, cols and diags we just return 0 and board is full
        if all(pos != ' ' for pos in self._positions):
            return 0
        # else we can send -1 if we can keep making moves
        return -1

    def _make_move(self,player):
        """
        Args: player - char denotes which player is making the move (either x or o)
        User inputs a value in the range [1,9] and we change that position to equal
        The player symbol.
        """
        print(player)
        if player != 'x' and player != 'o':
            raise Exception("Please enter a valid player (either x or o)")
        
        move = int(input("Please enter an integer in the range [1,9]: "))
        if not (1 <= move <= 9):
            print("Move must be an integer in the range [1,9]!")
            self._make_move(player)

        if self._positions[move-1]!= ' ':
            print("Move must be on a free square!")
            self._make_move(player)

        self._positions[move-1] = player

    def _play_game(self):
        """
        Starts the game X is always first and players take turns
        Until there are no more valid moves.
        """
        turns = 0
        self._print_board()
        while self._check_state()==-1:
            if turns % 2 == 0:
                self._make_move(player='x')
            else:
                self._make_move(player='o')
            self._print_board()
            turns+=1
        result = self._check_state()
        if result == 1:
            print(f"Player 1 is the winner of this round. (X)\nThis round was {turns} turns long.")
            return 1
        if result == 2:
            print(f"Player 2 is the winner of this round. (O)\nThis round was {turns} turns long.")
            return 2

        print("Its a draw! There is no winner.")
        return 0
    def play(self):
        """
        This function starts a round of consecutive Tic Tac Toe games until the user enters
        Something other than YES when prompted.
        """
        first_result = self._play_game()
        x_wins = 0
        o_wins = 0
        draws = 0
        if first_result == 1:
            x_wins +=1
        if first_result == 2:
            o_wins += 2
        if first_result == 0:
            draws +=1
        while input("Would u like to play another round [YES/NO]: ") == "YES":
            self._positions = [' ']*9
            result =self._play_game()
            if result == 1:
                x_wins +=1
            if result == 2:
                o_wins +=1
            draws+=1

        print(f"The session ended! X won {x_wins} games, O won {o_wins} games, They ended {draws} games in a draw")