import pygame as pg
import os
from board import Board

pg.init()

board = pg.transform.scale(pg.image.load(os.path.join("img","board.png")), (1000, 1000))
rect = (0,0,1000,1000)


clock = pg.time.Clock()

def redraw_gameWindow(win, color):
    win.blit(board, (0, 0))
    bo.draw(win, color)

    pg.display.update()

def click(pos):
    """
    :return: pos (x, y) in range 0-11 0-11
    """
    x = pos[0]
    y = pos[1]
    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[1] + rect[3]:
            divX = x - rect[0]
            divY = y - rect[1]
            i = int(divX / (rect[2]/12))
            j = int(divY / (rect[3]/12))
            return i, j

    return -1, -1


def main():
    global turn, bo

    bo = Board(12,12)
    color = bo.turn
    quit_game = False

    while not quit_game:

        redraw_gameWindow(win, color)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game = True
                quit()
                pg.quit()

            if event.type == pg.MOUSEBUTTONUP and color != "s":
                if color == bo.turn:
                    pos = pg.mouse.get_pos()
                    # TODO: implement this function
                    bo.update_moves()
                    i, j = click(pos)
                    bo.select(i, j, color)
                    redraw_gameWindow(win, color)
                    color = bo.turn

            pg.display.update()
            clock.tick(60)


width = 1000
height = 1000
win = pg.display.set_mode((width, height))
pg.display.set_caption("Chu Shogi")
main()
