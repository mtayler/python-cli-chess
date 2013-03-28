from nose.tools import *
import chess
class TestStart(object):
    def test_start(self):
        game = chess.Chess()
        game.start()

        assert_equal(game.__str__(), "\n   a  b  c  d  e  f  g  h\n"\
                                     "1 [R][H][B][Q][K][B][H][R]\n"\
                                     "2 [P][P][P][P][P][P][P][P]\n"\
                                     "3 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                     "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                     "5 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                     "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                     "7 [p][p][p][p][p][p][p][p]\n"\
                                     "8 [r][h][b][q][k][b][h][r]\n") 

#class TestCheck(object):
#    pass
#    def setup(self):
#        self.game = chess.Chess()
#        self.game.start()
#
#    def test_check_pawn(self):
#        turn = 1
#        # Check normal check_moves
#        assert_equal(self.game.check_move(turn, ('a',2), ('a',3)), True)
#        assert_equal(self.game.check_move(turn, ('b',2), ('b',5)), False)
#        assert_equal(self.game.check_move(turn, ('c',2), ('d',3)), False)
#        
#        # Check moving 2 squares at start
#        assert_equal(self.game.check_move(turn, ('b',2), ('b',4)), True)
#
#        # Check capture check_move
#        self.game.board[2][2] = '[P]'
#        self.game.board[1][1] = '[P]'
#        assert_equal(self.game.check_move(turn, ('b',2), ('c',3)), True)
#
#        # Check piece in path
#        self.game.board[1][2] = '[P]'
#        self.game.board[1][1] = '[P]'
#        assert_equal(self.game.check_move(turn, ('b',2), ('b',3)), False)
#        assert_equal(self.game.check_move(turn, ('b',2), ('b',4)), False)
#
#        # Check backwards moves
#        self.game.board[3][4] = '[P]'
#        assert_equal(self.game.check_move(turn, ('d',5), ('d',4)), False)
#        self.game.board[3][4] = '[p]'
#        assert_equal(self.game.check_move(turn, ('d',5), ('d',6)), False)
#
#    def test_check_rook(self):
#        turn = 1
#        # Check check_move along x axis
#        self.game.board[0][1] = '[ ]'
#        assert_equal(self.game.check_move(turn, ('a',1), ('a',4)), True)
#        
#        # Check check_move along y axis
#        self.game.board[0][3] = '[R]'
#        assert_equal(self.game.check_move(turn, ('a',4), ('d',4)), True)
#
#        # Check piece in path
#        assert_equal(self.game.check_move(turn, ('h',1), ('h',3)), False)
#
#    def test_check_knight(self):
#        turn = 1
#        # Check vertical L
#        assert_equal(self.game.check_move(turn, ('g',1), ('f',3)), True)
#        
#        # Check horizontal L
#        self.game.board[3][3] = '[H]'
#        assert_equal(self.game.check_move(turn, ('d',4), ('c',6)), True)
#
#        # Check invalid
#        assert_equal(self.game.check_move(turn, ('d',4), ('c',5)), False)
#
#    def test_check_bishop(self):
#        turn = 1
#        self.game.board = [['[ ]']*8 for x in xrange(8)]
#        self.game.board[0][0] = '[B]'
#
#        # Test Trues
#        assert_equal(self.game.check_move(turn, ('a',1), ('b',2)), True)
#        assert_equal(self.game.check_move(turn, ('a',1), ('c',3)), True)
#        
#        # Test Falses
#        assert_equal(self.game.check_move(turn, ('a',1), ('a',2)), False)
#        assert_equal(self.game.check_move(turn, ('a',1), ('b',3)), False)
#
#    def test_check_queen(self):
#        turn = 1
#        self.game.board = [['[ ]']*8 for x in xrange(8)]
#        self.game.board[0][0] = '[Q]'
#
#        # Check straight check_moves
#        assert_equal(self.game.check_move(turn, ('a',1), ('a',4)), True)
#        assert_equal(self.game.check_move(turn, ('a',1), ('d',1)), True)
#        assert_equal(self.game.check_move(turn, ('a',1), ('j',1)), False)
#        assert_equal(self.game.check_move(turn, ('a',1), ('a',9)), False)
#
#        # Check diagnol check_moves
#        assert_equal(self.game.check_move(turn, ('a',1), ('c',3)), True)
#        assert_equal(self.game.check_move(turn, ('a',1), ('d',4)), True)
#        assert_equal(self.game.check_move(turn, ('a',1), ('e',2)), False)
#
#    def test_check_king(self):
#        turn = 1
#        self.game.board = [['[ ]']*8 for x in xrange(8)]
#        self.game.board[0][0] = '[K]'
#
#        # Test diagnol
#        assert_equal(self.game.check_move(turn, ('a',1), ('b',2)), True)
#        assert_equal(self.game.check_move(turn, ('a',1), ('c',3)), False)
#
#        # Test straight
#        assert_equal(self.game.check_move(turn, ('a',1), ('a',2)), True)
#        assert_equal(self.game.check_move(turn, ('a',1), ('a',3)), False)
#        assert_equal(self.game.check_move(turn, ('a',1), ('c',1)), False)

class TestMove(object):
    def setup(self):
        self.game = chess.Chess()
        self.game.start()
        self.bad_move = "Invalid move."

    def test_move_pawn(self):
        turn = 0
        self.game.move(turn, ('b',2), ('b',3))
        assert_equal(self.game.__str__(),"\n   a  b  c  d  e  f  g  h\n"\
                                          "1 [R][H][B][Q][K][B][H][R]\n"\
                                          "2 [P][ ][P][P][P][P][P][P]\n"\
                                          "3 [ ][P][ ][ ][ ][ ][ ][ ]\n"\
                                          "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "5 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "7 [p][p][p][p][p][p][p][p]\n"\
                                          "8 [r][h][b][q][k][b][h][r]\n")    

        self.game.move(turn, ('d',2), ('d',4))
        print self.game
        assert_equal(self.game.__str__(),"\n   a  b  c  d  e  f  g  h\n"\
                                           "1 [R][H][B][Q][K][B][H][R]\n"\
                                           "2 [P][ ][P][ ][P][P][P][P]\n"\
                                           "3 [ ][P][ ][ ][ ][ ][ ][ ]\n"\
                                           "4 [ ][ ][ ][P][ ][ ][ ][ ]\n"\
                                           "5 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "7 [p][p][p][p][p][p][p][p]\n"\
                                           "8 [r][h][b][q][k][b][h][r]\n")    

        assert_equal(self.game.move(turn, ('c',2), ('d',1)), self.bad_move)
        assert_equal(self.game.move(turn, ('f',2), ('g',3)), self.bad_move)

    def test_move_rook(self):
        turn = 0
        self.game.board[0][1] = '[ ]'
        self.game.move(turn, ('a',1), ('a',3))
        assert_equal(self.game.__str__(),"\n   a  b  c  d  e  f  g  h\n"\
                                           "1 [ ][H][B][Q][K][B][H][R]\n"\
                                           "2 [ ][P][P][P][P][P][P][P]\n"\
                                           "3 [R][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "5 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "7 [p][p][p][p][p][p][p][p]\n"\
                                           "8 [r][h][b][q][k][b][h][r]\n") 

        self.game.board[1][0] = '[ ]'
        self.game.move(turn, ('a',3), ('a',5))
        assert_equal(self.game.__str__(),"\n   a  b  c  d  e  f  g  h\n"\
                                           "1 [ ][ ][B][Q][K][B][H][R]\n"\
                                           "2 [ ][P][P][P][P][P][P][P]\n"\
                                           "3 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "5 [R][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "7 [p][p][p][p][p][p][p][p]\n"\
                                           "8 [r][h][b][q][k][b][h][r]\n")   

        self.game.move(turn, ('a',5), ('e',5))
        assert_equal(self.game.__str__(),"\n   a  b  c  d  e  f  g  h\n"\
                                          "1 [ ][ ][B][Q][K][B][H][R]\n"\
                                          "2 [ ][P][P][P][P][P][P][P]\n"\
                                          "3 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "5 [ ][ ][ ][ ][R][ ][ ][ ]\n"\
                                          "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "7 [p][p][p][p][p][p][p][p]\n"\
                                          "8 [r][h][b][q][k][b][h][r]\n") 

        assert_equal(self.game.move(turn, ('e',5), ('f',4)), self.bad_move)

    def test_move_knight(self):
        turn = 0
        self.game.move(turn, ('b',1), ('c',3))
        assert_equal(self.game.__str__(),"\n   a  b  c  d  e  f  g  h\n"\
                                          "1 [R][ ][B][Q][K][B][H][R]\n"\
                                          "2 [P][P][P][P][P][P][P][P]\n"\
                                          "3 [ ][ ][H][ ][ ][ ][ ][ ]\n"\
                                          "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "5 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "7 [p][p][p][p][p][p][p][p]\n"\
                                          "8 [r][h][b][q][k][b][h][r]\n") 

        self.game.move(turn, ('c',3), ('e',4))
        assert_equal(self.game.__str__(),"\n   a  b  c  d  e  f  g  h\n"\
                                          "1 [R][ ][B][Q][K][B][H][R]\n"\
                                          "2 [P][P][P][P][P][P][P][P]\n"\
                                          "3 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "4 [ ][ ][ ][ ][H][ ][ ][ ]\n"\
                                          "5 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "7 [p][p][p][p][p][p][p][p]\n"\
                                          "8 [r][h][b][q][k][b][h][r]\n") 

    def test_move_bishop(self):
        turn = 0
        self.game.board[1][1] = '[ ]'
        self.game.move(turn, ('c',1), ('b',2))
        assert_equal(self.game.__str__(),"\n   a  b  c  d  e  f  g  h\n"\
                                          "1 [R][H][ ][Q][K][B][H][R]\n"\
                                          "2 [P][B][P][P][P][P][P][P]\n"\
                                          "3 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "5 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "7 [p][p][p][p][p][p][p][p]\n"\
                                          "8 [r][h][b][q][k][b][h][r]\n") 

    def test_move_queen(self):
        turn = 0
        self.game.board[3][1] = '[ ]'
        self.game.move(turn, ('d',1), ('d',4))
        assert_equal(self.game.__str__(),"\n   a  b  c  d  e  f  g  h\n"\
                                          "1 [R][H][B][ ][K][B][H][R]\n"\
                                          "2 [P][P][P][ ][P][P][P][P]\n"\
                                          "3 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "4 [ ][ ][ ][Q][ ][ ][ ][ ]\n"\
                                          "5 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "7 [p][p][p][p][p][p][p][p]\n"\
                                          "8 [r][h][b][q][k][b][h][r]\n") 
        self.game.move(turn, ('d',4), ('e',5))
        assert_equal(self.game.__str__(),"\n   a  b  c  d  e  f  g  h\n"\
                                          "1 [R][H][B][ ][K][B][H][R]\n"\
                                          "2 [P][P][P][ ][P][P][P][P]\n"\
                                          "3 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "5 [ ][ ][ ][ ][Q][ ][ ][ ]\n"\
                                          "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                          "7 [p][p][p][p][p][p][p][p]\n"\
                                          "8 [r][h][b][q][k][b][h][r]\n") 

    def test_move_king(self):
        turn = 0
        self.game.board[4][1] = '[ ]'
        self.game.move(turn, ('e',1), ('e',2))
        assert_equal(self.game.__str__(),"\n   a  b  c  d  e  f  g  h\n"\
                                           "1 [R][H][B][Q][ ][B][H][R]\n"\
                                           "2 [P][P][P][P][K][P][P][P]\n"\
                                           "3 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "4 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "5 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "6 [ ][ ][ ][ ][ ][ ][ ][ ]\n"\
                                           "7 [p][p][p][p][p][p][p][p]\n"\
                                           "8 [r][h][b][q][k][b][h][r]\n") 
        
        assert_equal(self.game.move(turn, ('e',2), ('f',2)), self.bad_move)

class TestCapture(object):
    def setup(self):
        self.game = chess.Chess()
        self.game.start()

    def test_black_capture(self):
        turn = 1
        self.game.board[3][6] = '[ ]'
        self.game.move(turn, ('d',8), ('d',2))
        assert_equal(self.game.black_captured, ['[P]'])

    def test_white_capture(self):
        turn = 0
        self.game.board[3][1] = '[ ]'
        self.game.move(turn, ('d',1), ('d', 7))
        assert_equal(self.game.white_captured, ['[p]'])

class TestTurns(object):
    def test(self):
        self.bad_move = "Invalid move."
        self.game = chess.Chess()
        self.game.start()

        assert_equal(self.game.move(1, ('a',2), ('a',3)), self.bad_move)

        assert_equal(self.game.move(0, ('a',6), ('a',5)), self.bad_move)
