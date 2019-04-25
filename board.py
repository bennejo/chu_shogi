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
import pygame as pg


class Board:

    # CHECK: Numbers will need fine tuning
    rect = (0, 0, 1000, 1000)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.ready = False

        self.last = None

        self.copy = True

        self.board = [[0 for x in range(12)] for _ in range(rows)]

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

        self.turn = "w"

        self.time1 = 900
        self.time2 = 900

        self.stored_time1 = 0
        self.stored_time2 = 0

        self.winner = None

        self.start_time = time.time()

    def update_moves(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].update_valid_moves(self.board)

    def draw(self, win, color):
        if self.last and color == self.turn:
            y, x = self.last[0]
            y1, x1 = self.last[1]

            xx = (6 - x) +round(self.startX + (x * self.rect[2] / 12))
            yy = 5 + round(self.startY + (y * self.rect[3] / 12))
            pygame.draw.circle(win, (0,0,255), (xx+32, yy+30), 34, 4)
            xx1 = (6 - x) + round(self.startX + (x1 * self.rect[2] / 12))
            yy1 = 5+ round(self.startY + (y1 * self.rect[3] / 12))
            pygame.draw.circle(win, (0, 0, 255), (xx1 + 32, yy1 + 30), 34, 4)

        s = None
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(win, color)
                    if self.board[i][j].is_selected:
                        s = (i, j)

    def get_danger_moves(self, color):
        danger_moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].color != color:
                        for move in self.board[i][j].move_list:
                            danger_moves.append(move)

        return danger_moves

    def is_checked(self, color):
        self.update_moves()
        danger_moves = self.get_danger_moves(color)
        king_pos = (-1, -1)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].king and self.board[i][j].color == color:
                        king_pos = (j, i)

        if king_pos in danger_moves:
            return True

        return False

    def select(self, col, row, color):
        changed = False
        prev = (-1, -1)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].selected:
                        prev = (i, j)


        # if piece
        if self.board[row][col] == 0:
            moves = self.board[prev[0]][prev[1]].move_list
            if (col, row) in moves:
                changed = self.move(prev, (row, col), color)

        else:
            if self.board[prev[0]][prev[1]].color != self.board[row][col].color:

                moves = self.board[prev[0]][prev[1]].move_list
                print("BOARD: " + str(self.board[prev[0]][prev[1]]))
                print("PREV: " + str(prev))
                if (col, row) in moves:
                    changed = self.move(prev, (row, col), color)

                if self.board[row][col].color == color:
                    self.board[row][col].selected = True

            else:
                self.reset_selected()
                if self.board[row][col].color == color:
                    self.board[row][col].selected = True

        if changed:
            if self.turn == "w":
                self.turn = "b"
                self.reset_selected()
            else:
                self.turn = "w"
                self.reset_selected()

    def reset_selected(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False

    def check_mate(self, color):
        pass

    def move(self, start, end, color):
        checkedBefore = self.is_checked(color)
        changed = True
        nBoard = self.board[:]
        if nBoard[start[0]][start[1]].pawn:
            nBoard[start[0]][start[1]].first = False

        nBoard[start[0]][start[1]].change_pos((end[0], end[1]))
        nBoard[end[0]][end[1]] = nBoard[start[0]][start[1]]
        nBoard[start[0]][start[1]] = 0
        self.board = nBoard

        if self.is_checked(color) or (checkedBefore and self.is_checked(color)):
            changed = False
            nBoard = self.board[:]
            if nBoard[end[0]][end[1]].pawn:
                nBoard[end[0]][end[1]].first = True

            nBoard[end[0]][end[1]].change_pos((start[0], start[1]))
            nBoard[start[0]][start[1]] = nBoard[end[0]][end[1]]
            nBoard[end[0]][end[1]] = 0
            self.board = nBoard
        else:
            self.reset_selected()

        self.update_moves()
        if changed:
            self.last = [start, end]
            if self.turn == "w":
                self.storedTime1 += (time.time() - self.startTime)
            else:
                self.storedTime2 += (time.time() - self.startTime)
            self.startTime = time.time()

        return changed
