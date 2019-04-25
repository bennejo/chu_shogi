import pygame
import os
from board import Board

pygame.init()

board = pygame.transform.scale(pygame.image.load(os.path.join("img","board.png")), (1000, 1000))



clock = pygame.time.Clock()

def redraw_gameWindow(win, color):
    win.blit(board, (0, 0))
    bo.draw(win, color)

    pygame.display.update()

def click(pos):
    pass

def main():
    global turn, bo


    bo = Board(12,12)
    color = bo.turn
    quit_game = False

    while not quit_game:

        redraw_gameWindow(win, color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
                quit()
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONUP and color != "s":
                if color == bo.turn and bo.ready:
                    pos = pygame.mouse.get_pos()
                    i, j = click(pos)


            pygame.display.update()
            clock.tick(60)

width = 1000
height = 1000
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chu Shogi")
main()
