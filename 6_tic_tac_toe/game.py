class TicTacToe:
    #we create the game board here
    def __init__(self):
        self.board = [' ' for _ in range(9)] #we will use a single list to rep 3x3 board
        self.current_winner = None # keep track of the winner

    def print_board(self):
        #this is just getting the rows
        for row in [self.board[(i*3):(i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' |')

    #this is the result for now:
    #  |   |   |   |
    #  |   |   |   |
    #  |   |   |   |

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' |')

    # this is the result for now:
    #  | 0 | 1 | 2 |
    #  | 3 | 4 | 5 |
    #  | 6 | 7 | 8 |

    def avaliable_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move then make the move(assing square to letter)
        #then return true, if invalid return false
        if self.board[square] = ' ':
            self.board[square] = letter
            return True
        return False




def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    #iterate while the game still has empty squares
    #(we dont have to worry about winner because we will just return that
    #which breaks the loop)
    while game.empty_squares():
        #get the move from the appropriate player
        if letter == 'O':
            square = o_player.choose_move(game)
        else:
            square = x_player.choose_move(game)

        # let's define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square {} ')
                game.print_board()
                print('') # just an empty line


