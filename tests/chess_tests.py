from nose.tools import *
import chess
class TestStart(object):
    def test_start(self):
        game = chess.Chess()
        game.start()

        assert_equal(game.__str__(), "   a  b  c  d  e  f  g  h\n"\
                                     "1 [R][H][B][Q][K][B][H][R]\n"\
                                     "2 [P][P][P][P][P][P][P][P]\n"\
                                     "3 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                     "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                     "5 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                     "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                     "7 [p][p][p][p][p][p][p][p]\n"\
                                     "8 [r][h][b][q][k][b][h][r]") 

class TestCheck(object):
    def setup(self):
        self.game = chess.Chess()
        self.game.start()

    def test_check_pawn(self):
        # Check normal check_moves
        assert_equal(self.game.check_move(('a',2), ('a',3)), True)
        assert_equal(self.game.check_move(('b',2), ('b',5)), False)
        assert_equal(self.game.check_move(('c',2), ('d',3)), False)
        
        # Check moving 2 squares at start
        assert_equal(self.game.check_move(('b',2), ('b',4)), True)

        # Check capture check_move
        self.game.board[2][2] = '[P]'
        self.game.board[1][1] = '[P]'
        assert_equal(self.game.check_move(('b',2), ('c',3)), True)

        # Check piece in path
        self.game.board[1][2] = '[P]'
        self.game.board[1][1] = '[P]'
        assert_equal(self.game.check_move(('b',2), ('b',3)), False)
        assert_equal(self.game.check_move(('b',2), ('b',4)), False)

        # Check backwards moves
        self.game.board[3][4] = '[P]'
        assert_equal(self.game.check_move(('d',5), ('d',4)), False)
        self.game.board[3][4] = '[p]'
        assert_equal(self.game.check_move(('d',5), ('d',6)), False)
    def test_check_rook(self):
        # Check check_move along x axis
        self.game.board[0][1] = '[ ]'
        assert_equal(self.game.check_move(('a',1), ('a',4)), True)
        
        # Check check_move along y axis
        self.game.board[0][3] = '[R]'
        assert_equal(self.game.check_move(('a',4), ('d',4)), True)

        # Check piece in path
        assert_equal(self.game.check_move(('h',1), ('h',3)), False)

    def test_check_knight(self):
        # Check vertical L
        assert_equal(self.game.check_move(('g',1), ('f',3)), True)
        
        # Check horizontal L
        self.game.board[3][3] = '[H]'
        assert_equal(self.game.check_move(('d',4), ('c',6)), True)

        # Check invalid
        assert_equal(self.game.check_move(('d',4), ('c',5)), False)

    def test_check_bishop(self):
        self.game.board = [['[ ]']*8 for x in xrange(8)]
        self.game.board[0][0] = '[B]'

        # Test Trues
        assert_equal(self.game.check_move(('a',1), ('b',2)), True)
        assert_equal(self.game.check_move(('a',1), ('c',3)), True)
        
        # Test Falses
        assert_equal(self.game.check_move(('a',1), ('a',2)), False)
        assert_equal(self.game.check_move(('a',1), ('b',3)), False)

    def test_check_queen(self):
        self.game.board = [['[ ]']*8 for x in xrange(8)]
        self.game.board[0][0] = '[Q]'

        # Check straight check_moves
        assert_equal(self.game.check_move(('a',1), ('a',4)), True)
        assert_equal(self.game.check_move(('a',1), ('d',1)), True)
        assert_equal(self.game.check_move(('a',1), ('j',1)), False)
        assert_equal(self.game.check_move(('a',1), ('a',9)), False)

        # Check diagnol check_moves
        assert_equal(self.game.check_move(('a',1), ('c',3)), True)
        assert_equal(self.game.check_move(('a',1), ('d',4)), True)
        assert_equal(self.game.check_move(('a',1), ('e',2)), False)

    def test_check_king(self):
        self.game.board = [['[ ]']*8 for x in xrange(8)]
        self.game.board[0][0] = '[K]'

        # Test diagnol
        assert_equal(self.game.check_move(('a',1), ('b',2)), True)
        assert_equal(self.game.check_move(('a',1), ('c',3)), False)

        # Test straight
        assert_equal(self.game.check_move(('a',1), ('a',2)), True)
        assert_equal(self.game.check_move(('a',1), ('a',3)), False)
        assert_equal(self.game.check_move(('a',1), ('c',1)), False)

#class TestMove(object):
#    def setup(self):
#        self.game = chess.Chess()
#        self.game.start()
#        self.bad_check_move = "Invalid check_move."
#
#    def test_move_pawn(self):
#        self.game.move(('b',2), ('b',3))
#        assert_equal(self.game.__str__(), "   a  b  c  d  e  f  g  h\n"\
#                                          "1 [R][H][B][Q][K][B][H][R]\n"\
#                                          "2 [P][ ][P][P][P][P][P][P]\n"\
#                                          "3 [ ][P][ ][ ][ ][ ][ ][ ]\n"\
#                                          "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                          "5 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                          "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                          "7 [p][p][p][p][p][p][p][p]\n"\
#                                          "8 [r][h][b][q][k][b][h][r]")    
#
#        self.game.move(('d',2), ('d',4))
#        assert_equal(self.game.__str__(), "   a  b  c  d  e  f  g  h\n"\
#                                          "1 [R][H][B][Q][K][B][H][R]\n"\
#                                          "2 [P][ ][P][ ][P][P][P][P]\n"\
#                                          "3 [ ][P][ ][ ][ ][ ][ ][ ]\n"\
#                                          "4 [ ][ ][ ][P][ ][ ][ ][ ]\n"\
#                                          "5 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                          "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                          "7 [p][p][p][p][p][p][p][p]\n"\
#                                          "8 [r][h][b][q][k][b][h][r]")    
#
#        assert_equal(self.game.move(('c',2), ('d',1)), self.bad_move)
#        assert_equal(self.game.move(('f',2), ('g',3)), self.bad_move)
#
#    def test_move_rook(self):
#        self.game.board[0][1] = '[ ]'
#        self.game.move(('a',1), ('a',3))
#        assert_equal(self.game.__str__(),  "   a  b  c  d  e  f  g  h\n"\
#                                           "1 [ ][H][B][Q][K][B][H][R]\n"\
#                                           "2 [ ][P][P][P][P][P][P][P]\n"\
#                                           "3 [R][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                           "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                           "5 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                           "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                           "7 [p][p][p][p][p][p][p][p]\n"\
#                                           "8 [r][h][b][q][k][b][h][r]") 
#
#        self.game.board[1][0] = '[ ]'
#        self.game.move(('a',3), ('a',5))
#        assert_equal(self.game.__str__(),  "   a  b  c  d  e  f  g  h\n"\
#                                           "1 [ ][H][B][Q][K][B][H][R]\n"\
#                                           "2 [ ][P][P][P][P][P][P][P]\n"\
#                                           "3 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                           "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                           "5 [R][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                           "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                           "7 [p][p][p][p][p][p][p][p]\n"\
#                                           "8 [r][h][b][q][k][b][h][r]")   
#
#        self.game.move(('a',5), ('e',5))
#        assert_equal(self.game.__str__(),  "   a  b  c  d  e  f  g  h\n"\
#                                           "1 [R][H][B][Q][K][B][H][R]\n"\
#                                           "2 [P][P][P][P][P][P][P][P]\n"\
#                                           "3 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                           "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                           "5 [ ][ ][ ][ ][R][ ][ ][ ]\n"\
#                                           "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
#                                           "7 [p][p][p][p][p][p][p][p]\n"\
#                                           "8 [r][h][b][q][k][b][h][r]") 
#
#        assert_equal(self.game.move(('e',5), ('f',4)), self.bad_move)
