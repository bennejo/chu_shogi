from pieces import Bishop
from pieces import BlindTiger
from pieces import CopperGeneral
from pieces import DragonHorse
from pieces import DragonKing
from pieces import DrunkElephant
from pieces import FerociousLeopard
from pieces import FreeKing
from pieces import GoBetween
from pieces import GoldGeneral
from pieces import King
from pieces import Kylin
from pieces import Lance
from pieces import Lion
from pieces import Pawn
from pieces import Phoenix
from pieces import ReverseChariot
from pieces import Rook
from pieces import SideMover
from pieces import SilverGeneral
from pieces import VerticalMover

import time


class Board:

    # CHECK: Numbers will need fine tuning
    rect = (0, 0, 1000, 1000)
    startX = rect[0]
    startY = rect[1]

    def __init__(self):
        self.rows = 12
        self.cols = 12

        self.ready = False

        self.last = None

        self.copy = True

        self.board = [[0 for x in range(12)] for _ in range(12)]

        self.board[0][0] = Lance(0, 0, "w")
        self.board[1][0] = FerociousLeopard(1, 0, "w")
        self.board[2][0] = CopperGeneral(2, 0, "w")
        self.board[3][0] = SilverGeneral(3, 0, "w")
        self.board[4][0] = GoldGeneral(4, 0, "w")
        self.board[5][0] = DrunkElephant(5, 0, "w")
        self.board[6][0] = King(6, 0, "w")
        self.board[7][0] = GoldGeneral(7, 0, "w")
        self.board[8][0] = SilverGeneral(8, 0, "w")
        self.board[9][0] = CopperGeneral(9, 0, "w")
        self.board[10][0] = FerociousLeopard(10, 0, "w")
        self.board[11][0] = Lance(11, 0, "w")
        self.board[0][1] = ReverseChariot(0, 1, "w")
        self.board[2][1] = Bishop(2, 1, "w")
        self.board[4][1] = BlindTiger(4, 1, "w")
        self.board[5][1] = Phoenix(5, 1, "w")
        self.board[6][1] = Kylin(6, 1, "w")
        self.board[7][1] = BlindTiger(7, 1, "w")
        self.board[9][1] = Bishop(9, 1, "w")
        self.board[11][1] = ReverseChariot(11, 1, "w")
        self.board[0][2] = SideMover(0, 2, "w")
        self.board[1][2] = VerticalMover(1, 2, "w")
        self.board[2][2] = Rook(2, 2, "w")
        self.board[3][2] = DragonHorse(3, 2, "w")
        self.board[4][2] = DragonKing(4, 2, "w")
        self.board[5][2] = FreeKing(5, 2, "w")
        self.board[6][2] = Lion(6, 2, "w")
        self.board[7][2] = DragonKing(7, 2, "w")
        self.board[8][2] = DragonHorse(8, 2, "w")
        self.board[9][2] = Rook(9, 2, "w")
        self.board[10][2] = VerticalMover(10, 2, "w")
        self.board[11][2] = SideMover(11, 2, "w")
        self.board[0][3] = Pawn(0, 3, "w")
        self.board[1][3] = Pawn(1, 3, "w")
        self.board[2][3] = Pawn(2, 3, "w")
        self.board[3][3] = Pawn(3, 3, "w")
        self.board[4][3] = Pawn(4, 3, "w")
        self.board[5][3] = Pawn(5, 3, "w")
        self.board[6][3] = Pawn(6, 3, "w")
        self.board[7][3] = Pawn(7, 3, "w")
        self.board[8][3] = Pawn(8, 3, "w")
        self.board[9][3] = Pawn(9, 3, "w")
        self.board[10][3] = Pawn(10, 3, "w")
        self.board[11][3] = Pawn(11, 3, "w")
        self.board[3][4] = GoBetween(3, 4, "w")
        self.board[8][4] = GoBetween(8, 4, "w")

        self.board[3][7] = GoBetween(3, 7, "b")
        self.board[8][7] = GoBetween(8, 7, "b")
        self.board[0][8] = Pawn(0, 8, "b")
        self.board[1][8] = Pawn(1, 8, "b")
        self.board[2][8] = Pawn(2, 8, "b")
        self.board[3][8] = Pawn(3, 8, "b")
        self.board[4][8] = Pawn(4, 8, "b")
        self.board[5][8] = Pawn(5, 8, "b")
        self.board[6][8] = Pawn(6, 8, "b")
        self.board[7][8] = Pawn(7, 8, "b")
        self.board[8][8] = Pawn(8, 8, "b")
        self.board[9][8] = Pawn(9, 8, "b")
        self.board[10][8] = Pawn(10, 8, "b")
        self.board[11][8] = Pawn(11, 8, "b")
        self.board[0][9] = SideMover(0, 9, "b")
        self.board[1][9] = VerticalMover(1, 9, "b")
        self.board[2][9] = Rook(2, 9, "b")
        self.board[3][9] = DragonHorse(3, 9, "b")
        self.board[4][9] = DragonKing(4, 9, "b")
        self.board[5][9] = Lion(5, 9, "b")
        self.board[6][9] = FreeKing(6, 9, "b")
        self.board[7][9] = DragonKing(7, 9, "b")
        self.board[8][9] = DragonHorse(8, 9, "b")
        self.board[9][9] = Rook(9, 9, "b")
        self.board[10][9] = VerticalMover(10, 9, "b")
        self.board[11][9] = SideMover(11, 9, "b")
        self.board[0][10] = ReverseChariot(0, 10, "b")
        self.board[2][10] = Bishop(2, 10, "b")
        self.board[4][10] = BlindTiger(4, 10, "b")
        self.board[5][10] = Kylin(5, 10, "b")
        self.board[6][10] = Phoenix(6, 10, "b")
        self.board[7][10] = BlindTiger(7, 10, "b")
        self.board[9][10] = Bishop(9, 10, "b")
        self.board[11][10] = ReverseChariot(11, 10, "b")
        self.board[0][11] = Lance(0, 11, "b")
        self.board[1][11] = FerociousLeopard(1, 11, "b")
        self.board[2][11] = CopperGeneral(2, 11, "b")
        self.board[3][11] = SilverGeneral(3, 11, "b")
        self.board[4][11] = GoldGeneral(4, 11, "b")
        self.board[5][11] = King(5, 11, "b")
        self.board[6][11] = DrunkElephant(6, 11, "b")
        self.board[7][11] = GoldGeneral(7, 11, "b")
        self.board[8][11] = SilverGeneral(8, 11, "b")
        self.board[9][11] = CopperGeneral(9, 11, "b")
        self.board[10][11] = FerociousLeopard(10, 11, "b")
        self.board[11][11] = Lance(11, 11, "b")
        self.selected = None

        self.time1 = 900
        self.time2 = 900

        self.stored_time1 = 0
        self.stored_time2 = 0

        self.winner = None

        self.start_time = time.time()

        self.turn = "w"
        self.color = None

    def draw(self, win):

        for x in range(self.cols):
            for y in range(self.rows):
                if self.board[x][y] != 0:
                    self.board[x][y].draw(win)

    def update_moves(self):
        for x in range(self.cols):
            for y in range(self.rows):
                if self.board[x][y] != 0:
                    self.board[x][y].update_valid_moves(self.board)

    def select(self, col, row):
        if self.board[col][row] != 0:
            to_select = self.board[col][row]
            if to_select.color == self.color:
                to_select.selected = True
                print("Selected a " + str(type(to_select)) + "at " + str([col, row]))
                self.selected = to_select
                if to_select.lion:
                    return 'lion'
                else:
                    return 'selected'
            else:

                return 'not selected'
        else:
            return False

    def reset_selected(self):
        for x in range(self.cols):
            for y in range(self.rows):
                if self.board[x][y] != 0:
                    self.board[x][y].selected = False

    def move(self, x, y):
        if self.selected is None:
            return 'no selection'
        elif (x, y) in self.selected.valid_moves(self.board):
            return 'valid move'
        elif x == self.selected.col and y == self.selected.row:
            self.board[x][y].selected = False
            return 'deselected'
        else:
            return 'no move'

    def lion_move_1(self, x, y, fly):
        print('DEBUG: in lion_move_1')
        piece = self.selected

        print("selected " + str(x) + ", " + str(y))

        for move in piece.lion_moves(self.board):
            print(move)

        if self.selected is None:
            return 'no selection'
        elif (x, y, False) in piece.lion_moves(self.board) or (x, y, True) in piece.lion_moves(self.board):
            if self.board[x][y] != 0:
                if self.board[x][y].color != piece.color:
                    if fly:
                        return 'lion flies'
                else:
                    return 'lion flies'
            return 'lion move'

        elif (x, y) in piece.valid_moves(self.board):
            return 'single move'

        elif x == self.selected.col and y == self.selected.row:
            self.board[x][y].selected = False
            return 'deselected'
        else:
            return 'no move'

    def lion_move_2(self, x, y):
        if self.selected is None:
            raise ValueError('Lion type piece expected to be selected')
        elif (x, y, False) in self.selected.lion_moves_2(self.board) or \
                (x, y, True) in self.selected.lion_moves_2(self.board):
            return 'valid move'
        else:
            return 'no move'

    def set_color(self, color):
        self.color = color

    def do_move(self, move_string):
        """
        assumes that move has been validated and performs the move given by the string
        :param move_string: comma separated string with i,j,I,J
            where (i,j) are the coordinates of the piece to move and (I,J) are the coordinates
            of the space to move to
        :return:
        """
        coords = [int(x.strip()) for x in move_string.split(',')]
        if self.selected:
            to_move = self.selected
        else:
            to_move = self.board[coords[0]][coords[1]]

        if len(coords) == 4:
            self.board[coords[0]][coords[1]] = 0
            self.board[coords[2]][coords[3]] = to_move
            to_move.change_pos([coords[2], coords[3]])
            to_move.selected = False
            self.selected = None
            self.update_moves()
        if len(coords) == 5:
            self.board[coords[0]][coords[1]] = 0
            self.board[coords[2]][coords[3]] = to_move.promote()
            self.board[coords[2]][coords[3]].change_pos([coords[2],coords[3]])
            self.selected = None
            self.update_moves()
        elif len(coords) == 6:
            self.board[coords[0]][coords[1]] = 0
            self.board[coords[2]][coords[3]] = 0
            self.board[coords[4]][coords[5]] = to_move
            to_move.change_pos([coords[4], coords[5]])
            to_move.selected = False
            self.selected = None
            self.update_moves()
