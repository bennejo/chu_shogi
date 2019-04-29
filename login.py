import pygame as pg
import os
from client import join_game


def splash_login(win, clock):
    splash_screen = pg.transform.scale(pg.image.load(os.path.join("img", "splash.png")), (1000, 1000))

    username = None
    win.blit(splash_screen, (0, 0))

    start_game = False

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

    return username, login_result