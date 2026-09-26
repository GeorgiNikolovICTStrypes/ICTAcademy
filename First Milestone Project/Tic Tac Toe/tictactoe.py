class TicTacToe:
    def __init__(self, positions = [' ',' ',' ',' ',' ',' ',' ',' ',' ']):
        """
        Args: positions - an array of lenght 9
        Initializes a game state given a positions array.
        """
        self.__positions = positions
        
    def __print_board(self):
        """
        Prints the board state.
        """
        print("   |   |   \n {} | {} | {} \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   ".format(*self.__positions))

    def __check_state(self):
        """
        Check if a player has won the game or if it has ended.
        Returns: 1 if x won, 2 if o won and 0 if there is no winner.
        """
        # Check rows
        for i in range(3):
            if self.__positions[i*3:i*3+3] == ['x','x','x']:
                return 1
            if self.__positions[i*3:i*3+3] == ['o','o','o']:
                return 2
        # check columns
        for i in range(3):
            if self.__positions[0+i] == self.__positions[3+i] == self.__positions[6+i] == 'x':
                return 1
            if self.__positions[0+i] == self.__positions[3+i] == self.__positions[6+i] == 'o':
                return 2
        # Check main diag
        if self.__positions[0] == self.__positions[4] == self.__positions[8] == 'x':
            return 1
        
        if self.__positions[0] == self.__positions[4] == self.__positions[8] == '0':
            return 2

        # Check secondary diag
        if self.__positions[2] == self.__positions[4] == self.__positions[6] == 'x':
            return 1
                
        if self.__positions[2] == self.__positions[4] == self.__positions[6] == '0':
            return 2
        # if there is no winner on rows, cols and diags we just return 0 and board is full
        if all(pos != ' ' for pos in self.__positions):
            return 0
        # else we can send -1 if we can keep making moves
        return -1

    def __make_move(self,player):
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
            self.__make_move(player)

        if self.__positions[move-1]!= ' ':
            print("Move must be on a free square!")
            self.__make_move(player)

        self.__positions[move-1] = player

    def play_game(self):
        """
        Starts the game X is always first and players take turns
        Until there are no more valid moves.
        """
        turns = 0
        self.__print_board()
        while self.__check_state()==-1:
            if turns % 2 == 0:
                self.__make_move(player='x')
            else:
                self.__make_move(player='o')
            self.__print_board()
            turns+=1
        result = self.__check_state()
        if result == 1:
            print(f"Player 1 is the winner of this round. (X)\nThis round was {turns} turns long.")
            return
        if result == 2:
            print(f"Player 2 is the winner of this round. (O)\nThis round was {turns} turns long.")
            return

        print("Its a draw! There is no winner.")
        