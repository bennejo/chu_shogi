import pygame as pg
import os
from board import Board

pg.init()

splash_screen = pg.transform.scale(pg.image.load(os.path.join("img","splash.png")), (1000, 1000))
board = pg.transform.scale(pg.image.load(os.path.join("img","board.png")), (1000, 1000))

clock = pg.time.Clock()

chu_shogi_board = Board()
chu_shogi_board.create_board()
chu_shogi_board.print_board()


def main():
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

        pg.display.flip()
        clock.tick(30)

    while not quit_game:

        win.blit(board, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game = True
                quit()
                pg.quit()

            pg.display.update()
            clock.tick(60)

width = 1000
height = 1000
win = pg.display.set_mode((width, height))
pg.display.set_caption("Chu Shogi")
main()
