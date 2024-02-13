import pygame
import sys

from render import render_board, render_numbers, generate_numbers
from mouse_action import track_mouse

WIDTH = 750
HEIGHT = 550

if __name__ == "__main__":
    pygame.init()
    pygame.display.init()
    if pygame.display.get_init() == 0:
        pygame.error("Display not initialized")
        pygame.quit()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    pygame.display.set_caption("Sudoku")
    img = pygame.image.load("icon.png")
    pygame.display.set_icon(img)

    screen.fill((211, 211, 211))

    board = [[0 for i in range(9)] for j in range(9)]

    render_board(screen)
    generate_numbers(screen, board)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if pygame.mouse.get_pressed()[0]:
            pos = track_mouse(screen)

            font = pygame.font.Font(None, 36)
            text = font.render(str(pos), True, (0, 0, 0))
            screen.blit(text, (550, 300))

        render_numbers(screen, board)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()
