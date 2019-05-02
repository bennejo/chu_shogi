import pygame as pg
import os
from board import Board
from login import splash_login
from utils import click
from utils import move_string
from client import send_move
from client import get_move

pg.init()

board = pg.transform.scale(pg.image.load(os.path.join("img","board.png")), (1000, 1000))
rect = (0,0,1000,1000)


clock = pg.time.Clock()

bo = Board()
bo.update_moves()


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
        bo.update_moves()

        if phase == 'wait':
            clock.tick(200)
            result = get_move(username)

            if result:
                print("DEBUG: got move (" + result.decode('utf-8') + ") from server, phase is select")
                bo.do_move(result.decode('utf-8'))
                phase = 'select'


                redraw_gameWindow(win)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game = True
                quit()
                pg.quit()

            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                if bo.selected:
                    selected_pos = (bo.selected.col, bo.selected.row)

                if phase == 'select':
                    x, y, top = click(pos)
                    result = bo.select(x, y)
                    if result == 'lion':
                        print('DEBUG: setting phase to lion')
                        phase = 'lion'
                    elif result == 'selected':
                        phase = 'move'

                    redraw_gameWindow(win)

                elif phase == 'move':
                    x, y, top = click(pos)
                    result = bo.move(x, y)
                    if result == 'no selection' or result == 'deselected':
                        phase = 'select'
                    elif result == 'valid move':
                        send_string = move_string(selected_pos, [x, y])
                        send_result = send_move(username, send_string)
                        if send_result:
                            phase = 'wait'
                            bo.do_move(send_string)
                        else:
                            # TODO: handle this a bit more gracefully
                            print('ERROR: Server error sending move.')
                            quit_game = True
                            quit()
                            pg.quit()

                    redraw_gameWindow(win)

                elif phase == 'lion':
                    x, y, fly = click(pos)
                    result = bo.lion_move_1(x, y, fly)
                    print("lion_move_1 returned: " + result)
                    if result == 'no selection' or result == 'deselected':
                        phase = 'select'
                    elif result == 'regular move': # for +DH and +DK
                        send_string = move_string(selected_pos, [x, y])
                        send_result = send_move(username, send_string)
                        if send_result:
                            phase = 'wait'
                            bo.do_move(send_string)
                        else:
                            # TODO: handle this a bit more gracefully
                            print('ERROR: Server error sending move.')
                            quit_game = True
                            quit()
                            pg.quit()
                    elif result == 'lion move':
                        send_string = move_string(selected_pos, [x, y], fly=False)
                        # update location of lion
                        bo.selected.change_pos([x, y])
                        bo.selected.lion_2 = True
                        phase = 'lion2'
                    elif result == 'lion flies':
                        send_string = move_string(selected_pos, [x, y], fly=True)
                        bo.selected.change_pos([x, y])
                        bo.selected.flying = True
                        bo.selected.lion_2 = True
                        phase = 'lion2'
                    redraw_gameWindow(win)

                elif phase == 'lion2':

                    x, y, top = click(pos)
                    result = bo.lion_move_2(x, y)
                    print("in lion2 phase click handler result is: " + result)
                    if result == 'no selection':
                        raise ValueError('Lion type piece should be selected')
                    elif result == 'valid move':

                        send_string += ", " + move_string(selected_pos, [x, y], land=True)
                        bo.selected.flying = False
                        bo.selected.lion_2 = False
                        send_result = send_move(username, send_string)

                        if send_result:
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
