import pygame
import sys

from render import render_board, render_numbers, generate_numbers, render_description, clear_screen
from mouse_action import handle_click
from validate import solve_sudoku

WIDTH = 850
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
    generated_cells = []
    render_board(screen)
    generate_numbers(board, generated_cells)
    render_description(screen)
    pos = []
    row, col = 0, 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                board = [[0 for i in range(9)] for j in range(9)]
                clear_screen(screen)
                generate_numbers(board, generated_cells)
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = handle_click(screen, board)
                if pos:
                    row, col = pos
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                running = False
            elif event.type == pygame.KEYDOWN and pos and pos not in generated_cells:
                if event.key == pygame.K_1:
                    board[row][col] = 1
                elif event.key == pygame.K_2:
                    board[row][col] = 2
                elif event.key == pygame.K_3:
                    board[row][col] = 3
                elif event.key == pygame.K_4:
                    board[row][col] = 4
                elif event.key == pygame.K_5:
                    board[row][col] = 5
                elif event.key == pygame.K_6:
                    board[row][col] = 6
                elif event.key == pygame.K_7:
                    board[row][col] = 7
                elif event.key == pygame.K_8:
                    board[row][col] = 8
                elif event.key == pygame.K_9:
                    board[row][col] = 9
                elif event.key == pygame.K_d:
                    board[row][col] = 0
                elif event.key == pygame.K_s:
                    solve_sudoku(board)

        render_numbers(screen, board, generated_cells)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()
