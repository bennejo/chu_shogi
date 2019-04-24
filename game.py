import pygame
import os
from board import Board

pygame.init()

board = pygame.transform.scale(pygame.image.load(os.path.join("img","board.png")), (1000, 1000))



clock = pygame.time.Clock()

chu_shogi_board = Board()
chu_shogi_board.create_board()
chu_shogi_board.print_board()



def main():
    quit_game = False

    while not quit_game:

        win.blit(board, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
                quit()
                pygame.quit()

            pygame.display.update()
            clock.tick(60)

width = 1000
height = 1000
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chu Shogi")
main()
