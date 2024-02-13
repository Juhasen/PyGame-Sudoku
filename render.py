import pygame
from validate import validate_number, solve_sudoku
import random


def render_board(screen):
    # Draw the grid lines
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 5)
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 5)
        else:
            pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500))
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i))

    # draw the numbers above the grid
    font = pygame.font.Font(None, 36)
    for i in range(9):
        text = font.render(str(i + 1), True, (0, 0, 0))
        screen.blit(text, (70 + i * 50, 20))
        screen.blit(text, (20, 65 + i * 50))


def render_numbers(screen, board, generated_cells):
    # clear cells
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(screen, (211, 211, 211), (55 + j * 50, 55 + i * 50, 40, 40))
    font = pygame.font.Font(None, 36)
    for i in range(9):
        for j in range(9):
            correct = validate_number(board, i, j, board[i][j])
            if board[i][j] != 0 and (i, j) not in generated_cells and not correct:
                print("Invalid number at", i, j, board[i][j])
                text = font.render(str(board[i][j]), True, (255, 0, 0))
                screen.blit(text, (70 + j * 50, 65 + i * 50))
            elif board[i][j] != 0 and (i, j) not in generated_cells and correct:
                print("Valid number at", i, j, board[i][j])
                text = font.render(str(board[i][j]), True, (50, 205, 50))
                screen.blit(text, (70 + j * 50, 65 + i * 50))
            elif board[i][j] != 0 and (i, j) in generated_cells:
                text = font.render(str(board[i][j]), True, (0, 0, 0))
                screen.blit(text, (70 + j * 50, 65 + i * 50))


def generate_numbers(board, generated_cells):
    generated_cells.clear()
    board = [[0 for i in range(9)] for j in range(9)]
    board[0] = random.sample(range(1, 10), 9)
    solve_sudoku(board)

    all_cells = [(i, j) for i in range(9) for j in range(9)]
    cells_to_keep = random.sample(all_cells, random.randint(40, 50))

    for i, j in set(all_cells) - set(cells_to_keep):
        board[i][j] = 0
        generated_cells.append((i, j))

    return board

def render_description(screen):
    font = pygame.font.Font(None, 25)
    click = font.render("Click on a cell to select it", True, (0, 0, 0))
    press = font.render("Then press a number to fill the cell", True, (0, 0, 0))
    delete = font.render("Press 'd' to delete a number", True, (0, 0, 0))
    reset = font.render("Press 'r' to reset the board", True, (0, 0, 0))
    solve = font.render("Press 's' to solve the board", True, (0, 0, 0))
    cell = font.render("Selected cell:", True, (0, 0, 0))
    quit_app = font.render("Press 'q' to quit the game", True, (0, 0, 0))
    screen.blit(click, (550, 50))
    screen.blit(press, (550, 100))
    screen.blit(delete, (550, 150))
    screen.blit(reset, (550, 200))
    screen.blit(solve, (550, 250))
    screen.blit(cell, (550, 350))
    screen.blit(quit_app, (550, 490))


def clear_screen(screen):
    screen.fill((211, 211, 211))
    render_board(screen)
    render_description(screen)
