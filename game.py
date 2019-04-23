import pygame
from board import Board

pygame.init()
game_display = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption("Chu Shogi")
clock = pygame.time.Clock()

chu_shogi_board = Board()
chu_shogi_board.create_board()
chu_shogi_board.print_board()

all_tiles = []
all_pieces = []

pygame.draw.rect(game_display, (100, 100, 100), [0, 0, 100, 100])

def squares(x, y, w, h, color):
    pygame.draw.rect(game_display, color, [x, y, w, h])
    all_tiles.append([color, [x, y, w, h]])


quit_game = False

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
            quit()
            pygame.quit()

    pygame.display.update()
    clock.tick(60)
