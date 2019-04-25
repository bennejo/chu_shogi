import pygame as pg
import os

b_b = pg.image.load(os.path.join("img", "B_B.png"))
b_bt = pg.image.load(os.path.join("img", "B_BT.png"))
b_c = pg.image.load(os.path.join("img", "B_C.png"))
b_de = pg.image.load(os.path.join("img", "B_DE.png"))
b_dh = pg.image.load(os.path.join("img", "B_DH.png"))
b_dk = pg.image.load(os.path.join("img", "B_DK.png"))
b_fk = pg.image.load(os.path.join("img", "B_FK.png"))
b_fl = pg.image.load(os.path.join("img", "B_FL.png"))
b_g = pg.image.load(os.path.join("img", "B_G.png"))
b_gb = pg.image.load(os.path.join("img", "B_GB.png"))
b_k = pg.image.load(os.path.join("img", "B_K.png"))
b_ky = pg.image.load(os.path.join("img", "B_KY.png"))
b_l = pg.image.load(os.path.join("img", "B_L.png"))
b_ln = pg.image.load(os.path.join("img", "B_LN.png"))
b_p = pg.image.load(os.path.join("img", "B_P.png"))
b_ph = pg.image.load(os.path.join("img", "B_PH.png"))
b_r = pg.image.load(os.path.join("img", "B_R.png"))
b_rc = pg.image.load(os.path.join("img", "B_RC.png"))
b_s = pg.image.load(os.path.join("img", "B_S.png"))
b_sm = pg.image.load(os.path.join("img", "B_SM.png"))
b_vm = pg.image.load(os.path.join("img", "B_VM.png"))

w_b = pg.image.load(os.path.join("img", "W_B.png"))
w_bt = pg.image.load(os.path.join("img", "W_BT.png"))
w_c = pg.image.load(os.path.join("img", "W_C.png"))
w_de = pg.image.load(os.path.join("img", "W_DE.png"))
w_dh = pg.image.load(os.path.join("img", "W_DH.png"))
w_dk = pg.image.load(os.path.join("img", "W_DK.png"))
w_fk = pg.image.load(os.path.join("img", "W_FK.png"))
w_fl = pg.image.load(os.path.join("img", "W_FL.png"))
w_g = pg.image.load(os.path.join("img", "W_G.png"))
w_gb = pg.image.load(os.path.join("img", "W_GB.png"))
w_k = pg.image.load(os.path.join("img", "W_K.png"))
w_ky = pg.image.load(os.path.join("img", "W_KY.png"))
w_l = pg.image.load(os.path.join("img", "W_L.png"))
w_ln = pg.image.load(os.path.join("img", "W_LN.png"))
w_p = pg.image.load(os.path.join("img", "W_P.png"))
w_ph = pg.image.load(os.path.join("img", "W_PH.png"))
w_r = pg.image.load(os.path.join("img", "W_R.png"))
w_rc = pg.image.load(os.path.join("img", "W_RC.png"))
w_s = pg.image.load(os.path.join("img", "W_S.png"))
w_sm = pg.image.load(os.path.join("img", "W_SM.png"))
w_vm = pg.image.load(os.path.join("img", "W_VM.png"))


b_img_paths = [b_b, b_bt, b_c, b_de, b_dh, b_dk, b_fk, b_fl, b_g, b_gb, b_k, b_ky, b_l, b_ln, b_p, b_ph, b_r, b_rc, b_s, b_sm, b_vm]
w_img_paths = [w_b, w_bt, w_c, w_de, w_dh, w_dk, w_fk, w_fl, w_g, w_gb, w_k, w_ky, w_l, w_ln, w_p, w_ph, w_r, w_rc, w_s, w_sm, w_vm]

b_imgs = []
w_imgs = []

for img in b_img_paths:
    b_imgs.append(pg.transform.scale(img, (82,82)))

for img in w_img_paths:
    w_imgs.append(pg.transform.scale(img, (82,82)))

class Piece:
    img = 100
    rect = (0, 0, 1000, 1000)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        self.move_list = []

    def is_selected(self):
        return self.selected

    def update_valid_moves(self, board):
        self.move_list = self.valid_moves(board)

    def draw(self, win, color):
        if self.color == 'w':
            draw_img = w_imgs[self.img]
        else:
            draw_img = b_imgs[self.img]

        # CHECK: Numbers will need fine tuning
        x = (6 - self.col) + round(self.startX + (self.col * self.rect[2] / 12))
        y = 5 + round(self.startY + (self.row * self.rect[3] / 12))

        # CHECK:  Numbers will need fine tuning
        if self.selected and self.color == color:
            pg.draw.rect(win, (255, 0, 0), (x, y, 76, 76), 4)

        win.blit(draw_img, (x, y))

    def change_pos(self, pos):
        pass

    # CHECK: Not sure I like this string convention
    def __str__(self):
        return str(self.col) + " " + str(self.row)

class Bishop(Piece):
    img = 0

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # TOP RIGHT
        djL = j + 1
        djR = j - 1
        for di in range(i - 1, -1, -1):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    break
            else:
                break

            djL += 1

        for di in range(i - 1, -1, -1):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    break
            else:
                break

            djR -= 1

        # TOP LEFT
        djL = j + 1
        djR = j - 1
        for di in range(i + 1, 8):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    break
            else:
                break
            djL += 1
        for di in range(i + 1, 8):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    break
            else:
                break

            djR -= 1

        return moves

class BlindTiger(Piece):
    img = 1

    def valid_moves(self, board):
        pass

class CopperGeneral(Piece):
    img = 2

    def valid_moves(self, board):
        pass

class DrunkElephant(Piece):
    img = 3

    def valid_moves(self, board):
        pass

class DragonHorse(Piece):
    img = 4

    def valid_moves(self, board):
        pass

class DragonKing(Piece):
    img = 5

    def valid_moves(self, board):
        pass

class FreeKing(Piece):
    img = 6

    def valid_moves(self, board):
        pass

class FerociousLeopard(Piece):
    img = 7

    def valid_moves(self, board):
        pass

class GoldGeneral(Piece):
    img = 8

    def valid_moves(self, board):
        pass

class GoBetween(Piece):
    img = 9

    def valid_moves(self, board):
        pass

class King(Piece):
    img = 10

    def valid_moves(self, board):
        pass

class Kylin(Piece):
    img = 11

    def valid_moves(self, board):
        pass

class Lance(Piece):
    img = 12

    def valid_moves(self, board):
        pass

class Lion(Piece):
    img = 13

    def valid_moves(self, board):
        pass

class Pawn(Piece):
    img = 14

    def valid_moves(self, board):
        i = self.row
        j = self.col
        print("({},{})".format(i,j))
        moves = []
        try:
            if self.color == "w":
                if i < 11:
                    p = board[i + 1][j]
                    if p == 0:
                        moves.append((j, i + 1))

                    # DIAGONAL
                    if j < 11:
                        p = board[i + 1][j + 1]
                        if p != 0:
                            if p.color != self.color:
                                moves.append((j + 1, i + 1))

                    if j > 0:
                        p = board[i + 1][j - 1]
                        if p != 0:
                            if p.color != self.color:
                                moves.append((j - 1, i + 1))

            # BLACK
            else:

                if i > 0:
                    p = board[i - 1][j]
                    if p == 0:
                        moves.append((j, i - 1))

                if j < 11:
                    p = board[i - 1][j + 1]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((j + 1, i - 1))

                if j > 0:
                    p = board[i - 1][j - 1]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((j - 1, i - 1))

        except Exception as e:
            print(e)
            exit(1)

        print("Moves: {}".format(str(moves)))
        return moves

class Phoenix(Piece):
    img = 15

    def valid_moves(self, board):
        pass

class Rook(Piece):
    img = 16

    def valid_moves(self, board):
        pass

class ReverseChariot(Piece):
    img = 17

    def valid_moves(self, board):
        pass

class SilverGeneral(Piece):
    img = 18

    def valid_moves(self, board):
        pass

class SideMover(Piece):
    img = 19

    def valid_moves(self, board):
        pass

class VerticalMover(Piece):
    img = 20

    def valid_moves(self, board):
        pass

class CrownPrince(Piece):
    img = 100

    def valid_moves(self, board):
        pass

class FlyingOx(Piece):

    img = 100

    def valid_moves(self, board):
        pass

class FlyingStag(Piece):
    img = 100

    def valid_moves(self, board):
        pass

class FreeBoar(Piece):
    img = 100

    def valid_moves(self, board):
        pass

class HornedFalcon(Piece):
    img = 100

    def valid_moves(self, board):
        pass

class SoaringEagle(Piece):
    img = 100

    def valid_moves(self, board):
        pass

class Tokin(Piece):
    img = 100

    def valid_moves(self, board):
        pass

class Whale(Piece):
    img = 100

    def valid_moves(self, board):
        pass

class WhiteHorse(Piece):
    img = 100

    def valid_moves(self, board):
        pass
