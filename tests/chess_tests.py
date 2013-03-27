from nose.tools import *
import chess

class TestStart(object):
    def test_start(self):
        game = chess.Chess()
        game.start()

        assert_equal(game.__str__(), "   1  2  3  4  5  6  7  8\n"\
                                     "a [r][p][ ][ ][ ][ ][P][R]\n"\
                                     "b [h][p][ ][ ][ ][ ][P][H]\n"\
                                     "c [b][p][ ][ ][ ][ ][P][B]\n"\
                                     "d [q][p][ ][ ][ ][ ][P][Q]\n"\
                                     "e [k][p][ ][ ][ ][ ][P][K]\n"\
                                     "f [b][p][ ][ ][ ][ ][P][B]\n"\
                                     "g [h][p][ ][ ][ ][ ][P][H]\n"\
                                     "h [r][p][ ][ ][ ][ ][P][R]") 

class TestCheck(object):
    def setup(self):
        self.game = chess.Chess()
        self.game.start()

    def test_check_pawn(self):
        # Check normal moves
        assert_equal(self.game.move.check((2,'a'), (3,'a')), True)
        assert_equal(self.game.move.check((2,'b'), (5,'b')), False)
        assert_equal(self.game.move.check((2,'c'), (3,'d')), False)
        
        # Check moving 2 squares at start
        assert_equal(self.game.move.check((2,'b'), (4,'b')), True

        # Check capture move
        self.game.board[2][2] = '[P]'
        self.game.board[1][1] = '[P]'
        assert_equal(self.game.move.check((2,'b'), (3,'c')), True)

        # Check piece in path
        self.game.board[2][1] = '[P]'
        self.game.board[1][1] = '[P]'
        assert_equal(self.game.move.check((2,'b'), (3,'b')), False)
        assert_equal(self.game.move.check((2,'b'), (4,'b')), False)

    def test_check_rook(self):
        # Check move along x axis
        self.game.board[1][0] = '[ ]'
        assert_equal(self.game.move.check((1,'a'), (4,'a')), True)
        
        # Check move along y axis
        self.game.board[3][0] = '[R]'
        assert_equal(self.game.move.check((4,'a'), (4,'d')), True)

        # Check piece in path
        assert_equal(self.game.move.check((1,'h'), (3,'h')), False)

    def test_check_knight(self):
        # Check vertical L
        assert_equal(self.game.move.check(1,'g'), (3,'f'))
        
        # Check horizontal L
        self.game.board[3][3]
        assert_equal(self.game.move.check((4,'d'), (6,'c')), True)

        # Check invalid
        assert_equal(self.game.move.check((4,'d'), (5,'c')), False)

        def test_check_bishop(self):
        self.game.board = [['[ ]']*8 for x in xrange(8)]
        self.game.board[0][0] = '[B]'

        # Test Trues
        assert_equal(self.game.move.check((1,'a'), (2,'b')), True)
        assert_equal(self.game.move.check((1,'a'), (3,'c')), True)
        
        # Test Falses
        assert_equal(self.game.move.check((1,'a'), (2,'a')), False)
        assert_equal(self.game.move.check((1,'a'), (3,'b')), False)

    def test_check_queen(self):
        self.game.board = [['[ ]']*8 for x in xrange(8)]
        self.game.board[0][0] = '[Q]'

        # Check straight moves
        assert_equal(self.game.move.check((1,'a'), (4,'a')), True)
        assert_equal(self.game.move.check((1,'a'), (1,'d')), True)
        assert_equal(self.game.move.check((1,'a'), (1,'j')), False)
        assert_equal(self.game.move.check((1,'a'), (9,'a')), False)

        # Check diagnol moves
        assert_equal(self.game.move.check((1,'a'), (3,'c')), True)
        assert_equal(self.game.move.check((1,'a'), (4,'d')), True)
        assert_equal(self.game.move.check((1,'a'), (2,'e')), False)

    def test_check_king(self):
        self.game.board = [['[ ]']*8 for x in xrange(8)]
        self.game.board[0][0] = '[K]'

        # Test diagnol
        assert_equal(self.game.move.check((1,'a'), (2,'b')), True)
        assert_equal(self.game.move.check((1,'a'), (3,'c')), False)

        # Test straight
        assert_equal(self.game.move.check((1,'a'), (2,'a')), True)
        assert_equal(self.game.move.check((1,'a'), (3,'a')), False)
        assert_equal(self.game.move.check((1,'a'), (1,'c')), False)

class TestMove(object):
    def setup(self):
        self.game = chess.Chess()
        self.game.start()
        self.bad_move = "Invalid move."

    def test_move_pawn(self):
        self.game.move((2,'b'), (3,'b'))
        assert_equal(self.game.__str__(), "   1  2  3  4  5  6  7  8\n"\
                                          "a [r][p][ ][ ][ ][ ][P][R]\n"\
                                          "b [h][ ][p][ ][ ][ ][P][H]\n"\
                                          "c [b][p][ ][ ][ ][ ][P][B]\n"\
                                          "d [q][p][ ][ ][ ][ ][P][Q]\n"\
                                          "e [k][p][ ][ ][ ][ ][P][K]\n"\
                                          "f [b][p][ ][ ][ ][ ][P][B]\n"\
                                          "g [h][p][ ][ ][ ][ ][P][H]\n"\
                                          "h [r][p][ ][ ][ ][ ][P][R]")    

        self.game.move((2,'d'), (4,'d'))
        assert_equal(self.game.__str__(), "   1  2  3  4  5  6  7  8\n"\
                                          "a [r][p][ ][ ][ ][ ][P][R]\n"\
                                          "b [h][ ][p][ ][ ][ ][P][H]\n"\
                                          "c [b][p][ ][ ][ ][ ][P][B]\n"\
                                          "d [q][ ][ ][p][ ][ ][P][Q]\n"\
                                          "e [k][p][ ][ ][ ][ ][P][K]\n"\
                                          "f [b][p][ ][ ][ ][ ][P][B]\n"\
                                          "g [h][p][ ][ ][ ][ ][P][H]\n"\
                                          "h [r][p][ ][ ][ ][ ][P][R]")    

        assert_equal(self.game.move((2,'c'), (1, 'd')), self.bad_move)
        assert_equal(self.game.move((2,'f'), (3,'g')), self.bad_move)

    def test_move_rook(self):
        self.game.board[1][0] = '[ ]'
        self.game.move((1, 'a'), (3, 'a'))
        assert_equal(self.game.__str__(),  "   1  2  3  4  5  6  7  8\n"\
                                           "a [ ][ ][r][p][ ][ ][P][R]\n"\
                                           "b [h][p][ ][ ][ ][ ][P][H]\n"\
                                           "c [b][p][ ][ ][ ][ ][P][B]\n"\
                                           "d [q][p][ ][ ][ ][ ][P][Q]\n"\
                                           "e [k][p][ ][ ][ ][ ][P][K]\n"\
                                           "f [b][p][ ][ ][ ][ ][P][B]\n"\
                                           "g [h][p][ ][ ][ ][ ][P][H]\n"\
                                           "h [r][p][ ][ ][ ][ ][P][R]")   

        self.game.board[1][0] = '[ ]'
        self.game.move((1,'a'), (5,'a'))
        assert_equal(self.game.__str__(),  "   1  2  3  4  5  6  7  8\n"\
                                           "a [ ][ ][ ][ ][r][ ][P][R]\n"\
                                           "b [h][p][ ][ ][ ][ ][P][H]\n"\
                                           "c [b][p][ ][ ][ ][ ][P][B]\n"\
                                           "d [q][p][ ][ ][ ][ ][P][Q]\n"\
                                           "e [k][p][ ][ ][ ][ ][P][K]\n"\
                                           "f [b][p][ ][ ][ ][ ][P][B]\n"\
                                           "g [h][p][ ][ ][ ][ ][P][H]\n"\
                                           "h [r][p][ ][ ][ ][ ][P][R]")   

        self.game.move((5,'a'), (5, 'e'))
        assert_equal(self.game.__str__(),  "   1  2  3  4  5  6  7  8\n"\
                                           "a [r][ ][ ][ ][ ][ ][P][R]\n"\
                                           "b [h][p][ ][ ][ ][ ][P][H]\n"\
                                           "c [b][p][ ][ ][ ][ ][P][B]\n"\
                                           "d [q][p][ ][ ][ ][ ][P][Q]\n"\
                                           "e [k][p][ ][ ][r][ ][P][K]\n"\
                                           "f [b][p][ ][ ][ ][ ][P][B]\n"\
                                           "g [h][p][ ][ ][ ][ ][P][H]\n"\
                                           "h [r][p][ ][ ][ ][ ][P][R]")   

        assert_equal(self.game.move((5, 'e'), (4, 'f')), self.bad_move)
