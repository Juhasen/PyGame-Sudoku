import pygame
import sys

from render import draw_board, draw_numbers, generate_numbers, draw_description, clear_screen, draw_win
from mouse_action import handle_click
from validate import solve_sudoku

WIDTH = 880
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
    img = pygame.image.load('icon.png')
    pygame.display.set_icon(img)

    screen.fill((211, 211, 211))
    generated_cells = []
    draw_board(screen)
    board = generate_numbers(generated_cells)
    draw_description(screen)
    pos = []
    row, col = 0, 0
    board_solved = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    clear_screen(screen)
                    board = generate_numbers(generated_cells)
                    board_solved = False
                    break
                elif event.key == pygame.K_s and not board_solved:
                    old_board = [row[:] for row in board]
                    for i in range(9):
                        for j in range(9):
                            if (i, j) in generated_cells:
                                board[i][j] = 0
                    solve_sudoku(board)
                    how_many_errors = 0
                    wrong_cells = []
                    for i in range(9):
                        for j in range(9):
                            if old_board[i][j] != board[i][j]:
                                wrong_cells.append((i, j))
                                how_many_errors += 1
                    draw_win(screen, how_many_errors, wrong_cells)
                    board_solved = True
                    break

            if event.type == pygame.MOUSEBUTTONDOWN and not board_solved:
                pos = handle_click(screen, board)
                if pos:
                    row, col = pos
            elif event.type == pygame.KEYDOWN and pos and pos in generated_cells and not board_solved:
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

        draw_numbers(screen, board, generated_cells)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()
