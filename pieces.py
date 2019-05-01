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
    
X_OFFSET = 0
Y_OFFSET = 0
X_BOARD_SIZE = 1000
Y_BOARD_SIZE = 1000
LINE_THICKNESS = 4
X_BOX_DELTA = X_BOARD_SIZE / 12
Y_BOX_DELTA = Y_BOARD_SIZE / 12

def draw_box(col, row, win, color=(255, 0, 0), color_bot=(0, 255, 0), option=False):

    x1 = round(X_OFFSET + (col * X_BOX_DELTA)) + 4
    y1 = round(Y_OFFSET + (row * Y_BOX_DELTA)) + 4
    x2 = x1 + X_BOX_DELTA
    y2 = y1 + Y_BOX_DELTA

    if option:
        pg.draw.polygon(win, color, [(x1, y1), (x1, y2), (x2, y1)], 4)
        pg.draw.polygon(win, color_bot, [(x2, y2), (x2, y1), (x1, y2)], 4)
    else:
        pg.draw.rect(win, color, (x1, y1, X_BOX_DELTA, Y_BOX_DELTA), 4)



class Piece:
    img = 100

    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.selected = False
        self.move_list = []
        self.lion_move_list = []
        self.lion_move_list_2 = []
        self.king = False
        self.lion = False
        self.lion_2 = False
        self.flying = False
        self.soaring_eagle_direction = None

    def is_selected(self):
        return self.selected

    def update_valid_moves(self, board):
        self.move_list = self.valid_moves(board)
        self.lion_move_list = self.lion_moves(board)
        self.lion_move_list_2 = self.lion_moves_2(board)

    def draw(self, win):
        # TODO: add flying handler

        if self.color == 'w':
            draw_img = w_imgs[self.img]
        else:
            draw_img = b_imgs[self.img]

        # CHECK:  Numbers will need fine tuning
        if self.selected:
            draw_box(self.col, self.row, win)
            for coords in self.move_list:
                draw_box(coords[0], coords[1], win, color=(255,128,0))
            if self.lion and not self.lion_2:
                for coords in self.lion_move_list:
                    draw_box(coords[0], coords[1], win, option=coords[2])
            if self.lion_2:
                for coords in self.lion_move_list_2:
                    draw_box(coords[0], coords[1], win, color=(255, 128, 0))

        x = round(X_OFFSET + (self.col * X_BOX_DELTA)) + 4
        y = round(Y_OFFSET + (self.row * Y_BOX_DELTA)) + 4

        if self.flying:
            win.blit(draw_img, (x-10, y-10))
        else:
            win.blit(draw_img, (x, y))

    def change_pos(self, pos):
        self.col = pos[0]
        self.row = pos[1]

    def valid_moves(self, board):
        return []

    def lion_moves(self, board):
        return []

    def lion_moves_2(self, board):
        return []

    # TODO: Not sure I like this string convention
    def __str__(self):
        return str(self.col) + " " + str(self.row)

# TODO: Define promotion to Dragon Horse
class Bishop(Piece):
    img = 0

    def valid_moves(self, board):
        x = self.col
        y = self.row

        moves = []

        # TOP RIGHT
        dxL = x + 1
        dxR = x - 1
        for dy in range(y - 1, -1, -1):
            if dxL < 8:
                p = board[dxL][dy]
                if p == 0:
                    moves.append((dxL, dy))
                elif p.color != self.color:
                    moves.append((dxL, dy))
                    break
                else:
                    break
            else:
                break

            dxL += 1

        for dy in range(y - 1, -1, -1):
            if dxR > -1:
                p = board[dxR][dy]
                if p == 0:
                    moves.append((dxR, dy))
                elif p.color != self.color:
                    moves.append((dxR, dy))
                    break
                else:
                    break
            else:
                break

            dxR -= 1

        # TOP LEFT
        dxL = x + 1
        dxR = x - 1
        for dy in range(y + 1, 8):
            if dxL < 8:
                p = board[dxL][dy]
                if p == 0:
                    moves.append((dxL, dy))
                elif p.color != self.color:
                    moves.append((dxL, dy))
                    break
                else:
                    break
            else:
                break
            dxL += 1
        for dy in range(y + 1, 8):
            if dxR > -1:
                p = board[dxR][dy]
                if p == 0:
                    moves.append((dxR, dy))
                elif p.color != self.color:
                    moves.append((dxR, dy))
                    break
                else:
                    break
            else:
                break

            dxR -= 1

        return moves

# TODO: Define promotion to Flying Stag
class BlindTiger(Piece):
    img = 1

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        if y > 0:
            # TOP LEFT
            if x > 0:
                p = board[x - 1][y - 1]
                if p == 0:
                    moves.append((x - 1, y - 1,))
                elif p.color != self.color:
                    moves.append((x - 1, y - 1,))

            if self.color == "w":
                # TOP MIDDLE
                p = board[x][y - 1]
                if p == 0:
                    moves.append((x, y - 1))
                elif p.color != self.color:
                    moves.append((x, y - 1))

            # TOP RIGHT
            if x < 11:
                p = board[x + 1][y - 1]
                if p == 0:
                    moves.append((x + 1, y - 1,))
                elif p.color != self.color:
                    moves.append((x + 1, y - 1,))

        if y < 11:
            # BOTTOM LEFT
            if x > 0:
                p = board[x - 1][y + 1]
                if p == 0:
                    moves.append((x - 1, y + 1,))
                elif p.color != self.color:
                    moves.append((x - 1, y + 1,))

            if self.color == "b":
                # BOTTOM MIDDLE
                p = board[x][y + 1]
                if p == 0:
                    moves.append((x, y + 1))
                elif p.color != self.color:
                    moves.append((x, y + 1))

            # BOTTOM RIGHT
            if x < 11:
                p = board[x + 1][y + 1]
                if p == 0:
                    moves.append((x + 1, y + 1))
                elif p.color != self.color:
                    moves.append((x + 1, y + 1))

        # MIDDLE LEFT
        if x > 0:
            p = board[x - 1][y]
            if p == 0:
                moves.append((x - 1, y))
            elif p.color != self.color:
                moves.append((x - 1, y))

        # MIDDLE RIGHT
        if x < 11:
            p = board[x + 1][y]
            if p == 0:
                moves.append((x + 1, y))
            elif p.color != self.color:
                moves.append((x + 1, y))

        return moves

# TODO: Define promotion to Side Mover
class CopperGeneral(Piece):
    img = 2

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        if y > 0:
            if self.color == "b":
                # TOP LEFT
                if x > 0:
                    p = board[x - 1][y - 1]
                    if p == 0:
                        moves.append((x - 1, y - 1,))
                    elif p.color != self.color:
                        moves.append((x - 1, y - 1,))

            # TOP MIDDLE
            p = board[x][y - 1]
            if p == 0:
                moves.append((x, y - 1))
            elif p.color != self.color:
                moves.append((x, y - 1))

            if self.color == "b":
                # TOP RIGHT
                if x < 11:
                    p = board[x + 1][y - 1]
                    if p == 0:
                        moves.append((x + 1, y - 1,))
                    elif p.color != self.color:
                        moves.append((x + 1, y - 1,))

        if y < 11:
            if self.color == "w":
                # BOTTOM LEFT
                if x > 0:
                    p = board[x - 1][y + 1]
                    if p == 0:
                        moves.append((x - 1, y + 1,))
                    elif p.color != self.color:
                        moves.append((x - 1, y + 1,))

            # BOTTOM MIDDLE
            p = board[x][y + 1]
            if p == 0:
                moves.append((x, y + 1))
            elif p.color != self.color:
                moves.append((x, y + 1))

            if self.color == "w":
                # BOTTOM RIGHT
                if x < 11:
                    p = board[x + 1][y + 1]
                    if p == 0:
                        moves.append((x + 1, y + 1))
                    elif p.color != self.color:
                        moves.append((x + 1, y + 1))

        return moves

# TODO: Define promotion to Crown Prince
class DrunkElephant(Piece):
    img = 3

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        if y > 0:
            # TOP LEFT
            if x > 0:
                p = board[x - 1][y - 1]
                if p == 0:
                    moves.append((x - 1, y - 1,))
                elif p.color != self.color:
                    moves.append((x - 1, y - 1,))

            if self.color == "b":
                # TOP MIDDLE
                p = board[x][y - 1]
                if p == 0:
                    moves.append((x, y - 1))
                elif p.color != self.color:
                    moves.append((x, y - 1))

            # TOP RIGHT
            if x < 11:
                p = board[x + 1][y - 1]
                if p == 0:
                    moves.append((x + 1, y - 1,))
                elif p.color != self.color:
                    moves.append((x + 1, y - 1,))

        if y < 11:
            # BOTTOM LEFT
            if x > 0:
                p = board[x - 1][y + 1]
                if p == 0:
                    moves.append((x - 1, y + 1,))
                elif p.color != self.color:
                    moves.append((x - 1, y + 1,))

            if self.color == "w":
                # BOTTOM MIDDLE
                p = board[x][y + 1]
                if p == 0:
                    moves.append((x, y + 1))
                elif p.color != self.color:
                    moves.append((x, y + 1))

            # BOTTOM RIGHT
            if x < 11:
                p = board[x + 1][y + 1]
                if p == 0:
                    moves.append((x + 1, y + 1))
                elif p.color != self.color:
                    moves.append((x + 1, y + 1))

        # MIDDLE LEFT
        if x > 0:
            p = board[x - 1][y]
            if p == 0:
                moves.append((x - 1, y))
            elif p.color != self.color:
                moves.append((x - 1, y))

        # MIDDLE RIGHT
        if x < 11:
            p = board[x + 1][y]
            if p == 0:
                moves.append((x + 1, y))
            elif p.color != self.color:
                moves.append((x + 1, y))

        return moves

# TODO: Define promotion to Horned Falcon
class DragonHorse(Piece):
    img = 4

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        # TOP RIGHT
        dxL = x + 1
        dxR = x - 1
        for dy in range(y - 1, -1, -1):
            if dxL < 8:
                p = board[dxL][dy]
                if p == 0:
                    moves.append((dxL, dy))
                elif p.color != self.color:
                    moves.append((dxL, dy))
                    break
                else:
                    break
            else:
                break

            dxL += 1

        for dy in range(y - 1, -1, -1):
            if dxR > -1:
                p = board[dxR][dy]
                if p == 0:
                    moves.append((dxR, dy))
                elif p.color != self.color:
                    moves.append((dxR, dy))
                    break
                else:
                    break
            else:
                break

            dxR -= 1

        # TOP LEFT
        dxL = x + 1
        dxR = x - 1
        for dy in range(y + 1, 8):
            if dxL < 8:
                p = board[dxL][dy]
                if p == 0:
                    moves.append((dxL, dy))
                elif p.color != self.color:
                    moves.append((dxL, dy))
                    break
                else:
                    break
            else:
                break
            dxL += 1
        for dy in range(y + 1, 8):
            if dxR > -1:
                p = board[dxR][dy]
                if p == 0:
                    moves.append((dxR, dy))
                elif p.color != self.color:
                    moves.append((dxR, dy))
                    break
                else:
                    break
            else:
                break

            dxR -= 1

        if y > 0:
            # TOP MIDDLE
            p = board[x][y - 1]
            if p == 0:
                moves.append((x, y - 1))
            elif p.color != self.color:
                moves.append((x, y - 1))

        if y < 11:
            # BOTTOM MIDDLE
            p = board[x][y + 1]
            if p == 0:
                moves.append((x, y + 1))
            elif p.color != self.color:
                moves.append((x, y + 1))

        # MIDDLE LEFT
        if x > 0:
            p = board[x - 1][y]
            if p == 0:
                moves.append((x - 1, y))
            elif p.color != self.color:
                moves.append((x - 1, y))

        # MIDDLE RIGHT
        if x < 11:
            p = board[x + 1][y]
            if p == 0:
                moves.append((x + 1, y))
            elif p.color != self.color:
                moves.append((x + 1, y))
        return moves

# TODO: Define promotion to Soaring Eagle
class DragonKing(Piece):
    img = 5

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        # UP RANGE
        for dy in range(y - 1, -1, -1):
            p = board[x][dy]
            if p == 0:
                moves.append((x, dy))
            elif p.color != self.color:
                moves.append((x, dy))
                break
            else:
                break

        # DOWN RANGE
        for dy in range(y + 1, 12, 1):
            p = board[x][dy]
            if p == 0:
                moves.append((x, dy))
            elif p.color != self.color:
                moves.append((x, dy))
                break
            else:
                break

        # LEFT RANGE
        for dx in range(x - 1, -1, -1):
            p = board[dx][y]
            if p == 0:
                moves.append((dx, y))
            elif p.color != self.color:
                moves.append((dx, y))
                break
            else:
                break

        # RIGHT RANGE
        for dx in range(x + 1, 12, 1):
            p = board[dx][y]
            if p == 0:
                moves.append((dx, y))
            elif p.color != self.color:
                moves.append((dx, y))
                break
            else:
                break

        if y > 0:
            # TOP LEFT
            if x > 0:
                p = board[x - 1][y - 1]
                if p == 0:
                    moves.append((x - 1, y - 1,))
                elif p.color != self.color:
                    moves.append((x - 1, y - 1,))

            # TOP RIGHT
            if x < 11:
                p = board[x + 1][y - 1]
                if p == 0:
                    moves.append((x + 1, y - 1,))
                elif p.color != self.color:
                    moves.append((x + 1, y - 1,))

        if y < 11:
            # BOTTOM LEFT
            if x > 0:
                p = board[x - 1][y + 1]
                if p == 0:
                    moves.append((x - 1, y + 1,))
                elif p.color != self.color:
                    moves.append((x - 1, y + 1,))

            # BOTTOM RIGHT
            if x < 11:
                p = board[x + 1][y + 1]
                if p == 0:
                    moves.append((x + 1, y + 1))
                elif p.color != self.color:
                    moves.append((x + 1, y + 1))

        return moves


class FreeKing(Piece):
    img = 6

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        # TOP RIGHT
        dxL = x + 1
        dxR = x - 1
        for dy in range(y - 1, -1, -1):
            if dxL < 8:
                p = board[dxL][dy]
                if p == 0:
                    moves.append((dxL, dy))
                elif p.color != self.color:
                    moves.append((dxL, dy))
                    break
                else:
                    dxL = 9

            dxL += 1

        for dy in range(y - 1, -1, -1):
            if dxR > -1:
                p = board[dxR][dy]
                if p == 0:
                    moves.append((dxR, dy))
                elif p.color != self.color:
                    moves.append((dxR, dy))
                    break
                else:
                    dxR = -1

            dxR -= 1

        # TOP LEFT
        dxL = x + 1
        dxR = x - 1
        for dy in range(y + 1, 12):
            if dxL < 8:
                p = board[dxL][dy]
                if p == 0:
                    moves.append((dxL, dy))
                elif p.color != self.color:
                    moves.append((dxL, dy))
                    break
                else:
                    dxL = 9
            dxL += 1
        for dy in range(y + 1, 12):
            if dxR > -1:
                p = board[dxR][dy]
                if p == 0:
                    moves.append((dxR, dy))
                elif p.color != self.color:
                    moves.append((dxR, dy))
                    break
                else:
                    dxR = -1

            dxR -= 1

        # UP
        for dy in range(y - 1, -1, -1):
            p = board[x][dy]
            if p == 0:
                moves.append((x, dy))
            elif p.color != self.color:
                moves.append((x, dy))
                break
            else:
                break

        # DOWN
        for dy in range(y + 1, 12, 1):
            p = board[x][dy]
            if p == 0:
                moves.append((x, dy))
            elif p.color != self.color:
                moves.append((x, dy))
                break
            else:
                break

        # LEFT
        for dx in range(x - 1, -1, -1):
            p = board[dx][y]
            if p == 0:
                moves.append((dx, y))
            elif p.color != self.color:
                moves.append((dx, y))
                break
            else:
                break

        # RIGHT
        for dx in range(x + 1, 8, 1):
            p = board[dx][y]
            if p == 0:
                moves.append((dx, y))
            elif p.color != self.color:
                moves.append((dx, y))
                break
            else:
                break

        return moves

# TODO: Define promotion to Bishop
class FerociousLeopard(Piece):
    img = 7

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        if y > 0:
            # TOP LEFT
            if x > 0:
                p = board[x - 1][y - 1]
                if p == 0:
                    moves.append((x - 1, y - 1,))
                elif p.color != self.color:
                    moves.append((x - 1, y - 1,))

            # TOP MIDDLE
            p = board[x][y - 1]
            if p == 0:
                moves.append((x, y - 1))
            elif p.color != self.color:
                moves.append((x, y - 1))

            # TOP RIGHT
            if x < 11:
                p = board[x + 1][y - 1]
                if p == 0:
                    moves.append((x + 1, y - 1,))
                elif p.color != self.color:
                    moves.append((x + 1, y - 1,))

        if y < 11:
            # BOTTOM LEFT
            if x > 0:
                p = board[x - 1][y + 1]
                if p == 0:
                    moves.append((x - 1, y + 1,))
                elif p.color != self.color:
                    moves.append((x - 1, y + 1,))

            # BOTTOM MIDDLE
            p = board[x][y + 1]
            if p == 0:
                moves.append((x, y + 1))
            elif p.color != self.color:
                moves.append((x, y + 1))

            # BOTTOM RIGHT
            if x < 11:
                p = board[x + 1][y + 1]
                if p == 0:
                    moves.append((x + 1, y + 1))
                elif p.color != self.color:
                    moves.append((x + 1, y + 1))

        return moves

# TODO: Define promotion to Rook
class GoldGeneral(Piece):
    img = 8

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        if y > 0:
            if self.color == "b":
                # TOP LEFT
                if x > 0:
                    p = board[x - 1][y - 1]
                    if p == 0:
                        moves.append((x - 1, y - 1,))
                    elif p.color != self.color:
                        moves.append((x - 1, y - 1,))

            # TOP MIDDLE
            p = board[x][y - 1]
            if p == 0:
                moves.append((x, y - 1))
            elif p.color != self.color:
                moves.append((x, y - 1))

            if self.color == "b":
                # TOP RIGHT
                if x < 11:
                    p = board[x + 1][y - 1]
                    if p == 0:
                        moves.append((x + 1, y - 1,))
                    elif p.color != self.color:
                        moves.append((x + 1, y - 1,))

        if y < 11:
            if self.color == "w":
                # BOTTOM LEFT
                if x > 0:
                    p = board[x - 1][y + 1]
                    if p == 0:
                        moves.append((x - 1, y + 1,))
                    elif p.color != self.color:
                        moves.append((x - 1, y + 1,))

            # BOTTOM MIDDLE
            p = board[x][y + 1]
            if p == 0:
                moves.append((x, y + 1))
            elif p.color != self.color:
                moves.append((x, y + 1))

            if self.color == "w":
                # BOTTOM RIGHT
                if x < 11:
                    p = board[x + 1][y + 1]
                    if p == 0:
                        moves.append((x + 1, y + 1))
                    elif p.color != self.color:
                        moves.append((x + 1, y + 1))

        # MIDDLE LEFT
        if x > 0:
            p = board[x - 1][y]
            if p == 0:
                moves.append((x - 1, y))
            elif p.color != self.color:
                moves.append((x - 1, y))

        # MIDDLE RIGHT
        if x < 11:
            p = board[x + 1][y]
            if p == 0:
                moves.append((x + 1, y))
            elif p.color != self.color:
                moves.append((x + 1, y))

        return moves

# TODO: Define promotion to Drunk Elephant
class GoBetween(Piece):
    img = 9

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        if y > 0:
            # TOP MIDDLE
            p = board[x][y - 1]
            if p == 0:
                moves.append((x, y - 1))
            elif p.color != self.color:
                moves.append((x, y - 1))

        if y < 11:

            # BOTTOM MIDDLE
            p = board[x][y + 1]
            if p == 0:
                moves.append((x, y + 1))
            elif p.color != self.color:
                moves.append((x, y + 1))

        return moves


class King(Piece):
    img = 10

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.king = True

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        if y > 0:
            # TOP LEFT
            if x > 0:
                p = board[x - 1][y - 1]
                if p == 0:
                    moves.append((x - 1, y - 1,))
                elif p.color != self.color:
                    moves.append((x - 1, y - 1,))

            # TOP MIDDLE
            p = board[x][y - 1]
            if p == 0:
                moves.append((x, y - 1))
            elif p.color != self.color:
                moves.append((x, y - 1))

            # TOP RIGHT
            if x < 11:
                p = board[x + 1][y - 1]
                if p == 0:
                    moves.append((x + 1, y - 1,))
                elif p.color != self.color:
                    moves.append((x + 1, y - 1,))

        if y < 11:
            # BOTTOM LEFT
            if x > 0:
                p = board[x - 1][y + 1]
                if p == 0:
                    moves.append((x - 1, y + 1,))
                elif p.color != self.color:
                    moves.append((x - 1, y + 1,))

            # BOTTOM MIDDLE
            p = board[x][y + 1]
            if p == 0:
                moves.append((x, y + 1))
            elif p.color != self.color:
                moves.append((x, y + 1))

            # BOTTOM RIGHT
            if x < 11:
                p = board[x + 1][y + 1]
                if p == 0:
                    moves.append((x + 1, y + 1))
                elif p.color != self.color:
                    moves.append((x + 1, y + 1))

        # MIDDLE LEFT
        if x > 0:
            p = board[x - 1][y]
            if p == 0:
                moves.append((x - 1, y))
            elif p.color != self.color:
                moves.append((x - 1, y))

        # MIDDLE RIGHT
        if x < 11:
            p = board[x + 1][y]
            if p == 0:
                moves.append((x + 1, y))
            elif p.color != self.color:
                moves.append((x + 1, y))

        return moves

# TODO: Define promotion to Lion
class Kylin(Piece):
    img = 11

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        if y > 0:
            # TOP LEFT
            if x > 0:
                p = board[x - 1][y - 1]
                if p == 0:
                    moves.append((x - 1, y - 1,))
                elif p.color != self.color:
                    moves.append((x - 1, y - 1,))

            # TOP RIGHT
            if x < 11:
                p = board[x + 1][y - 1]
                if p == 0:
                    moves.append((x + 1, y - 1,))
                elif p.color != self.color:
                    moves.append((x + 1, y - 1,))
        if y > 1:
            # TOP JUMP MIDDLE
            p = board[x][y - 2]
            if p == 0:
                moves.append((x, y - 2))
            elif p.color != self.color:
                moves.append((x, y - 2))

        if y < 11:
            # BOTTOM LEFT
            if x > 0:
                p = board[x - 1][y + 1]
                if p == 0:
                    moves.append((x - 1, y + 1,))
                elif p.color != self.color:
                    moves.append((x - 1, y + 1,))

            # BOTTOM RIGHT
            if x < 11:
                p = board[x + 1][y + 1]
                if p == 0:
                    moves.append((x + 1, y + 1))
                elif p.color != self.color:
                    moves.append((x + 1, y + 1))

        if y < 10:
            # BOTTOM JUMP MIDDLE
            p = board[x][y + 2]
            if p == 0:
                moves.append((x, y + 2))
            elif p.color != self.color:
                moves.append((x, y + 2))

        # MIDDLE LEFT
        if x > 1:
            p = board[x - 2][y]
            if p == 0:
                moves.append((x - 2, y))
            elif p.color != self.color:
                moves.append((x - 2, y))

        # MIDDLE RIGHT
        if x < 10:
            p = board[x + 2][y]
            if p == 0:
                moves.append((x + 2, y))
            elif p.color != self.color:
                moves.append((x + 2, y))

        return moves

# TODO: Define promotion to White Horse
class Lance(Piece):
    img = 12

    def valid_moves(self, board):
        y = self.row
        x = self.col
        moves = []

        # White is ranged down
        if self.color == "w":
            for dy in range(y + 1, 12, 1):
                p = board[x][dy]
                if p == 0:
                    moves.append((x, dy))
                elif p.color != self.color:
                    moves.append((x, dy))
                    break
                else:
                    break

        # Black is ranged up
        else:
            for dy in range(y - 1, -1, -1):
                p = board[x][dy]
                if p == 0:
                    moves.append((x, dy))
                elif p.color != self.color:
                    moves.append((x, dy))
                    break
                else:
                    break

        return moves

class Lion(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.lion = True

    img = 13

    # TODO: These are the valid moves for a king. We need to adjust them to Lion moves
    def lion_moves_2(self, board):
        move_list = []
        for move in self.lion_moves(board):
            if board[move[0]][move[1]] == 0:
                move_list.append(move)
            elif board[move[0]][move[1]].color != self.color:
                move_list.append(move)
        return move_list

    def lion_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        if y > 0:
            # TOP LEFT
            if x > 0:
                p = board[x - 1][y - 1]
                if p == 0 or p.color == self.color:
                    moves.append((x - 1, y - 1, False))
                elif p.color != self.color:
                    moves.append((x - 1, y - 1, True))


            # TOP MIDDLE
            p = board[x][y - 1]
            if p == 0 or p.color == self.color:
                moves.append((x, y - 1, False))
            elif p.color != self.color:
                moves.append((x, y - 1, True))

            # TOP RIGHT
            if x < 11:
                p = board[x + 1][y -  1]
                if p == 0 or p.color == self.color:
                    moves.append((x + 1, y - 1, False))
                elif p.color != self.color:
                    moves.append((x + 1, y - 1, True))

        if y < 11:
            # BOTTOM LEFT
            if x > 0:
                p = board[x - 1][y + 1]
                if p == 0 or p.color == self.color:
                    moves.append((x - 1, y + 1, False))
                elif p.color != self.color:
                    moves.append((x - 1, y + 1, True))

            # BOTTOM MIDDLE
            p = board[x][y + 1]
            if p == 0 or p.color == self.color:
                moves.append((x, y + 1, False))
            elif p.color != self.color:
                moves.append((x, y + 1, True))

            # BOTTOM RIGHT
            if x < 11:
                p = board[x + 1][y + 1]
                if p == 0 or p.color == self.color:
                    moves.append((x + 1, y + 1, False))
                elif p.color != self.color:
                    moves.append((x + 1, y + 1, True))

        # MIDDLE LEFT
        if x > 0:
            p = board[x - 1][y]
            if p == 0 or p.color == self.color:
                moves.append((x - 1, y, False))
            elif p.color != self.color:
                moves.append((x - 1, y, True))

        # MIDDLE RIGHT
        if x < 11:
            p = board[x + 1][y]
            if p == 0 or p.color == self.color:
                moves.append((x + 1, y, False))
            elif p.color != self.color:
                moves.append((x + 1, y, True))

        return moves

# TODO: Define promotion to Tokin
class Pawn(Piece):
    img = 14

    def valid_moves(self, board):
        y = self.row
        x = self.col
        moves = []
        try:
            if self.color == "w":
                if y < 11:
                    p = board[x][y + 1]
                    if p == 0:
                        moves.append((x, y + 1))

                    if x > 0:
                        p = board[x - 1][y + 1]
                        if p != 0:
                            if p.color != self.color:
                                moves.append((x - 1, y + 1))

            # BLACK
            else:

                if y > 0:
                    p = board[x][y - 1]
                    if p == 0:
                        moves.append((x, y - 1))

                if x > 0:
                    p = board[x - 1][y - 1]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((x - 1, y - 1))

        except:
            exit(1)

        return moves

# TODO: Define promotion to Free King
class Phoenix(Piece):
    img = 15

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        if y > 0:
            # TOP MIDDLE
            p = board[x][y - 1]
            if p == 0:
                moves.append((x, y - 1))
            elif p.color != self.color:
                moves.append((x, y - 1))

        if y > 1:
            # TOP JUMP LEFT
            if x > 1:
                p = board[x - 2][y - 2]
                if p == 0:
                    moves.append((x - 2, y - 2,))
                elif p.color != self.color:
                    moves.append((x - 2, y - 2,))

            # TOP JUMP RIGHT
            if x < 10:
                p = board[x + 2][y - 2]
                if p == 0:
                    moves.append((x + 2, y - 2,))
                elif p.color != self.color:
                    moves.append((x + 2, y - 2,))

        if y < 11:
            # BOTTOM MIDDLE
            p = board[x][y + 1]
            if p == 0:
                moves.append((x, y + 1))
            elif p.color != self.color:
                moves.append((x, y + 1))

        if y < 10:
            # BOTTOM JUMP LEFT
            if x > 1:
                p = board[x - 2][y + 2]
                if p == 0:
                    moves.append((x - 2, y + 2,))
                elif p.color != self.color:
                    moves.append((x - 2, y + 2,))

            # BOTTOM JUMP RIGHT
            if x < 10:
                p = board[x + 2][y + 2]
                if p == 0:
                    moves.append((x + 2, y + 2))
                elif p.color != self.color:
                    moves.append((x + 2, y + 2))

        # MIDDLE LEFT
        if x > 0:
            p = board[x - 1][y]
            if p == 0:
                moves.append((x - 1, y))
            elif p.color != self.color:
                moves.append((x - 1, y))

        # MIDDLE RIGHT
        if x < 11:
            p = board[x + 1][y]
            if p == 0:
                moves.append((x + 1, y))
            elif p.color != self.color:
                moves.append((x + 1, y))

        return moves

# TODO: Define promotion to Dragon King
class Rook(Piece):
    img = 16

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        # UP RANGE
        for dy in range(y - 1, -1, -1):
            p = board[x][dy]
            if p == 0:
                moves.append((x, dy))
            elif p.color != self.color:
                moves.append((x, dy))
                break
            else:
                break

        # DOWN RANGE
        for dy in range(y + 1, 12, 1):
            p = board[x][dy]
            if p == 0:
                moves.append((x, dy))
            elif p.color != self.color:
                moves.append((x, dy))
                break
            else:
                break

        # LEFT RANGE
        for dx in range(x - 1, -1, -1):
            p = board[dx][y]
            if p == 0:
                moves.append((dx, y))
            elif p.color != self.color:
                moves.append((dx, y))
                break
            else:
                break

        # RIGHT RANGE
        for dx in range(x + 1, 12, 1):
            p = board[dx][y]
            if p == 0:
                moves.append((dx, y))
            elif p.color != self.color:
                moves.append((dx, y))
                break
            else:
                break

        return moves

# TODO: Define promotion to Whale
class ReverseChariot(Piece):
    img = 17

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        # UP RANGE
        for dy in range(y - 1, -1, -1):
            p = board[x][dy]
            if p == 0:
                moves.append((x, dy))
            elif p.color != self.color:
                moves.append((x, dy))
                break
            else:
                break

        # DOWN RANGE
        for dy in range(y + 1, 12, 1):
            p = board[x][dy]
            if p == 0:
                moves.append((x, dy))
            elif p.color != self.color:
                moves.append((x, dy))
                break
            else:
                break

        return moves

# TODO: Define promotion to Vertical Mover
class SilverGeneral(Piece):
    img = 18

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        if y > 0:
            if self.color == "b":
                # TOP LEFT
                if x > 0:
                    p = board[x - 1][y - 1]
                    if p == 0:
                        moves.append((x - 1, y - 1,))
                    elif p.color != self.color:
                        moves.append((x - 1, y - 1,))

            # TOP MIDDLE
            p = board[x][y - 1]
            if p == 0:
                moves.append((x, y - 1))
            elif p.color != self.color:
                moves.append((x, y - 1))

            if self.color == "b":
                # TOP RIGHT
                if x < 11:
                    p = board[x + 1][y - 1]
                    if p == 0:
                        moves.append((x + 1, y - 1,))
                    elif p.color != self.color:
                        moves.append((x + 1, y - 1,))

        if y < 11:
            if self.color == "w":
                # BOTTOM LEFT
                if x > 0:
                    p = board[x - 1][y + 1]
                    if p == 0:
                        moves.append((x - 1, y + 1,))
                    elif p.color != self.color:
                        moves.append((x - 1, y + 1,))

            # BOTTOM MIDDLE
            p = board[x][y + 1]
            if p == 0:
                moves.append((x, y + 1))
            elif p.color != self.color:
                moves.append((x, y + 1))

            if self.color == "w":
                # BOTTOM RIGHT
                if x < 11:
                    p = board[x + 1][y + 1]
                    if p == 0:
                        moves.append((x + 1, y + 1))
                    elif p.color != self.color:
                        moves.append((x + 1, y + 1))

        return moves

# TODO: Define promotion to Free Boar
class SideMover(Piece):
    img = 19

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        if y > 0:
            # TOP MIDDLE
            p = board[x][y - 1]
            if p == 0:
                moves.append((x, y - 1))
            elif p.color != self.color:
                moves.append((x, y - 1))

        if y < 11:
            # BOTTOM MIDDLE
            p = board[x][y + 1]
            if p == 0:
                moves.append((x, y + 1))
            elif p.color != self.color:
                moves.append((x, y + 1))

        # LEFT RANGE
        for dx in range(x - 1, -1, -1):
            p = board[dx][y]
            if p == 0:
                moves.append((dx, y))
            elif p.color != self.color:
                moves.append((dx, y))
                break
            else:
                break

        # RIGHT RANGE
        for dx in range(x + 1, 12, 1):
            p = board[dx][y]
            if p == 0:
                moves.append((dx, y))
            elif p.color != self.color:
                moves.append((dx, y))
                break
            else:
                break

        return moves

# TODO: Define promotion to Flying Ox
class VerticalMover(Piece):
    img = 20

    def valid_moves(self, board):
        y = self.row
        x = self.col

        moves = []

        # UP RANGE
        for dy in range(y - 1, -1, -1):
            p = board[x][dy]
            if p == 0:
                moves.append((x, dy))
            elif p.color != self.color:
                moves.append((x, dy))
                break
            else:
                break

        # DOWN RANGE
        for dy in range(y + 1, 12, 1):
            p = board[x][dy]
            if p == 0:
                moves.append((x, dy))
            elif p.color != self.color:
                moves.append((x, dy))
                break
            else:
                break

        # MIDDLE LEFT
        if x > 0:
            p = board[x - 1][y]
            if p == 0:
                moves.append((x - 1, y))
            elif p.color != self.color:
                moves.append((x - 1, y))

        # MIDDLE RIGHT
        if x < 11:
            p = board[x + 1][y]
            if p == 0:
                moves.append((x + 1, y))
            elif p.color != self.color:
                moves.append((x + 1, y))
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
