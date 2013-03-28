class Chess(object):
    # All possible values for board
    EMPTY = '[ ]' 

    WHITE_PAWN = '[p]'
    WHITE_KING = '[k]'
    WHITE_QUEEN = '[q]'
    WHITE_BISHOP = '[b]'
    WHITE_KNIGHT = '[h]'
    WHITE_ROOK = '[r]'

    BLACK_PAWN = '[P]'
    BLACK_KING = '[K]'
    BLACK_QUEEN = '[Q]'
    BLACK_BISHOP = '[B]'
    BLACK_KNIGHT = '[H]'
    BLACK_ROOK = '[R]' 


    def __init__(self):
        self.board = [['[ ]']*8 for x in xrange(8)]
        # Records captured pieces
        self.white_captured = ""
        self.black_captured = ""

    # Resets game board
    def start(self):
        """
        Resets board and captured pieces.
        """
        self.white_captured = ""
        self.black_captured = ""

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
    def check_move(self, coords1, coords2):
        """
        coords1: Tuple of (int,int), both ints valid indices of board; from place
        coords2: Tuple of (int,int), both ints valid indices of board; to place
        
        Checks if move is valid.
        """

        def pawn(coords1, coords2):
            # Checks if piece in movement path
            if coords1[0]-coords2[0] == 0:
                x = coords1[1]
                # <= because pawns can't capture forwards
                while x <= coords2[1][0]:
                    if self.board[coords1[0]][x] != self.EMPTY:
                        return False
                    else:
                        x += 1

            # Checks if pawn moves along x axis
            if coords1[0]-coords2[0] != 0:
                return False

            if self.board[coords2[0]][coords2[1]] != self.EMPTY:
                if not abs(coords1[0]-coords2[0]) < 2 \
                        or not abs(coords1[1]-coords[2]) < 2:
                    return False 

            # Checks if pawn can move 2 squares
            elif coords1[0] == 1 or coords1[0] == 6 and \
                    coords1 not in self.moved_pawns:
                if not abs(coords1[0]-coords2[0]) < 3:
                    return False

            # Checks if pawn moves less than 2 squares
            else:
                if not abs(coords1[0]-coords2[0]) < 2:
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
                    if self.board[coords1[1]][x] != self.EMPTY:
                        return False
                    else:
                        x += 1

            # Ensures move is only along one axis
            x_delta = coords1[0]-coords2[0]
            y_delta = coords1[1]-coords2[1]
            if coords1[0]-coords[2] != 0 and coords1[1]-coords2[1] != 0:
                print "not only one direction"
                return False
            
            return True

        def knight(coords1, coords2):
            if not abs(coords1[0]-coords2[0]) == 1 \
                    and not abs(coords1[1]-coords2[1]) == 2 \
                    or not abs(coords1[1]-coords2[1]) == 1 \
                    and not abs(coords1[0]-coords2[0]) == 2:
                return False

            return True

        def bishop(coords1, coords2):
            # Checks if move is diagnol
            if abs(coords1[0]-coords2[0]) != abs(coords1[1]-coords2[1]):
                return False

            # Checks if path is empty
            x = coords1[0]+1
            y = coords2[0]+1
            while x < coords2[1] or y < coords2[1]:
                if self.board[x][y] != self.EMPTY:
                    return False
                else:
                    x += 1
                    y += 1

            return True

        def queen(coords1, coords2):
            # Checks if valid using bishop and rook
            return bishop(coords1, coords2) and rook(coords1, coords2)

        def king(coords1, coords2):
            # Checks if move less than 2 squares
            if abs(coords1[0]-coords2[0]) < 2 \
                    and abs(coords2[1]-coords2[1]) < 2:
                return False
            # Checks if valid  using queen
            return queen(coords1, coords2)


        if coords2[0] > 8 or coords2[1] > 'h':
            return False

        # Remove after move is implemented
        coords1 = (ord(coords1[0])-ord('a'), coord1[1]-1)
        coords2 = (ord(coords2[0])-ord('a'), coord2[1]-1)

        piece = self.board[coords1[0]][coords1[1]]

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
    def move(self, coords1, coords2):
        """
        coords1: Tuple of (int,char); from space
        coords2: Tuple of (int,char); to space
        
        Moves pieces.
        """
        # sets coords to array values (eg. 1 -> 0)
        coords1 = (ord(coords1[0])-ord('a'), coord1[1]-1)
        coords2 = (ord(coords2[0])-ord('a'), coord2[1]-1)

        if self.check_move(coords1, coords2):
            # TODO Implement moving and capturing
            pass

    def __str__(self):
        output = ''
        output += "   a  b  c  d  e  f  g  h"

        for k in range(len(self.board)):
            output += "\n%d " % (k+1)
            for j in range(len(self.board[k])):
                output += self.board[j][k]

        #for j in range(1,9):
        #    output += "\n%d " % j
        #    for i in self.board[j-1]:
        #        output += str(i) 

        return output
