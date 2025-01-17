"""
Tic Tac Toe Player
"""

class Minimax:
    X = "X"
    O = "O"
    EMPTY = None
    
    def __init__(self):
        """
        Returns starting board of the board.
        """

        self.AI = None
        self.user = None
        self.board = [[None, None, None],
                [None, None, None],
                [None, None, None]]
        
    def player(self, board):
        """
        Returns player who has the next turn on a board.
        """
        MOVES = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != None: 
                    MOVES += 1
        
        if MOVES % 2 != 0: return self.AI
        else: return self.user

    def actions(self, search_board):
        """
        Returns set of all possible actions (i, j) available on the board.
        """
        actions = []
        for i in range(3):
            for j in range(3):
                if search_board[i][j] == None:
                    actions.append((i, j))
        return actions
        
    def result(self, search_board, action):
        """
        Returns the board that results from making move (i, j) on the board.
        """

        search_board[action[0]][action[1]] = self.player(search_board)
        return search_board

    def winner(self, search_board):
        """
        Returns the winner of the game, if there is one.
        """
        # [0][0] check (top straight and vertical right)
        if (search_board[0][0] == search_board[0][1] and search_board[0][1] == search_board[0][2] and search_board[0][0] != None) or (search_board[0][0] == search_board[1][0] and search_board[1][0] == search_board[2][0] and search_board[0][0] != None):
            return search_board[0][0]
        
        # [1][1] check (middle straight, vertical middle, and diagonals)
        if (search_board[0][0] == search_board[1][1] and search_board[1][1] == search_board[2][2] and search_board[1][1] != None) or (search_board[0][2] == search_board[1][1] and search_board[1][1] == search_board[2][0] and search_board[1][1] != None) or (search_board[1][0] == search_board[1][1] and search_board[1][1] == search_board[1][2] and search_board[1][1] != None) or (search_board[0][1] == search_board[1][1] and search_board[1][1] == search_board[2][1] and search_board[1][1] != None):
            return search_board[1][1]
        
        # [2][2] check (bottom straight, and vertical left)
        if (search_board[2][0] == search_board [2][1] and search_board[2][1] == search_board[2][2] and search_board[2][2] != None) or (search_board[0][2] == search_board[1][2] and search_board[1][2] == search_board[2][2] and search_board[2][2] != None):
            return search_board[2][2]

        # No winner yet
        return None

    def terminal(self, search_board):
        """
        Returns True if game is over, False otherwise.
        """
        
        has_EMPTY = False
        for i in range(3):
            for j in range(3):
                if search_board[i][j] == None:
                    has_EMPTY = True
        
        if has_EMPTY == False: return True
        return False
        
    def utility(self, search_board):
        """
        Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
        """

        if self.winner(search_board) == self.AI: return 10
        if self.winner(search_board) == self.user: return -10
        if self.terminal(search_board): return 0
        return None

    def minimax(self, board):
        """
        Returns the optimal action for the current player on the board.
        """   
        search_board = [[],[],[]]
        for i in range(3):
            for j in board[i]:
                search_board[i].append(j)

        value = -inf
        best_move = None
        for action in self.actions(search_board):
            search_board[action[0]][action[1]] = self.AI
            move_value = self.funny(search_board, 0, False)
            search_board[action[0]][action[1]] = None

            if move_value > value: 
                value = move_value
                best_move = action

        print(f'ACTION: {best_move}')
        return best_move

    def funny(self, board, depth, AI_turn):
        '''
        returns the action for the optimal outcome for max user
        '''
        score = self.utility(board)
        if score == -10 or score == 0 or score == 10:
            return score

        if AI_turn:
            value = -inf

            for action in self.actions(board):
                board[action[0]][action[1]] = self.AI
                value = max(value, self.funny(board, depth+1, False)) # Plays every game out from that action                                                
                board[action[0]][action[1]] = None

            return value

        else:
            value = inf

            for action in self.actions(board): 
                board[action[0]][action[1]] = self.user
                value = min(value, self.funny(board, depth+1, True))
                board[action[0]][action[1]] = None

            return value

from numpy import inf