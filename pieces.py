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
        self.king = False

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
        self.row = pos[0]
        self.col = pos[1]

    # TODO: Not sure I like this string convention
    def __str__(self):
        return str(self.col) + " " + str(self.row)

# TODO: Define promotion to Dragon Horse
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

# TODO: Define promotion to Flying Stag
class BlindTiger(Piece):
    img = 1

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            # TOP LEFT
            if j > 0:
                p = board[i - 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i - 1,))

            if self.color == "w":
                # TOP MIDDLE
                p = board[i - 1][j]
                if p == 0:
                    moves.append((j, i - 1))
                elif p.color != self.color:
                    moves.append((j, i - 1))

            # TOP RIGHT
            if j < 11:
                p = board[i - 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j + 1, i - 1,))

        if i < 11:
            # BOTTOM LEFT
            if j > 0:
                p = board[i + 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i + 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i + 1,))

            if self.color == "b":
                # BOTTOM MIDDLE
                p = board[i + 1][j]
                if p == 0:
                    moves.append((j, i + 1))
                elif p.color != self.color:
                    moves.append((j, i + 1))

            # BOTTOM RIGHT
            if j < 11:
                p = board[i + 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i + 1))
                elif p.color != self.color:
                    moves.append((j + 1, i + 1))

        # MIDDLE LEFT
        if j > 0:
            p = board[i][j - 1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.color != self.color:
                moves.append((j - 1, i))

        # MIDDLE RIGHT
        if j < 11:
            p = board[i][j + 1]
            if p == 0:
                moves.append((j + 1, i))
            elif p.color != self.color:
                moves.append((j + 1, i))

        return moves

# TODO: Define promotion to Side Mover
class CopperGeneral(Piece):
    img = 2

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            if self.color == "b":
                # TOP LEFT
                if j > 0:
                    p = board[i - 1][j - 1]
                    if p == 0:
                        moves.append((j - 1, i - 1,))
                    elif p.color != self.color:
                        moves.append((j - 1, i - 1,))

            # TOP MIDDLE
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))

            if self.color == "b":
                # TOP RIGHT
                if j < 11:
                    p = board[i - 1][j + 1]
                    if p == 0:
                        moves.append((j + 1, i - 1,))
                    elif p.color != self.color:
                        moves.append((j + 1, i - 1,))

        if i < 11:
            if self.color == "w":
                # BOTTOM LEFT
                if j > 0:
                    p = board[i + 1][j - 1]
                    if p == 0:
                        moves.append((j - 1, i + 1,))
                    elif p.color != self.color:
                        moves.append((j - 1, i + 1,))

            # BOTTOM MIDDLE
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))

            if self.color == "w":
                # BOTTOM RIGHT
                if j < 11:
                    p = board[i + 1][j + 1]
                    if p == 0:
                        moves.append((j + 1, i + 1))
                    elif p.color != self.color:
                        moves.append((j + 1, i + 1))

        return moves

# TODO: Define promotion to Crown Prince
class DrunkElephant(Piece):
    img = 3

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            # TOP LEFT
            if j > 0:
                p = board[i - 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i - 1,))

            if self.color == "b":
                # TOP MIDDLE
                p = board[i - 1][j]
                if p == 0:
                    moves.append((j, i - 1))
                elif p.color != self.color:
                    moves.append((j, i - 1))

            # TOP RIGHT
            if j < 11:
                p = board[i - 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j + 1, i - 1,))

        if i < 11:
            # BOTTOM LEFT
            if j > 0:
                p = board[i + 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i + 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i + 1,))

            if self.color == "w":
                # BOTTOM MIDDLE
                p = board[i + 1][j]
                if p == 0:
                    moves.append((j, i + 1))
                elif p.color != self.color:
                    moves.append((j, i + 1))

            # BOTTOM RIGHT
            if j < 11:
                p = board[i + 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i + 1))
                elif p.color != self.color:
                    moves.append((j + 1, i + 1))

        # MIDDLE LEFT
        if j > 0:
            p = board[i][j - 1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.color != self.color:
                moves.append((j - 1, i))

        # MIDDLE RIGHT
        if j < 11:
            p = board[i][j + 1]
            if p == 0:
                moves.append((j + 1, i))
            elif p.color != self.color:
                moves.append((j + 1, i))

        return moves

# TODO: Define promotion to Horned Falcon
class DragonHorse(Piece):
    img = 4

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

        if i > 0:
            # TOP MIDDLE
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))

        if i < 11:
            # BOTTOM MIDDLE
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))

        # MIDDLE LEFT
        if j > 0:
            p = board[i][j - 1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.color != self.color:
                moves.append((j - 1, i))

        # MIDDLE RIGHT
        if j < 11:
            p = board[i][j + 1]
            if p == 0:
                moves.append((j + 1, i))
            elif p.color != self.color:
                moves.append((j + 1, i))
        return moves

# TODO: Define promotion to Soaring Eagle
class DragonKing(Piece):
    img = 5

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # UP RANGE
        for x in range(i - 1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        # DOWN RANGE
        for x in range(i + 1, 12, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        # LEFT RANGE
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        # RIGHT RANGE
        for x in range(j + 1, 12, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        if i > 0:
            # TOP LEFT
            if j > 0:
                p = board[i - 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i - 1,))

            # TOP RIGHT
            if j < 11:
                p = board[i - 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j + 1, i - 1,))

        if i < 11:
            # BOTTOM LEFT
            if j > 0:
                p = board[i + 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i + 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i + 1,))

            # BOTTOM RIGHT
            if j < 11:
                p = board[i + 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i + 1))
                elif p.color != self.color:
                    moves.append((j + 1, i + 1))

        return moves


class FreeKing(Piece):
    img = 6

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
                    djL = 9

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
                    djR = -1

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
                    djL = 9
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
                    djR = -1

            djR -= 1

        # UP
        for x in range(i - 1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        # DOWN
        for x in range(i + 1, 8, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        # LEFT
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        # RIGHT
        for x in range(j + 1, 8, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        return moves

# TODO: Define promotion to Bishop
class FerociousLeopard(Piece):
    img = 7

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            # TOP LEFT
            if j > 0:
                p = board[i - 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i - 1,))

            # TOP MIDDLE
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))

            # TOP RIGHT
            if j < 11:
                p = board[i - 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j + 1, i - 1,))

        if i < 11:
            # BOTTOM LEFT
            if j > 0:
                p = board[i + 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i + 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i + 1,))

            # BOTTOM MIDDLE
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))

            # BOTTOM RIGHT
            if j < 11:
                p = board[i + 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i + 1))
                elif p.color != self.color:
                    moves.append((j + 1, i + 1))

        return moves

# TODO: Define promotion to Rook
class GoldGeneral(Piece):
    img = 8

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            if self.color == "b":
                # TOP LEFT
                if j > 0:
                    p = board[i - 1][j - 1]
                    if p == 0:
                        moves.append((j - 1, i - 1,))
                    elif p.color != self.color:
                        moves.append((j - 1, i - 1,))

            # TOP MIDDLE
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))

            if self.color == "b":
                # TOP RIGHT
                if j < 11:
                    p = board[i - 1][j + 1]
                    if p == 0:
                        moves.append((j + 1, i - 1,))
                    elif p.color != self.color:
                        moves.append((j + 1, i - 1,))

        if i < 11:
            if self.color == "w":
                # BOTTOM LEFT
                if j > 0:
                    p = board[i + 1][j - 1]
                    if p == 0:
                        moves.append((j - 1, i + 1,))
                    elif p.color != self.color:
                        moves.append((j - 1, i + 1,))

            # BOTTOM MIDDLE
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))

            if self.color == "w":
                # BOTTOM RIGHT
                if j < 11:
                    p = board[i + 1][j + 1]
                    if p == 0:
                        moves.append((j + 1, i + 1))
                    elif p.color != self.color:
                        moves.append((j + 1, i + 1))

        # MIDDLE LEFT
        if j > 0:
            p = board[i][j - 1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.color != self.color:
                moves.append((j - 1, i))

        # MIDDLE RIGHT
        if j < 11:
            p = board[i][j + 1]
            if p == 0:
                moves.append((j + 1, i))
            elif p.color != self.color:
                moves.append((j + 1, i))

        return moves

# TODO: Define promotion to Drunk Elephant
class GoBetween(Piece):
    img = 9

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            # TOP MIDDLE
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))

        if i < 11:

            # BOTTOM MIDDLE
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))

        return moves


class King(Piece):
    img = 10

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.king = True

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            # TOP LEFT
            if j > 0:
                p = board[i - 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i - 1,))

            # TOP MIDDLE
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))

            # TOP RIGHT
            if j < 11:
                p = board[i - 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j + 1, i - 1,))

        if i < 11:
            # BOTTOM LEFT
            if j > 0:
                p = board[i + 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i + 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i + 1,))

            # BOTTOM MIDDLE
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))

            # BOTTOM RIGHT
            if j < 11:
                p = board[i + 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i + 1))
                elif p.color != self.color:
                    moves.append((j + 1, i + 1))

        # MIDDLE LEFT
        if j > 0:
            p = board[i][j - 1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.color != self.color:
                moves.append((j - 1, i))

        # MIDDLE RIGHT
        if j < 11:
            p = board[i][j + 1]
            if p == 0:
                moves.append((j + 1, i))
            elif p.color != self.color:
                moves.append((j + 1, i))

        return moves

# TODO: Define promotion to Lion
class Kylin(Piece):
    img = 11

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            # TOP LEFT
            if j > 0:
                p = board[i - 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i - 1,))

            # TOP RIGHT
            if j < 11:
                p = board[i - 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j + 1, i - 1,))
        if i > 1:
            # TOP JUMP MIDDLE
            p = board[i - 2][j]
            if p == 0:
                moves.append((j, i - 2))
            elif p.color != self.color:
                moves.append((j, i - 2))

        if i < 11:
            # BOTTOM LEFT
            if j > 0:
                p = board[i + 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i + 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i + 1,))

            # BOTTOM RIGHT
            if j < 11:
                p = board[i + 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i + 1))
                elif p.color != self.color:
                    moves.append((j + 1, i + 1))

        if i < 10:
            # BOTTOM JUMP MIDDLE
            p = board[i + 2][j]
            if p == 0:
                moves.append((j, i + 2))
            elif p.color != self.color:
                moves.append((j, i + 2))

        # MIDDLE LEFT
        if j > 1:
            p = board[i][j - 2]
            if p == 0:
                moves.append((j - 2, i))
            elif p.color != self.color:
                moves.append((j - 2, i))

        # MIDDLE RIGHT
        if j < 10:
            p = board[i][j + 2]
            if p == 0:
                moves.append((j + 2, i))
            elif p.color != self.color:
                moves.append((j + 2, i))

        return moves

# TODO: Define promotion to White Horse
class Lance(Piece):
    img = 12

    def valid_moves(self, board):
        i = self.row
        j = self.col
        moves = []

        # White is ranged down
        if self.color == "w":
            for x in range(i + 1, 12, 1):
                p = board[x][j]
                if p == 0:
                    moves.append((j, x))
                elif p.color != self.color:
                    moves.append((j, x))
                    break
                else:
                    break

        # Black is ranged up
        else:
            for x in range(i - 1, -1, -1):
                p = board[x][j]
                if p == 0:
                    moves.append((j, x))
                elif p.color != self.color:
                    moves.append((j, x))
                    break
                else:
                    break

        return moves

class Lion(Piece):
    img = 13

    # TODO: These are the valid moves for a king. We need to adjust them to Lion moves
    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            # TOP LEFT
            if j > 0:
                p = board[i - 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i - 1,))

            # TOP MIDDLE
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))

            # TOP RIGHT
            if j < 11:
                p = board[i - 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i - 1,))
                elif p.color != self.color:
                    moves.append((j + 1, i - 1,))

        if i < 11:
            # BOTTOM LEFT
            if j > 0:
                p = board[i + 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i + 1,))
                elif p.color != self.color:
                    moves.append((j - 1, i + 1,))

            # BOTTOM MIDDLE
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))

            # BOTTOM RIGHT
            if j < 11:
                p = board[i + 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i + 1))
                elif p.color != self.color:
                    moves.append((j + 1, i + 1))

        # MIDDLE LEFT
        if j > 0:
            p = board[i][j - 1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.color != self.color:
                moves.append((j - 1, i))

        # MIDDLE RIGHT
        if j < 11:
            p = board[i][j + 1]
            if p == 0:
                moves.append((j + 1, i))
            elif p.color != self.color:
                moves.append((j + 1, i))

        return moves

# TODO: Define promotion to Tokin
class Pawn(Piece):
    img = 14

    def valid_moves(self, board):
        i = self.row
        j = self.col
        moves = []
        try:
            if self.color == "w":
                if i < 11:
                    p = board[i + 1][j]
                    if p == 0:
                        moves.append((j, i + 1))

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

                if j > 0:
                    p = board[i - 1][j - 1]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((j - 1, i - 1))

        except:
            exit(1)

        return moves

# TODO: Define promotion to Free King
class Phoenix(Piece):
    img = 15

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            # TOP MIDDLE
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))

        if i > 1:
            # TOP JUMP LEFT
            if j > 1:
                p = board[i - 2][j - 2]
                if p == 0:
                    moves.append((j - 2, i - 2,))
                elif p.color != self.color:
                    moves.append((j - 2, i - 2,))

            # TOP JUMP RIGHT
            if j < 10:
                p = board[i - 2][j + 2]
                if p == 0:
                    moves.append((j + 2, i - 2,))
                elif p.color != self.color:
                    moves.append((j + 2, i - 2,))

        if i < 11:
            # BOTTOM MIDDLE
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))

        if i < 10:
            # BOTTOM JUMP LEFT
            if j > 1:
                p = board[i + 2][j - 2]
                if p == 0:
                    moves.append((j - 2, i + 2,))
                elif p.color != self.color:
                    moves.append((j - 2, i + 2,))

            # BOTTOM JUMP RIGHT
            if j < 10:
                p = board[i + 2][j + 2]
                if p == 0:
                    moves.append((j + 2, i + 2))
                elif p.color != self.color:
                    moves.append((j + 2, i + 2))

        # MIDDLE LEFT
        if j > 0:
            p = board[i][j - 1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.color != self.color:
                moves.append((j - 1, i))

        # MIDDLE RIGHT
        if j < 11:
            p = board[i][j + 1]
            if p == 0:
                moves.append((j + 1, i))
            elif p.color != self.color:
                moves.append((j + 1, i))

        return moves

# TODO: Define promotion to Dragon King
class Rook(Piece):
    img = 16

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # UP RANGE
        for x in range(i - 1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        # DOWN RANGE
        for x in range(i + 1, 12, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        # LEFT RANGE
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        # RIGHT RANGE
        for x in range(j + 1, 12, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        return moves

# TODO: Define promotion to Whale
class ReverseChariot(Piece):
    img = 17

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # UP RANGE
        for x in range(i - 1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        # DOWN RANGE
        for x in range(i + 1, 12, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        return moves

# TODO: Define promotion to Vertical Mover
class SilverGeneral(Piece):
    img = 18

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            if self.color == "b":
                # TOP LEFT
                if j > 0:
                    p = board[i - 1][j - 1]
                    if p == 0:
                        moves.append((j - 1, i - 1,))
                    elif p.color != self.color:
                        moves.append((j - 1, i - 1,))

            # TOP MIDDLE
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))

            if self.color == "b":
                # TOP RIGHT
                if j < 11:
                    p = board[i - 1][j + 1]
                    if p == 0:
                        moves.append((j + 1, i - 1,))
                    elif p.color != self.color:
                        moves.append((j + 1, i - 1,))

        if i < 11:
            if self.color == "w":
                # BOTTOM LEFT
                if j > 0:
                    p = board[i + 1][j - 1]
                    if p == 0:
                        moves.append((j - 1, i + 1,))
                    elif p.color != self.color:
                        moves.append((j - 1, i + 1,))

            # BOTTOM MIDDLE
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))

            if self.color == "w":
                # BOTTOM RIGHT
                if j < 11:
                    p = board[i + 1][j + 1]
                    if p == 0:
                        moves.append((j + 1, i + 1))
                    elif p.color != self.color:
                        moves.append((j + 1, i + 1))

        return moves

# TODO: Define promotion to Free Boar
class SideMover(Piece):
    img = 19

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            # TOP MIDDLE
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))

        if i < 11:
            # BOTTOM MIDDLE
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))

        # LEFT RANGE
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        # RIGHT RANGE
        for x in range(j + 1, 12, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        return moves

# TODO: Define promotion to Flying Ox
class VerticalMover(Piece):
    img = 20

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # UP RANGE
        for x in range(i - 1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        # DOWN RANGE
        for x in range(i + 1, 12, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        # MIDDLE LEFT
        if j > 0:
            p = board[i][j - 1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.color != self.color:
                moves.append((j - 1, i))

        # MIDDLE RIGHT
        if j < 11:
            p = board[i][j + 1]
            if p == 0:
                moves.append((j + 1, i))
            elif p.color != self.color:
                moves.append((j + 1, i))
        return moves

# TODO: Define valid moves
class CrownPrince(Piece):
    img = 100

    def valid_moves(self, board):
        pass

# TODO: Define valid moves
class FlyingOx(Piece):

    img = 100

    def valid_moves(self, board):
        pass

# TODO: Define valid moves
class FlyingStag(Piece):
    img = 100

    def valid_moves(self, board):
        pass

# TODO: Define valid moves
class FreeBoar(Piece):
    img = 100

    def valid_moves(self, board):
        pass

# TODO: Define valid moves
class HornedFalcon(Piece):
    img = 100

    def valid_moves(self, board):
        pass

# TODO: Define valid moves
class SoaringEagle(Piece):
    img = 100

    def valid_moves(self, board):
        pass

# TODO: Define valid moves
class Tokin(Piece):
    img = 100

    def valid_moves(self, board):
        pass

# TODO: Define valid moves
class Whale(Piece):
    img = 100

    def valid_moves(self, board):
        pass

# TODO: Define valid moves
class WhiteHorse(Piece):
    img = 100

    def valid_moves(self, board):
        pass
