import pygame as pg
import os
from board import Board
from client import join_game

pg.init()

board = pg.transform.scale(pg.image.load(os.path.join("img","board.png")), (1000, 1000))
splash_screen = pg.transform.scale(pg.image.load(os.path.join("img","splash.png")), (1000, 1000))
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

    username = None

    win.blit(splash_screen, (0,0))

    start_game = False
    quit_game = False

    input_box = pg.Rect(400, 250, 140, 32)
    font = pg.font.Font(None, 32)
    color_inactive = pg.Color('grey')
    color_active = pg.Color('black')
    color = color_inactive
    active = False
    text = ''

    while not start_game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game = True
                start_game = True
                quit()
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        if text != '':
                            username = text
                            start_game = True
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.

        input_box.w = 200
        # Blit the text.
        win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pg.draw.rect(win, color, input_box, 2)

        pg.display.update()
        clock.tick(30)

    # log into server with username
    login_result = join_game(username)

    if login_result[0:5] == b'ERROR':
        # TODO: display error message and wait some few seconds
        print(login_result)
        quit_game = True
        quit()
        pg.quit()

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
