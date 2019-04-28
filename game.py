import pygame as pg
import os
from board import Board
from login import splash_login
from utils import click
from utils import move_string
from client import send_move

pg.init()

board = pg.transform.scale(pg.image.load(os.path.join("img","board.png")), (1000, 1000))
rect = (0,0,1000,1000)


clock = pg.time.Clock()

bo = Board()


def redraw_gameWindow(win):
    win.blit(board, (0, 0))
    bo.draw(win)

    pg.display.update()


def main():
    quit_game = False

    # The first player to join the game takes black and waits for the other player to make the first move
    # valid values for 'phase' are 'select', 'lion', 'move', and 'wait'
    # the 'lion' value of 'phase' denotes the phase in which the first move of the lion is selected
    # the lion will take that position on the board (offset to show any piece underneath it in the case of moving
    # over friendly pieces) and will be highlighted as selected and the phase changed to 'move' for the second move
    # to be selected. [N.B. eventually we will need to distinguish between capturing an enemy piece on the first lion
    # move and flying over the piece, as those are both valid moves]

    username, login_result = splash_login(win, clock)


    if login_result[0:5] == b'ERROR':
        # TODO: display error message and wait some few seconds
        print(login_result)
        quit_game = True
        quit()
        pg.quit()

    elif login_result == b'joined game':
        bo.set_color('b')
        phase = 'wait'
        print("DEBUG: logged in as black, phase is wait")

    else:
        bo.set_color('w')
        phase = 'select'
        print("DEBUG: logged in a white, phase is select")

    while not quit_game:

        redraw_gameWindow(win)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game = True
                quit()
                pg.quit()

            if event.type == pg.MOUSEBUTTONUP:
                print("Click event")
                if phase == 'select':
                    pos = pg.mouse.get_pos()
                    i, j = click(pos)
                    result = bo.select(i, j)
                    if result == 'lion':
                        phase = 'lion'
                    elif result == 'selected':
                        print("DEBUG: phase is now move")
                        phase = 'move'

                    redraw_gameWindow(win)

                elif phase == 'move':
                    print("in move click handler")
                    pos = pg.mouse.get_pos()
                    i, j = click(pos)

                    result = bo.move(i, j)
                    print("move result is: " + result)
                    if result == 'no selection' or result == 'deselected':
                        phase = 'select'
                        print('DEBUG: piece deselected, phase is now select')
                    elif result == 'valid move':
                        print("DEBUG valid move at " + str(i) + ", " + str(j))
                        send_string = move_string(bo.selected, [i, j])
                        send_result = send_move(username, send_string)
                        if send_result:
                            print("DEBUG: successfully sent (" + send_string + ") to server")
                            phase = 'wait'
                            bo.do_move(send_string)
                        else:
                            # TODO: handle this a bit more gracefully
                            print('ERROR: Server error sending move.')
                            quit_game = True
                            quit()
                            pg.quit()

                    redraw_gameWindow(win)

            pg.display.update()
            clock.tick(60)


width = 1000
height = 1000
win = pg.display.set_mode((width, height))
pg.display.set_caption("Chu Shogi")
main()
