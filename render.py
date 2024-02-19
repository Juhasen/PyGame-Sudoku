import pygame
from validate import validate_number, solve_sudoku
import random


def draw_board(screen):
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


def draw_numbers(screen, board, ungenerated_cells):
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(screen, (211, 211, 211), (55 + j * 50, 55 + i * 50, 40, 40))
    font = pygame.font.Font(None, 36)

    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (50, 205, 50)

    for i in range(0, 9):
        for j in range(0, 9):
            correct = validate_number(board, i, j, board[i][j])
            if (i, j) not in ungenerated_cells:  # if the cell is generated, draw black number
                text = font.render(str(board[i][j]), True, black)
                screen.blit(text, (70 + j * 50, 62 + i * 50))
            elif board[i][j] != 0 and correct:
                text = font.render(str(board[i][j]), True, green)
                screen.blit(text, (70 + j * 50, 62 + i * 50))
            elif board[i][j] != 0 and not correct:
                text = font.render(str(board[i][j]), True, red)
                screen.blit(text, (70 + j * 50, 62 + i * 50))


def generate_numbers(ungenerated_cells):
    ungenerated_cells.clear()
    board = [[0 for i in range(9)] for j in range(9)]
    board[0] = random.sample(range(1, 10), 9)
    solve_sudoku(board)

    all_cells = [(i, j) for i in range(9) for j in range(9)]
    cells_to_keep = random.sample(all_cells, random.randint(40, 50))

    for i, j in set(all_cells) - set(cells_to_keep):
        board[i][j] = 0
        ungenerated_cells.append((i, j))

    return board


def draw_description(screen):
    font = pygame.font.Font(None, 25)
    click = font.render("Click on a cell to select it", True, (0, 0, 0))
    press = font.render("Then press a number to fill the cell", True, (0, 0, 0))
    range1_9 = font.render("The numbers range from 1 to 9", True, (0, 0, 0))
    delete = font.render("Press 'd' to delete a number", True, (0, 0, 0))
    reset = font.render("Press 'r' to reset the board", True, (0, 0, 0))
    solve = font.render("Press 's' to show the answer", True, (0, 0, 0))
    cell = font.render("Selected cell:", True, (0, 0, 0))
    quit_app = font.render("Press 'q' to quit the game", True, (0, 0, 0))
    screen.blit(click, (550, 50))
    screen.blit(press, (550, 100))
    screen.blit(range1_9, (550, 150))
    screen.blit(delete, (550, 200))
    screen.blit(reset, (550, 250))
    screen.blit(solve, (550, 300))
    screen.blit(cell, (550, 350))
    screen.blit(quit_app, (550, 490))


def clear_screen(screen):
    screen.fill((211, 211, 211))
    draw_board(screen)
    draw_description(screen)
