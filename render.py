import pygame
from validate import validate_number
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


def render_numbers(screen, board):
    font = pygame.font.Font(None, 36)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, (0, 0, 0))
                screen.blit(text, (70 + j * 50, 65 + i * 50))


def render_input_boxes(screen):
    #to be done
    return None

def generate_numbers(screen, board):
    counter = random.randint(50, 65)
    for i in range(counter):
        found = False
        while not found:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)
            if validate_number(board, row, col, num) and board[row][col] == 0:
                board[row][col] = num
                found = True
