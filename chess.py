class Chess(object):
    # All possible values for board
    EMPTY = '[ ]' 

    BLACK_PAWN = '[p]'
    BLACK_KING = '[k]'
    BLACK_QUEEN = '[q]'
    BLACK_BISHOP = '[b]'
    BLACK_KNIGHT = '[h]'
    BLACK_ROOK = '[r]'

    WHITE_PAWN = '[P]'
    WHITE_KING = '[K]'
    WHITE_QUEEN = '[Q]'
    WHITE_BISHOP = '[B]'
    WHITE_KNIGHT = '[H]'
    WHITE_ROOK = '[R]' 
    
    # Coloured lists of pieces
    BLACK_PIECES = (BLACK_PAWN, BLACK_KING, BLACK_QUEEN, BLACK_BISHOP, BLACK_KNIGHT,
            BLACK_ROOK)
    WHITE_PIECES = (WHITE_PAWN, WHITE_KING, WHITE_QUEEN, WHITE_BISHOP, WHITE_KNIGHT,
            WHITE_ROOK)

    # List of pawn pieces
    PAWNS = (WHITE_PAWN, BLACK_PAWN)

    # Turn values
    WHITE = 0
    BLACK = 1


    def __init__(self):
        self.board = [['[ ]']*8 for x in xrange(8)]
        # Pieces white has captured
        self.white_captured = []
        # Pieces black has captured
        self.black_captured = []

        self.moved_pawns = []

    # Resets game board
    def start(self):
        """
        Resets board and captured pieces.
        """
        self.white_captured = []
        self.black_captured = []

        start_board = self.board[:]
        for i in range(0, 8):
            start_board[i][1], start_board[i][6] = self.WHITE_PAWN, self.BLACK_PAWN

        start_board[0][0], start_board[7][0] = self.WHITE_ROOK, self.WHITE_ROOK
        start_board[0][7], start_board[7][7] = self.BLACK_ROOK, self.BLACK_ROOK

        start_board[1][0], start_board[6][0] = self.WHITE_KNIGHT, self.WHITE_KNIGHT
        start_board[1][7], start_board[6][7] = self.BLACK_KNIGHT, self.BLACK_KNIGHT

        start_board[2][0], start_board[5][0] = self.WHITE_BISHOP, self.WHITE_BISHOP
        start_board[2][7], start_board[5][7] = self.BLACK_BISHOP, self.BLACK_BISHOP

        start_board[3][0], start_board[3][7] = self.WHITE_QUEEN, self.BLACK_QUEEN
        start_board[4][0], start_board[4][7] = self.WHITE_KING, self.BLACK_KING

        self.board = start_board

    # Checks if move valid
    def check_move(self, turn, coords1, coords2):
        """
        coords1: Tuple of (int,int), both ints valid indices of board; from place
        coords2: Tuple of (int,int), both ints valid indices of board; to place
        
        Checks if move is valid.
        """
        def pawn(coords1, coords2):
            # Checks if move is forwards
            if coords2[1]-coords1[1] < 0 and piece == self.WHITE_PAWN:
                return False
            if coords2[1]-coords1[1] > 0 and piece == self.BLACK_PAWN:
                return False

            # Checks if piece in movement path
            x = coords1[1]+1
            # <= because pawns can't capture forwards
            while x <= coords2[1]:
                if self.board[coords1[0]][x] != self.EMPTY:
                    return False
                else:
                    x += 1

            # Checks if pawn can make "capture" move (diagnol)
            if abs(coords1[0]-coords2[0]) == 1 and abs(coords1[1]-coords2[1]) == 1:
                if self.board[coords2[0]][coords2[1]] == self.EMPTY:
                    return False 
            # Checks if move along y-axis
            else:
                if coords1[0]-coords2[0] != 0:
                    return False


            # Checks if pawn can move 2 squares
            if abs(coords1[1]-coords2[1]) > 1 and coords1 in self.moved_pawns:
                return False

            # If pawn can move 2, checks if moves more than 2 
            if coords1 not in self.moved_pawns:
                if abs(coords1[1]-coords2[1]) > 2:
                    return False
            # If pawn can't move 2, checks if moves more than 1
            else:
                if abs(coords1[1]-coords2[1]) > 1:
                    return False

            return True

        def rook(coords1, coords2):
            # Checks if path is clear depending on move direction
            # x-axis path
            if coords1[0]-coords2[0] == 0:
                x = coords1[1]+1
                while x < coords2[1]:
                    if self.board[coords1[0]][x] != self.EMPTY:
                        return False
                    else:
                        x += 1
            # y-axis path
            elif coords1[1]-coords2[1] == 0:
                x = coords1[0]+1
                while x < coords2[0]:
                    if self.board[x][coords1[1]] != self.EMPTY:
                        return False
                    else:
                        x += 1

            # Ensures move is only along one axis
            if coords1[0]-coords2[0] != 0 and coords1[1]-coords2[1] != 0:
                return False
            
            return True

        def knight(coords1, coords2):
            x_delta = abs(coords1[0]-coords2[0])
            y_delta = abs(coords1[1]-coords2[1])

            if y_delta == 2 and x_delta == 1:
                return True

            elif y_delta == 1 and x_delta == 2:
                return True

            return False

        def bishop(coords1, coords2):
            # Checks if move is diagnol
            if abs(coords1[0]-coords2[0]) != abs(coords1[1]-coords2[1]):
                print "not diagnol"
                print "diag check", abs(coords1[0]-coords2[0]) != abs(coords1[1]-coords2[1])

                return False

            # Checks if path is empty
            x = coords1[0]+1
            y = coords2[0]+1
            while x < coords2[1] or y < coords2[1]:
                if self.board[x][y] != self.EMPTY:
                    print "path not empty"
                    return False
                else:
                    x += 1
                    y += 1

            return True

        def queen(coords1, coords2):
            # Checks if valid using bishop and rook
            return bishop(coords1, coords2) or rook(coords1, coords2)

        def king(coords1, coords2):
            # Checks if move less than 2 squares
            if abs(coords1[0]-coords2[0]) > 1 or abs(coords1[1]-coords2[1]) > 1:
                return False

            # Checks if valid  using queen
            return queen(coords1, coords2)

        piece = self.board[coords1[0]][coords1[1]]

        if turn == self.BLACK and piece not in self.BLACK_PIECES:
            return False
        if turn == self.WHITE and piece not in self.WHITE_PIECES:
            return False

        if piece == self.WHITE_PAWN or piece == self.BLACK_PAWN:
            return pawn(coords1, coords2)
        elif piece == self.WHITE_ROOK or piece == self.BLACK_ROOK:
            return rook(coords1, coords2)
        elif piece == self.WHITE_KNIGHT or piece == self.BLACK_KNIGHT: 
            return knight(coords1, coords2)
        elif piece == self.WHITE_BISHOP or piece == self.BLACK_BISHOP:
            return bishop(coords1, coords2)
        elif piece == self.WHITE_QUEEN or piece == self.BLACK_QUEEN:
            return queen(coords1, coords2)
        elif piece == self.WHITE_KING or piece == self.BLACK_KING:
            return king(coords1, coords2) 
        else:
            return False

    # Checks if valid, then moves. Also checks for captures
    def move(self, turn, coords1, coords2):
        """
        coords1: Tuple of (int,char); from space
        coords2: Tuple of (int,char); to space
        
        Moves pieces.
        """
        invalid_move = "Invalid move."
        invalid_piece = "That is not your piece."

        if coords2[0] > 'h' or coords2[1] > 8:
            return invalid_move

        # sets coords to array values (eg. 1 -> 0, 'a' -> 0)
        coords1 = (ord(coords1[0])-ord('a'), coords1[1]-1)
        coords2 = (ord(coords2[0])-ord('a'), coords2[1]-1)

        if self.check_move(turn, coords1, coords2):
            # if pawn, adds to moved pawn list
            if self.board[coords1[0]][coords2[1]] in self.PAWNS:
                self.moved_pawns.append(coords1)

            if self.board[coords2[0]][coords2[1]] != self.EMPTY:
                if turn == self.WHITE:
                    if self.board[coords2[0]][coords2[1]] in self.WHITE_PIECES:
                        return invalid_move

                    else:
                        self.white_captured.append(self.board[coords2[0]][coords2[1]])
                elif turn == self.BLACK:
                    if self.board[coords2[0]][coords2[1]] in self.BLACK_PIECES:
                        return invalid_move

                    else:
                        self.black_captured.append(self.board[coords2[0]][coords2[1]]) 
            self.board[coords2[0]][coords2[1]] = self.board[coords1[0]][coords1[1]]
            self.board[coords1[0]][coords1[1]] = self.EMPTY

        else:
            return invalid_move

        return self.__str__() 

    def get_captured(self, colour):
        """
        colour: str, colour of player's captured pieces.

        Assumes colour is valid.
        """
        if colour == "white":
            return len(self.white_captured)
        elif colour == "black":
            return len(self.black_captured)


    def __str__(self):
        output = ''

        capped = ''
        capped += "\nCapped: "
        for x in self.white_captured:
            if len(capped)%25 == 0:
                capped += "\n"
            capped += x.strip("[]")
        capped += "\n\n"

        output += capped

        output += "   a  b  c  d  e  f  g  h"
        for k in range(len(self.board)):
            output += "\n%d " % (k+1)
            for j in range(len(self.board[k])):
                output += self.board[j][k]

        capped = ''
        capped += "\n\nCapped: "
        for x in self.black_captured:
            if len(capped)%25 == 0:
                capped += "\n"
            capped += x.strip("[]")
        capped += "\n"
        
        output += capped
        
        return output

class Engine():
    def __init__(self):
        print "Welcome to a commandline interface version of chess!"
        print
        print "Player 1 is White, Player 2 is Black."
        print "White pieces are uppercase, black pieces are lowercase."
        print
        print "Input moves as <from> <to> (eg. a2 a3)."
        print "Type 'quit' to quit."
        print "If you need help at anytime, try 'help'!"
        print
        print "Read the README for more info!"
        self.game = Chess()

    def parse_input(self, move):
        if move == "help":
            return "help"
        elif move == "quit":
            return "quit"
        else:
            move = move.split()
            if len(move) > 1:
                if len(move[0]) >  1 and len(move[1]) > 1:
                    coords1 = (move[0][0], int(move[0][1]))
                    coords2 = (move[1][0], int(move[1][1]))
                    return (coords1, coords2)
            
    def play(self):
        stop = False
        turn = -1

        print self.game
        while not stop:
            turn += 1

            valid = False
            while not valid:
                move = raw_input("Player %d > " % ((turn%2)+1))
                coords = self.parse_input(move)

                # Interprets input
                if type(coords) is tuple:
                        output = self.game.move(turn%2, coords[0], coords[1])
                        print output

                        if output == self.game.__str__():
                            valid = True

                if coords == None:
                    print "Input invalid, type 'help' for help"
                elif coords == "help":
                    print "Enter move as <from letter><from number>" \
                            "<to letter><to number>"
                    print "eg. a3 a5"
                    print
                    print "Type 'quit' to quit"
                elif coords == 'quit':
                    valid = True
                    stop = True

            # Checks if anyones captured all the pieces
            if self.game.get_captured("white") >= 16:
                print "Player 1 wins!"
                stop = True

            elif self.game.get_captured("black") >= 16:
                print "Player 2 wins!"
                stop = True

        print "Turns played: %d" % turn
        play_again = raw_input("Would you like to play again? (y/n) ")
        while True:
            if play_again in 'yesYes':
                self.start()
            elif play_again in 'noNo':
                print "Thanks for playing!"
                exit(0)
            else:
                print "Not valid, yes or no?"
        
    def start(self):
        self.game.start()
        self.play()

engine = Engine()
engine.start()
