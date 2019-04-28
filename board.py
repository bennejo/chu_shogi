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
        self.board[0][1] = FerociousLeopard(0, 1, "w")
        self.board[0][2] = CopperGeneral(0, 2, "w")
        self.board[0][3] = SilverGeneral(0, 3, "w")
        self.board[0][4] = GoldGeneral(0, 4, "w")
        self.board[0][5] = DrunkElephant(0, 5, "w")
        self.board[0][6] = King(0, 6, "w")
        self.board[0][7] = GoldGeneral(0, 7, "w")
        self.board[0][8] = SilverGeneral(0, 8, "w")
        self.board[0][9] = CopperGeneral(0, 9, "w")
        self.board[0][10] = FerociousLeopard(0, 10, "w")
        self.board[0][11] = Lance(0, 11, "w")
        self.board[1][0] = ReverseChariot(1, 0, "w")
        self.board[1][2] = Bishop(1, 2, "w")
        self.board[1][4] = BlindTiger(1, 4, "w")
        self.board[1][5] = Phoenix(1, 5, "w")
        self.board[1][6] = Kylin(1, 6, "w")
        self.board[1][7] = BlindTiger(1, 7, "w")
        self.board[1][9] = Bishop(1, 9, "w")
        self.board[1][11] = ReverseChariot(1, 11, "w")
        self.board[2][0] = SideMover(2, 0, "w")
        self.board[2][1] = VerticalMover(2, 1, "w")
        self.board[2][2] = Rook(2, 2, "w")
        self.board[2][3] = DragonHorse(2, 3, "w")
        self.board[2][4] = DragonKing(2, 4, "w")
        self.board[2][5] = FreeKing(2, 5, "w")
        self.board[2][6] = Lion(2, 6, "w")
        self.board[2][7] = DragonKing(2, 7, "w")
        self.board[2][8] = DragonHorse(2, 8, "w")
        self.board[2][9] = Rook(2, 9, "w")
        self.board[2][10] = VerticalMover(2, 10, "w")
        self.board[2][11] = SideMover(2, 11, "w")
        self.board[3][0] = Pawn(3, 0, "w")
        self.board[3][1] = Pawn(3, 1, "w")
        self.board[3][2] = Pawn(3, 2, "w")
        self.board[3][3] = Pawn(3, 3, "w")
        self.board[3][4] = Pawn(3, 4, "w")
        self.board[3][5] = Pawn(3, 5, "w")
        self.board[3][6] = Pawn(3, 6, "w")
        self.board[3][7] = Pawn(3, 7, "w")
        self.board[3][8] = Pawn(3, 8, "w")
        self.board[3][9] = Pawn(3, 9, "w")
        self.board[3][10] = Pawn(3, 10, "w")
        self.board[3][11] = Pawn(3, 11, "w")
        self.board[4][3] = GoBetween(4, 3, "w")
        self.board[4][8] = GoBetween(4, 8, "w")

        self.board[7][3] = GoBetween(7, 3, "b")
        self.board[7][8] = GoBetween(7, 8, "b")
        self.board[8][0] = Pawn(8, 0, "b")
        self.board[8][1] = Pawn(8, 1, "b")
        self.board[8][2] = Pawn(8, 2, "b")
        self.board[8][3] = Pawn(8, 3, "b")
        self.board[8][4] = Pawn(8, 4, "b")
        self.board[8][5] = Pawn(8, 5, "b")
        self.board[8][6] = Pawn(8, 6, "b")
        self.board[8][7] = Pawn(8, 7, "b")
        self.board[8][8] = Pawn(8, 8, "b")
        self.board[8][9] = Pawn(8, 9, "b")
        self.board[8][10] = Pawn(8, 10, "b")
        self.board[8][11] = Pawn(8, 11, "b")
        self.board[9][0] = SideMover(9, 0, "b")
        self.board[9][1] = VerticalMover(9, 1, "b")
        self.board[9][2] = Rook(9, 2, "b")
        self.board[9][3] = DragonHorse(9, 3, "b")
        self.board[9][4] = DragonKing(9, 4, "b")
        self.board[9][5] = Lion(9, 5, "b")
        self.board[9][6] = FreeKing(9, 6, "b")
        self.board[9][7] = DragonKing(9, 7, "b")
        self.board[9][8] = DragonHorse(9, 8, "b")
        self.board[9][9] = Rook(9, 9, "b")
        self.board[9][10] = VerticalMover(9, 10, "b")
        self.board[9][11] = SideMover(9, 11, "b")
        self.board[10][0] = ReverseChariot(10, 0, "b")
        self.board[10][2] = Bishop(10, 2, "b")
        self.board[10][4] = BlindTiger(10, 4, "b")
        self.board[10][5] = Kylin(10, 5, "b")
        self.board[10][6] = Phoenix(10, 6, "b")
        self.board[10][7] = BlindTiger(10, 7, "b")
        self.board[10][9] = Bishop(10, 9, "b")
        self.board[10][11] = ReverseChariot(10, 11, "b")
        self.board[11][0] = Lance(11, 0, "b")
        self.board[11][1] = FerociousLeopard(11, 1, "b")
        self.board[11][2] = CopperGeneral(11, 2, "b")
        self.board[11][3] = SilverGeneral(11, 3, "b")
        self.board[11][4] = GoldGeneral(11, 4, "b")
        self.board[11][5] = King(11, 5, "b")
        self.board[11][6] = DrunkElephant(11, 6, "b")
        self.board[11][7] = GoldGeneral(11, 7, "b")
        self.board[11][8] = SilverGeneral(11, 8, "b")
        self.board[11][9] = CopperGeneral(11, 9, "b")
        self.board[11][10] = FerociousLeopard(11, 10, "b")
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

    def update_moves(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].update_valid_moves(self.board)

    def draw(self, win):

        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(win)

    def get_danger_moves(self):
        danger_moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].color != self.color:
                        for move in self.board[i][j].move_list:
                            danger_moves.append(move)

        return danger_moves

    def is_checked(self):
        self.update_moves()
        danger_moves = self.get_danger_moves()
        king_pos = (-1, -1)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].king and self.board[i][j].color == self.color:
                        king_pos = (j, i)

        if king_pos in danger_moves:
            return True

        return False

    def select(self, col, row):
        if self.board[row][col] != 0:
            to_select = self.board[row][col]
            if to_select.color == self.color:
                to_select.selected = True
                self.selected = (row, col)
                if to_select.lion:
                    return 'lion'
                else:
                    return 'selected'
            else:

                return 'not selected'
        else:
            return False

    def reset_selected(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False

    def check_mate(self, color):
        pass

    def move(self, i, j):
        print("in move handler")
        if self.selected is not None:
            for move in self.board[self.selected[0]][self.selected[1]].valid_moves(self.board):
                print(str(move))
        if self.selected is None:
            return 'no selection'
        elif (j, i) in self.board[self.selected[0]][self.selected[1]].valid_moves(self.board):
            return 'valid move'
        elif i == self.selected[0] and j == self.selected[1]:
            self.board[i][j].selected = False
            return 'deselected'
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
        coords = [x.strip() for x in move_string.split(',')]
        to_move = self.board[coords[0]][coords[1]]
        self.board[coords[0]][coords[1]] = 0
        self.board[coords[2]][coords[3]] = to_move
